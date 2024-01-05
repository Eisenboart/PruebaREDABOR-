# Proyecto de Automatización con Selenium y Python

Este proyecto contiene scripts de automatización para pruebas utilizando Selenium y Python.

## Configuración

### Requisitos Previos

- [VSCode](https://code.visualstudio.com/) instalado
- [Python 3.x](https://www.python.org/) instalado
- [PIP](https://pip.pypa.io/en/stable/installation/) instalado
- [GeckoDriver 0.33](https://github.com/mozilla/geckodriver/releases) ya esta descargado y agregado al proyecto

### Configuración del Proyecto

1. Descarga o clona este repositorio.

2. Abre el proyecto en VSCode.

3. Crea un entorno virtual (opcional pero recomendado):

   Paso a paso en windows:
   -Abre un terminal (powershell) como administrador
   -Ejecuta los siguientes comandos:
        -python -m venv venv
        -Set-ExecutionPolicy RemoteSigned -Scope Process
        - .\venv\Scripts\Activate
   -Instala las dependencias:
        -pip install Selenium
        -(en caso de 2 o mas dependecias) pip install -r requirements.txt


## Estructura del Proyecto PruebaRedabor:

Este proyecto está organizado en una estructura de carpetas y archivos destinados a realizar pruebas automatizadas en un sitio web específico. Aquí hay una descripción general de cada elemento:

    geckodriver.exe:
        Descripción: Este archivo ejecutable es el controlador (driver) específico para el navegador Firefox. La versión proporcionada es 0.33.0.

    LocatorsNCommon: Carpeta contenedora.

        Descripción: Esta carpeta contiene archivos relacionados con la localización de elementos en la interfaz de usuario (locators) y funcionalidades comunes necesarias para las pruebas.

        init.py: Descripción: Este archivo indica que el directorio LocatorsNCommon debe ser considerado como un paquete de Python.

        common.py: Descripción: Archivo que contiene funciones comunes utilizadas en varias partes del proyecto para interactuar con elementos de la interfaz de usuario.

        locator.py: Descripción: Archivo que define la clase PageLocatorsClass, la cual contiene identificadores (locators) para elementos específicos en las páginas web.

    Page: Carpeta contenedora.

        Descripción: Esta carpeta contiene módulos individuales que representan diferentes páginas web del sitio bajo prueba.

        init.py:
            Descripción: Este archivo indica que el directorio Page debe ser considerado como un paquete de Python.

        modulo_001.py:
            Descripción: Módulo que representa y contiene funciones para interactuar con la página de aterrizaje común.

        modulo_002.py:
            Descripción: Módulo que representa y contiene funciones para interactuar con la página de aterrizaje en Colombia.

        modulo_003.py: Descripción: Módulo que representa y contiene funciones para interactuar con la página de búsqueda de empleos y filtros.

        modulo_004.py: Descripción: Módulo que representa y contiene funciones para interactuar con la página de creación de cuenta.

    Test: Carpeta contenedora.

        Descripción: Esta carpeta contiene los scripts de prueba que utilizan los módulos de la carpeta Page para realizar pruebas automatizadas.

        init.py: Descripción: Este archivo indica que el directorio Test debe ser considerado como un paquete de Python.

        prueba_red-abor.py: Descripción: Script principal de prueba que utiliza las clases y funciones definidas en los módulos de la carpeta Page para ejecutar una serie de pruebas automatizadas en el sitio web.

## Ejecutar Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

    Navega al directorio donde fue descargado el proyecto:
        -cd:"(tudirectorio)/PruebaREDABOR"
        -ejecuta el siguiente comando:
        -python -m unittest Test.prueba_red_abor

## Contacto
Para preguntas o comentarios, contacta a Rodrigo Eisenboart <rodeisen@gmail.com>
