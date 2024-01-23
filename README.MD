<p align="center"><a href="https://www.python.org/" target="_blank"><img src="https://www.python.org/static/img/python-logo.png" width="500"></a></p>

# DJango Framework - Python
Front/Back-end Application

## Instalación de Python:

Instalar Python 3.12 desde el siguiente link:
<a href="https://www.python.org/downloads/release/python-3121/">Python 3.12</a>

- Al instalar verifique que la casilla de agregar al path este marcada.

## Instalación IDE de desarrollo:
Instalar Pycharm Jetbreains Community (outdate) desde el siguiente Link:
<a href="https://download.jetbrains.com/webstorm/Pycharm-2023.2.2.exe">Pycharm </a>

WebStorm Early Access Program (No subscription required) -- deprecated
<a href="https://www.jetbrains.com/webstorm/nextversion/">Pycharm EAP</a>

ó instalar Visual code desde el siguiente Link:
<a href="https://code.visualstudio.com/download">Visual Code</a>

## Instalación de Paquetes:
Para el correcto funcionamiento del siguiente proyecto siga los sigueintes pasos:
- [x] Instale Visual Tools C++ (aproximadamente 6.38GB) desde el siguiente link:
```
https://visualstudio.microsoft.com/es/visual-cpp-build-tools/
```
- Coloque el cheque en la opcion "Desarrollo para el escritorio con C++" y haga clic en instalar.


- [x] Clone el repositorio actual desde la linea de comandos (git clone "link")

```
git clone https://github.com/totoday72/AWG_DJANGO_PYTHON.git
```

- [x] Una vez clonado el repositorio, abra una ventana de linea de comandos y entre a la carpeta del proyecto,
Ejemplo:
```
Ingreso a la carpeta:
cd C:\django\awg-django\
```
- Cree el entorno de desarrollo ejecutando el siguiente comando:
```
python -m venv env
```
- Habilite el entorno virtual con el siguiente comando:

```
.\env\Scripts\activate
```

- Verifique que no exista ninguna dependencia instalada actualmente con el siguiente comando:
```
pip freeze
```

- Instale las dependencias para el proyecto con el siguiente comando:
```
pip install -r requirements.txt 
```

- Cree las migraciones de los modelos para poder actualizar la base de datos.
```
py.exe .\manage.py makemigrations
```
- Sincronizar la base de datos con los modelos del sistema.
```
py.exe .\manage.py migrate
```

- Ejecute el servidor Django con el siguiente comando:
```
py.exe .\manage.py runserver
```

- Presione Ctrl+C para cerrar el servidor de Django y escriba el siguiente comando para salir del ambiente de desarrollo:
```
deactivate
```

- [x] Configurar el ambiente de desarrollo:
El proyecto se puede ejecutar tanto con una terminal o linea de comandos asi como con una configuración del IDE de desarrollo.

# Linea de comandos o Terminal:

- Ejecute el servidor Django con el siguiente comando:
```
.\env\Scripts\activate
py.exe .\manage.py runserver
```

- Presione Ctrl+C para cerrar el servidor de Django y escriba el siguiente comando para salir del ambiente de desarrollo:
```
deactivate
```


Configuración Python en Pycharm:
```
Name: AWG DJango
Run: Proyect Default (env directory)
Domain: localhost
Port: 8000
Aditional Options: (Dejar Vacio)
Run Browser: http://localhost:8000
Workin Directory: C:\Django\AWG
path to .env directory:  (Dejar Vacio)
```

Después de las configuraciones anteriores ya estará listo el ambiente de desarrollo para NodeJS.

> [!IMPORTANT]
> La version de PYTHON utilizada en esta versión de software es la v.3.12

> [!WARNING]
> Antes de ejecutar verificar de tener instaladas las dependencias, puede revisar el archivo requirements.txt