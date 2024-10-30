# Usa una imagen base ligera de Python 3.9, optimizada para minimizar el tamaño del contenedor
FROM python:3.9-slim

# Establece el directorio de trabajo en /app dentro del contenedor
WORKDIR /app

# Copia el archivo de entrenamiento train.py en el directorio /app del contenedor
COPY train.py /app/train.py

# Copia el archivo de predicción predict.py en el directorio /app del contenedor
COPY predict.py /app/predict.py

# Copia el archivo de datos de entrenamiento en el directorio /app del contenedor
COPY train.csv /app/train.csv

# Copia el archivo de datos de prueba en el directorio /app del contenedor
COPY test.csv /app/test.csv

# Copia el modelo previamente entrenado en el directorio /app del contenedor
COPY model.pkl /app/model.pkl

# Copia el archivo de requerimientos para instalar las dependencias necesarias
COPY requirements.txt /app/requirements.txt

# Copia el archivo de API apirest.py para exponer los endpoints de entrenamiento y predicción
COPY apirest.py /app/apirest.py

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Instala todas las dependencias listadas en requirements.txt
RUN pip install -r requirements.txt

# Expone el puerto 5000 para que Flask esté accesible desde fuera del contenedor
EXPOSE 5000

# Establece el comando de inicio del contenedor: ejecuta apirest.py para iniciar la API
CMD ["python", "apirest.py"]
