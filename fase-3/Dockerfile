# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios en el contenedor
COPY train.py /app/train.py
COPY predict.py /app/predict.py
COPY train.csv /app/train.csv
COPY test.csv /app/test.csv
COPY model.pkl /app/model.pkl
COPY requirements.txt /app/requirements.txt
COPY apirest.py /app/apirest.py

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto 5000 para la API
EXPOSE 5000

# Comando de inicio para ejecutar la API
CMD ["python", "apirest.py"]
