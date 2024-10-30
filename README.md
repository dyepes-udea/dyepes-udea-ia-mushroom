# Proyecto Sustituto IA - MushroomClass
Este proyecto se realiza como parte de la materia Modelos I en la Universidad de Antioquia.
Se centra en el desarrollo de un modelo de machine learning para clasificar hongos utilizando características específicas de sus atributos. A lo largo de las diferentes fases, se han preparado, limpiado y analizado los datos para entrenar y evaluar un modelo de clasificación utilizando algoritmos como XGBoost. El proyecto también incluye la implementación de un contenedor Docker para facilitar la replicabilidad y el despliegue del modelo, así como una API REST para exponer el modelo y permitir la interacción con el proceso de entrenamiento y predicción.

Desarrollador por: Daniel Alejandro Yepes Mesa

## Estructura del Proyecto

El proyecto está dividido en dos fases principales, cada una con su propio conjunto de archivos:

### Fase 1

- **mushroomclass.py**: Script en Python que contiene el análisis y preprocesamiento de los datos, así como la implementación inicial del modelo.
- **MushroomClass.ipynb**: Notebook en Jupyter que detalla todo el proceso de análisis, visualización de datos y pruebas del modelo de clasificación.
- **readme.md**: Documento que explica el propósito y las instrucciones para ejecutar los scripts y notebooks en esta fase.

### Fase 2

- **Dockerfile**: Archivo de configuración que define la imagen Docker para crear un entorno reproducible donde ejecutar el modelo.
- **Predict.py**: Script que carga el modelo entrenado y genera predicciones basadas en los datos de prueba.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar los scripts en el entorno Docker.
- **test.csv**: Dataset de prueba utilizado para evaluar las predicciones del modelo.
- **train.csv**: Dataset de entrenamiento utilizado para entrenar el modelo de clasificación.
- **readme.md**: Documento con instrucciones detalladas sobre cómo construir, ejecutar y gestionar el contenedor Docker para entrenar y probar el modelo.

### Fase 3

- **apirest.py**: Script que define una API REST en Flask para interactuar con el modelo entrenado. Incluye dos endpoints:
  - `/train`: Entrena el modelo utilizando `train.py` y guarda el modelo actualizado.
  - `/predict`: Realiza predicciones utilizando `predict.py` y genera un archivo de salida con las predicciones.
- **Dockerfile**: Archivo Docker modificado para contenerizar la API y exponer los endpoints definidos en `apirest.py`.
- **input_test.csv** y **submission.csv**: Archivos de entrada y salida temporales utilizados por la API durante el procesamiento de predicciones.
- **README.md**: Documento que proporciona instrucciones detalladas sobre cómo construir, ejecutar y probar la API REST en el contenedor Docker.


## Propósito del Proyecto

El propósito de este proyecto es desarrollar un modelo de clasificación preciso que pueda predecir si un hongo es comestible o venenoso basado en sus características físicas. Para lograrlo, se ha dividido el proyecto en dos fases:

1. **Fase de Exploración y Desarrollo del Modelo**: En esta fase se exploran los datos, se realiza la limpieza y el preprocesamiento necesario, y se desarrolla un modelo inicial utilizando XGBoost, evaluando su desempeño con métricas como el MCC (coeficiente de correlación de Matthews).

2. **Fase de Contenerización y Despliegue**: En esta fase, se desarrolla un entorno Docker para contenerizar el modelo y sus dependencias, facilitando la replicabilidad y permitiendo que otros usuarios puedan ejecutar el modelo sin preocuparse por configuraciones locales. Los scripts están configurados para ejecutarse dentro del contenedor y generar las predicciones basadas en los datasets de entrada.

3. **Fase de Exposición de la API REST**: Esta fase expone el modelo entrenado y el proceso de predicción mediante una API REST creada con Flask. Con esta API, el modelo se puede integrar fácilmente en otros sistemas y aplicaciones mediante solicitudes HTTP. El contenedor Docker facilita el despliegue de la API en cualquier entorno, y los endpoints `/train` y `/predict` permiten interactuar con el modelo de manera directa para entrenar y realizar predicciones.

Este enfoque permite que el modelo sea fácilmente desplegable, reproducible y escalable en diferentes entornos, asegurando la consistencia y portabilidad del código. La API REST agrega una capa de accesibilidad adicional, permitiendo que el modelo sea integrado en otros servicios o interfaces de usuario.
