# ILI_SVC_APP (Servicio de Validación Catastral)

Servicio para validar datos XTF

## Clonación de repositorio

```bash
git clone --recurse-submodules https://github.com/ceicol/ili_svc_app.git
```

## Creación entorno virtual

```bash
python3 -m venv .venv
```

## Activación entorno virtual

```bash
source .venv/bin/activate
```

## Instalación de dependencias

```bash
pip install -r ./requirements.txt
```

## Instalación de dependencias externas

```bash
pip install -r ./ili_svc_app/submodules/requirements.txt
```

## Creación de archivo .env

Crear un archivo .env con las mismas varibales que estan definidas en el archivo de ejemplo .env.example

```bash
DB_SCHEMA=id_schema_in_db

# Actualizar según corresponda.
ILISERVICES_DB_NAME=iliservices
ILISERVICES_DB_USER=postgres
ILISERVICES_DB_PASS=admin
ILISERVICES_DB_PORT=5432
ILISERVICES_DB_HOST=localhost
```

## Levantar servicio local

Ubicarse en la ruta princial y ejecutar lo siguiente:

```bash
python manage.py migrate
python manage.py runserver
```

El servicio se levantara por defecto en http://127.0.0.1:8000/

## Uso

La API cuenta con las siguientes rutas:

#### 1. Obtener archivo XTF [GET]

```
http://127.0.0.1:8000/api/get_file/<reemplazar_por_id_basket>/
```

#### 2. Actualizar datos en db según XTF [POST]

Recibe un archivo adjunto de tipo .xtf

```
http://127.0.0.1:8000/api/upload_file/
```

Ejemplo en formulario html

- Importante la key name del input en el front debera ser nombrada con "file":

```html
<form method="post" enctype="multipart/form-data">
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="file" name="file" accept=".xtf, .XTF" />
  </div>
  <div>
    <button type="submit">Submit</button>
  </div>
</form>
```

## Desarrolladores

Este proyecto depende de submodulos, por lo tanto si estas trabajando en modo local deberas ejecutar los siguientes comandos para iniciar los submodulos y descargar las ultimas actualizaciones de las dependencias.

```bash
git submodule init
git submodule update --remote --recursive
```
