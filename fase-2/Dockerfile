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

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando por defecto para iniciar una consola interactiva
CMD ["bash"]
