# App_shortener_URLs

## Descripcion

Aplicacion web acortador de URLs, utilizando python3 django3.2 y sqlite3 para la base de datos.

## Como instalar

  * Para ejecutar el proyecto localmente recomiendo instalar un entorno virtual:
`python3 -m venv <nombre_del_entorno>` luego `source <nombre_del_entorno>/bin/activate`
  * Luego dentro del entorno virtual ejecutar `pip install -r requeriments.txt`.

## Modulos y archivos:

  * `src/shortener/models.py` en este achivo se encuentra declarado el modelo de base de datos.
  * `src/kirr/settings.py` en este archivo se encuentra la configuracion del proyecto en cuanto a base de datos entornos 
y aplicaciones instaladas.
  * `src/kirr/urls.py` en este archivo se encuentran las URLs o rutas permitidas en la aplicacion.

## Ejecutar

  * En linux desde la carpeta `src/` ejecutar `python manage.py runserver`
  


