"""
Este script define una API REST usando Flask para interactuar con modelos de Machine Learning.
Incluye dos endpoints:
- /train: Ejecuta el script train.py para entrenar el modelo y guardar el archivo del modelo entrenado.
- /predict: Ejecuta el script predict.py para realizar predicciones sobre un archivo CSV de prueba.

Requisitos:
- Flask
- pandas
"""


from flask import Flask, request, jsonify
import subprocess
import os
import pandas as pd

app = Flask(__name__)

# Ruta temporal para archivos de entrada y salida
INPUT_FILE = "input_test.csv"  # Archivo temporal para guardar datos de predicción si se sube uno
DEFAULT_FILE = "test.csv"  # Archivo CSV predeterminado para predicciones si no se recibe un archivo en la solicitud
OUTPUT_FILE = "submission.csv"  # Archivo de salida donde se guardarán las predicciones

# Endpoint para entrenar el modelo
@app.route('/train', methods=['POST'])
def train():
    """
    Endpoint para entrenar el modelo.
    Ejecuta el script `train.py` con argumentos específicos para:
    - model_file: nombre del archivo donde se guardará el modelo.
    - data_train: archivo CSV de entrenamiento.
    - overwrite_model: opción para sobreescribir el modelo.
    
    Retorna:
    - JSON con el estado de éxito o error del entrenamiento.
    """
    try:
        # Ejecuta el script train.py sin modificarlo
        result = subprocess.run(
            ["python", "train.py", "--model_file", "model.pkl", "--data_train", "train.csv", "--overwrite_model"],
            capture_output=True, text=True
        )
        
        # Captura la salida y verifica si hubo algún error
        if result.returncode == 0:
            return jsonify({"status": "Modelo entrenado y guardado exitosamente."})
        else:
            return jsonify({"error": result.stderr}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para predecir con el modelo
@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para realizar predicciones usando el modelo entrenado.
    - Si se recibe un archivo CSV en la solicitud, se utiliza ese archivo.
    - Si no se recibe un archivo, se utiliza el archivo predeterminado `test.csv`.
    Ejecuta el script `predict.py` y procesa las predicciones generadas.

    Retorna:
    - JSON con el mensaje de archivo utilizado y las predicciones generadas o un mensaje de error.
    """
    try:
        # Verifica si se envió un archivo; si no, usa el archivo predeterminado
        if 'file' in request.files:
            # Guarda el archivo recibido temporalmente
            file = request.files['file']
            file.save(INPUT_FILE)
            input_file_used = INPUT_FILE
            message = "Predicciones realizadas con el archivo proporcionado."
        else:
            # Usa el archivo predeterminado
            input_file_used = DEFAULT_FILE
            message = "No se envió ningún archivo; se usó el archivo predeterminado para realizar predicciones."

        # Ejecuta el script predict.py con el archivo CSV de entrada
        result = subprocess.run(
            ["python", "predict.py", "--model_file", "model.pkl", "--data_file", input_file_used, "--output_file", OUTPUT_FILE],
            capture_output=True, text=True
        )
        
        # Lee el archivo de salida de predict.py y devuelve el resultado
        if result.returncode == 0:
            df_resultado = pd.read_csv(OUTPUT_FILE)
            predictions = df_resultado.to_dict(orient="records")
            return jsonify({"message": message, "predictions": predictions})
        else:
            return jsonify({"error": result.stderr}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)