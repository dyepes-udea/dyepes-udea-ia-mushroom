# Configuración y Uso de Docker para Entrenamiento y Predicción de un Modelo de Machine Learning

Este repositorio contiene todos los archivos y las instrucciones necesarias para configurar un contenedor Docker que permita entrenar y predecir con un modelo de machine learning utilizando Python y XGBoost. El contenedor incluye los scripts, datasets y todas las dependencias necesarias.

## Estructura del Proyecto

Dockerfile # Archivo de configuración de Docker train.py # Script para entrenar el modelo predict.py # Script para generar predicciones con el modelo entrenado train.csv # Archivo CSV por defecto para los datos de entrenamiento test.csv # Archivo CSV por defecto para los datos de prueba requirements.txt # Lista de dependencias del proyecto


## Prerrequisitos

- Asegúrate de tener Docker instalado en tu máquina. Puedes descargar e instalar Docker desde el [sitio oficial de Docker](https://www.docker.com/).

## Instrucciones para Configurar el Docker

### Paso 1: Clonar el Repositorio

Primero, clona el repositorio en tu máquina local y navega al directorio:

```bash
git clone <url_del_repositorio>
cd <directorio_del_repositorio>
```

### Paso 2: Construir la Imagen Docker

Construye la imagen Docker utilizando el Dockerfile proporcionado:

```bash
docker build -t mi-imagen-docker . 
```
- -t mi-imagen-docker asigna un nombre a la imagen Docker. Puedes cambiar mi-imagen-docker por un nombre de tu preferencia.
- El . indica que Docker debe usar el Dockerfile en el directorio actual.

### Paso 3: Ejecutar el Contenedor Docker

Para iniciar el contenedor Docker y acceder a una terminal interactiva:

```bash
docker run -it --name mi-contenedor mi-imagen-docker bash

```

- -it abre una terminal interactiva.
- -name mi-contenedor asigna un nombre al contenedor. Puedes cambiar mi-contenedor según prefieras.
- mi-imagen-docker debe coincidir con el nombre de la imagen que construiste anteriormente.

### Paso 4: Verificar los Archivos en el Contenedor

Una vez dentro del contenedor, deberías estar en el directorio /app. Verifica que todos los archivos necesarios estén presentes:

```bash
ls
```
Deberías ver los siguientes archivos:

train.py
predict.py
train.csv
test.csv
model.pkl
requirements.txt

## Uso de los Scripts
Los scripts train.py y predict.py pueden ejecutarse con parámetros opcionales (banderas) o sin ellos. Si no se proporcionan banderas, se usarán los archivos y configuraciones por defecto.

### Paso 1: Entrenamiento del Modelo (train.py)
Uso Mínimo (sin banderas)
Si ejecutas el script sin especificar banderas:

```bash
python train.py
```
Por defecto, el script utiliza train.csv como el archivo de datos para el entrenamiento y guarda el modelo en model.pkl.
Nota: Si model.pkl ya existe, no se sobrescribirá a menos que se especifique explícitamente.
Uso con Banderas
Puedes especificar las siguientes banderas para personalizar la ejecución:

--data_train: Especifica un archivo CSV de entrenamiento diferente.
--model_file: Especifica el nombre del archivo en el que se guardará el modelo entrenado.
--overwrite_model: Permite sobrescribir un modelo existente.
Ejemplo:

```bash
python train.py --data_train mi_dataset.csv --model_file mi_modelo.pkl --overwrite_model
```
En este ejemplo, se entrena el modelo con mi_dataset.csv, se guarda como mi_modelo.pkl y se sobrescribe cualquier archivo existente con ese nombre.

### Paso 2: Ejecución de Predicciones (predict.py)
Uso Mínimo (sin banderas)
Si ejecutas el script sin especificar banderas:

```bash
python predict.py
```

El script usará test.csv como archivo de datos para las predicciones y model.pkl como el modelo para generar las predicciones. El resultado se guardará en submission.csv.
Nota: Si no se encuentra un archivo model.pkl en el directorio, el script generará un error.
Uso con Banderas
Puedes personalizar el comportamiento del script de predicciones con las siguientes banderas:

- --data_file: Especifica un archivo CSV de datos de prueba diferente.
- --model_file: Especifica el modelo a utilizar para las predicciones.
- --output_file: Especifica el nombre del archivo de salida para guardar las predicciones.

Ejemplo:

```bash
python predict.py --data_file mi_prueba.csv --model_file mi_modelo.pkl --output_file mis_predicciones.csv
```

En este ejemplo, se utiliza mi_prueba.csv como archivo de prueba, mi_modelo.pkl como el modelo, y los resultados se guardan en mis_predicciones.csv.

## Acceso y Gestión de Archivos en el Contenedor Docker

### Comprobar los Archivos Generados
Para verificar que los archivos de salida (model.pkl o submission.csv) se hayan creado:

```bash
ls
```
Visualizar el Contenido de un Archivo
Para ver el contenido de cualquier archivo, utiliza cat:

```bash
cat submission.csv
```
### Copiar Archivos entre el Contenedor y la Máquina 

Para copiar un archivo, como submission.csv, desde el contenedor a tu máquina local:

```bash
docker cp mi-contenedor:/app/submission.csv ./submission.
```

Este comando copia submission.csv desde el directorio /app en mi-contenedor al directorio actual en tu máquina local.

### Copiar un Archivo de la Máquina Local al Contenedor
Para copiar un archivo desde tu máquina local al contenedor:

```bash
docker cp ./archivo_nuevo.csv mi-contenedor:/app/archivo_nuevo.csv
```

Este comando copia archivo_nuevo.csv desde tu directorio actual al directorio /app del contenedor mi-contenedor.

### Parar y Eliminar el Contenedor Docker
Cuando termines de trabajar, puedes detener el contenedor:

```bash
docker stop mi-contenedor
```
### Para eliminar el contenedor:

```bash
docker rm mi-contenedor
```
También puedes eliminar la imagen Docker si es necesario:

```bash

docker rmi mi-imagen-docker

```

## Resumen

Este contenedor Docker proporciona un entorno completo y fácil de usar para el entrenamiento y la predicción de modelos de machine learning. Siguiendo estas instrucciones, podrás configurar, ejecutar y gestionar eficientemente tus modelos de manera aislada y reproducible. Este enfoque no solo garantiza la portabilidad del código, sino que también simplifica la colaboración y el despliegue en distintos entornos. Si tienes cualquier duda o necesitas soporte adicional, no dudes en ponerte en contacto.
