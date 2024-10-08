# predict.py
# Este script carga un modelo previamente entrenado y lo utiliza para realizar predicciones
# sobre un dataset de prueba. Imputa valores faltantes en los datos, transforma las
# características categóricas y genera un archivo de salida en formato CSV con las predicciones.


import pandas as pd
import pickle
import argparse
import os
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OrdinalEncoder

# Argumentos de entrada
parser = argparse.ArgumentParser()
parser.add_argument('--model_file', type=str, default="model.pkl", help="Ruta del modelo guardado")
parser.add_argument('--data_file', type=str, default="test.csv", help="Archivo CSV de entrada para predicciones")
parser.add_argument('--output_file', type=str, default="submission.csv", help="Archivo de salida para las predicciones en formato submission")
args = parser.parse_args()

# Verificar si el archivo del modelo existe
if not os.path.exists(args.model_file):
    raise FileNotFoundError(f"El archivo del modelo {args.model_file} no existe.")

# Cargar el modelo
with open(args.model_file, "rb") as f:
    model = pickle.load(f)

# Cargar los datos para predicción
df_test = pd.read_csv(args.data_file)

# Asumiendo que el archivo de prueba tiene una columna 'id'
if 'id' not in df_test.columns:
    raise ValueError("El archivo de prueba debe contener una columna 'id'.")

# Imputar valores faltantes utilizando KNN
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

df_test = knn_impute(df_test)

# Transformar las columnas categóricas en valores ordinales (asegúrate de usar el mismo codificador que durante el entrenamiento)
cat_cols_test = df_test.select_dtypes(include=['object']).columns
ordinal_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df_test[cat_cols_test] = ordinal_encoder.fit_transform(df_test[cat_cols_test].astype(str))

# Predecir con el modelo
predicciones = model.predict(df_test)

# Mapear las predicciones de 0 a 'e' y 1 a 'p'
predicciones_mapeadas = ['e' if pred == 0 else 'p' for pred in predicciones]

# Crear el DataFrame con el formato de submission
df_resultado = pd.DataFrame({
    'id': df_test['id'],
    'class': predicciones_mapeadas
})

# Guardar las predicciones en un archivo CSV en formato de submission
df_resultado.to_csv(args.output_file, index=False)

print(f"Predicciones guardadas en {args.output_file}")
