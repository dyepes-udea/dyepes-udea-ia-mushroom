# train.py
# Este script entrena un modelo de clasificación utilizando un dataset proporcionado.
# Se encarga de cargar, limpiar e imputar valores faltantes en los datos, codificar
# las características categóricas y entrenar un modelo XGBoost. Finalmente, guarda el
# modelo entrenado en un archivo para su posterior uso.

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.impute import KNNImputer
from xgboost import XGBClassifier
import pickle
import argparse
import os

# Argumentos de entrada
# Se utilizan para especificar las rutas y opciones al ejecutar el script desde la línea de comandos.
parser = argparse.ArgumentParser()
parser.add_argument('--model_file', type=str, default="model.pkl", help="Ruta para guardar el modelo")
parser.add_argument('--data_train', type=str, default="train.csv", help="Archivo CSV de entrada para entrenamiento")
parser.add_argument('--overwrite_model', action='store_true', help="Si se debe sobreescribir el modelo existente")
args = parser.parse_args()

# Cargar datos de entrenamiento
# Lee el archivo CSV proporcionado en la ruta especificada para cargar el dataset de entrenamiento.
df_train = pd.read_csv(args.data_train)

# Preprocesamiento de datos: tratamiento de valores faltantes y eliminación de columnas con muchos valores nulos
# Se eliminan las columnas que tienen más del 95% de valores nulos para limpiar el conjunto de datos.
missing_threshold = 0.95
high_missing_columns = df_train.columns[df_train.isnull().mean() > missing_threshold]
df_train = df_train.drop(columns=high_missing_columns)

# Imputación de valores nulos en columnas restantes
# Para las columnas categóricas se usa la moda (valor más frecuente) y para las numéricas, la mediana.
for column in df_train.columns:
    if df_train[column].isnull().any():
        if df_train[column].dtype == 'object':
            mode_value = df_train[column].mode()[0]
            df_train[column].fillna(mode_value, inplace=True)
        else:
            median_value = df_train[column].median()
            df_train[column].fillna(median_value, inplace=True)

# Imputación utilizando KNN
# Esta función aplica el algoritmo KNN para imputar valores faltantes basado en los vecinos más cercanos.
def knn_impute(df, n_neighbors=5):
    df_encoded = df.copy()
    for col in df_encoded.select_dtypes(include='object').columns:
        df_encoded[col] = df_encoded[col].astype('category').cat.codes
    knn_imputer = KNNImputer(n_neighbors=n_neighbors)
    df_imputed = pd.DataFrame(knn_imputer.fit_transform(df_encoded), columns=df_encoded.columns)
    for col in df.select_dtypes(include='object').columns:
        df_imputed[col] = df_imputed[col].round().astype(int).map(
            dict(enumerate(df[col].astype('category').cat.categories)))
    return df_imputed

# Aplicar la función de imputación KNN al dataset
df_train = knn_impute(df_train)

# Codificación de variables categóricas
# Se transforman las variables categóricas en valores numéricos ordinales para usarlas en el modelo.
cat_cols_train = df_train.select_dtypes(include=['object']).columns
ordinal_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df_train[cat_cols_train] = ordinal_encoder.fit_transform(df_train[cat_cols_train].astype(str))

# Codificación de la variable objetivo 'class'
# La variable objetivo se codifica en valores numéricos usando LabelEncoder.
le = LabelEncoder()
df_train['class'] = le.fit_transform(df_train['class'])

# Separar características (X) y variable objetivo (y)
# Separamos la variable objetivo 'class' del resto de las características para entrenar el modelo.
y = df_train['class']
X = df_train.drop(['class'], axis=1)

# Entrenar el modelo
# Se utiliza un clasificador XGBoost con hiperparámetros específicos para entrenar el modelo.
model = XGBClassifier(
    alpha=0.1,
    subsample=0.8,
    colsample_bytree=0.6,
    objective='binary:logistic',
    max_depth=14,
    min_child_weight=7,
    gamma=1e-6,
    n_estimators=100
)
model.fit(X, y)

# Guardar el modelo
# Se guarda el modelo entrenado en un archivo. Si el archivo ya existe, se verifica si se debe sobrescribir.
if args.overwrite_model or not os.path.exists(args.model_file):
    with open(args.model_file, "wb") as f:
        pickle.dump(model, f)
    print(f"Modelo guardado en {args.model_file}")
else:
    print(f"El modelo ya existe en {args.model_file}. Usa --overwrite_model para sobreescribir.")
