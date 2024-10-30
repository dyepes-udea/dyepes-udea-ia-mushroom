# Fase 3: API REST para Entrenamiento y Predicción

Esta fase se enfoca en exponer los scripts de entrenamiento y predicción mediante una API REST usando Flask. La API cuenta con dos endpoints principales: `/train` y `/predict`, que permiten entrenar el modelo y realizar predicciones sobre nuevos datos.

## Estructura de Archivos

- **apirest.py**: Script que define la API REST con Flask.
- **train.py**: Script de entrenamiento del modelo.
- **predict.py**: Script para realizar predicciones usando el modelo entrenado.
- **train.csv**: Archivo de datos de entrenamiento.
- **test.csv**: Archivo de datos para predicciones.
- **model.pkl**: Modelo entrenado guardado.
- **requirements.txt**: Lista de dependencias para el proyecto.
- **Dockerfile**: Archivo de configuración para construir el contenedor Docker.

## Requisitos Previos

- Tener Docker instalado en tu sistema.

## Construcción de la Imagen Docker

Para construir la imagen Docker del proyecto, asegúrate de estar en el directorio donde se encuentra el archivo `Dockerfile`. Luego ejecuta el siguiente comando:

```bash
docker build -t mushroom-api .
```

Este comando construirá la imagen Docker con el nombre mushroom-api.

## Ejecución del Contenedor Docker

Para iniciar el contenedor con la API Flask, ejecuta el siguiente comando:

```bash
docker run -p 5000:5000 mushroom-api
```

Esto ejecutará el contenedor y expondrá la API en http://127.0.0.1:5000.

## Uso de la API

### Endpoint /train

Este endpoint inicia el proceso de entrenamiento del modelo utilizando los datos del archivo train.csv.

URL: http://127.0.0.1:5000/train
Método: POST
Cuerpo de la Solicitud: No se requiere cuerpo de solicitud.

#### Ejemplo de Solicitud en Postman

Abre Postman y crea una nueva solicitud POST.
Ingresa la URL http://127.0.0.1:5000/train.
Haz clic en Send para enviar la solicitud.

#### Respuesta Exitosa:

```json
{
    "status": "Modelo entrenado y guardado exitosamente."
}
```

### Endpoint /predict

Este endpoint realiza una predicción utilizando el modelo entrenado. Puedes enviar un archivo CSV para las predicciones, o si no se proporciona uno, el endpoint usará test.csv como archivo predeterminado.

URL: http://127.0.0.1:5000/predict
Método: POST
Cuerpo de la Solicitud: Form-data con una clave file que contenga un archivo CSV.

#### Ejemplo de Solicitud en Postman

Abre Postman y crea una nueva solicitud POST.
Ingresa la URL http://127.0.0.1:5000/predict.
En la pestaña Body, selecciona form-data.
Agrega un campo file y sube un archivo CSV para predicciones. Si omites el archivo, se usará test.csv.
Haz clic en Send para enviar la solicitud.

#### Respuesta Exitosa con Archivo:

```json
{
    "message": "Predicciones realizadas con el archivo proporcionado.",
    "predictions": [
        {"id": 1, "class": "e"},
        {"id": 2, "class": "p"}
    ]
}
```
#### Respuesta Exitosa sin Archivo (usando test.csv):

```json
{
    "message": "No se envió ningún archivo; se usó el archivo predeterminado para realizar predicciones.",
    "predictions": [
        {"id": 1, "class": "e"},
        {"id": 2, "class": "p"}
    ]
}
```
## Notas Finales

Esta API permite interactuar con el modelo de manera flexible, facilitando el entrenamiento y las predicciones mediante solicitudes HTTP. Asegúrate de contar con los archivos de entrada adecuados (train.csv y test.csv) y el modelo (model.pkl) en el contenedor.
