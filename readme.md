# Despliegue en [Local]

A continuación, se describen los pasos para desplegar el proyecto localmente en tu máquina.

## 1 - tener Python instalado de lo contrario bajar ultima versión disponible en el siguiente link:

- [Descargar Python](https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe)

## 2. Configurar las variables del sistema

Asegúrate de que Python esté disponible en las **variables de entorno** o en el **PATH** de Windows. Esto es necesario para poder ejecutar los comandos de Python desde la terminal.

## 3. Actualizar `pip`

Es recomendable mantener `pip` actualizado. Para hacerlo, ejecuta el siguiente comando en tu terminal:

python -m pip install --upgrade pip

## 4 - verificar y instalado y usar entornos virtuales/contenedores para este y todos sus proyectos (buena practica)

si no se tiene usar:

pip install virtualenv

en la terminal de vscode/cmd/powerShell

## 5 - recrear el entorno con:

python -m venv .venv

## 6 - activar o desactivar el entorno virtual para este proyecto con 

-activar

.venv\Scripts\activate

-desactivar

deactivate

## 7 - instalar dependencias dentro del entorno virtual con 

pip install -r requirements.txt

## 8 - actualizar pip  en el entorno con:

python -m pip install --upgrade pip

## 9 actualizar dependencias para posterior uso (en caso de que se incluyan nuevas) con:

pip freeze > requirements.txt

## 10 - ejecutar con:

Python app.py

## Errores Conocidos
------------------------------------------------------------------------------------------------------
...[ Failed to build pandas
...ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (pandas) ]
------------------------------------------------------------------------------------------------------
para este error se sugiere descargar c++ tootls aquí: 
https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

