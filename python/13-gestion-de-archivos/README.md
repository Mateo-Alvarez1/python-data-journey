# Archivos

## Metadatos de un archivo (stat)

``Path.stat()`` devuelve un objeto`` os.stat_result ``con información del sistema de archivos sobre un archivo: cuándo se accedió, se creó o se modificó por última vez. Esos valores vienen como timestamp Unix (un número), por eso se combinan con ``ctime()`` para volverlos legibles.

```python
from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")

print("acceso", ctime(archivo.stat().st_atime))       # último acceso de lectura
print("creacion", ctime(archivo.stat().st_ctime))      # en Windows: fecha de creación / en Linux: cambio de metadatos
print("modificacion", ctime(archivo.stat().st_mtime))  # última vez que se editó el contenido
```

> Nota: st_ctime significa cosas distintas según el sistema operativo. En Windows es la fecha de creación del archivo. En Linux/Mac es la fecha del último cambio de metadatos (permisos, nombre, etc.), no de creación — Linux no guarda la fecha de creación real en la mayoría de los sistemas de archivos.

## Leer y escribir archivos de texto (.txt)

``read_text()`` y ``write_text()`` son atajos de ``pathlib`` que evitan tener que usar ``open()`` + ``with`` a mano para casos simples: abren el archivo, hacen la operación y lo cierran solos.

```python
from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")  # lee todo el contenido y lo separa en una lista, una línea por elemento
texto.insert(0, "hola mundo")                    # insertamos una línea nueva al principio de la lista
archivo.write_text("\n".join(texto), "utf-8")    # unimos la lista de nuevo en un solo string y sobreescribimos el archivo

print(texto)
```

Por qué se separa con ``.split("\n")`` antes de insertar: ``write_text()`` sobreescribe todo el archivo, no agrega contenido al final. Si insertáramos el texto nuevo directo sobre el string completo, perderíamos el control de en qué línea exacta queda insertado. Separando por líneas primero, podemos insertar en la posición que queramos (acá, al principio con ``insert(0, ...)``) y después reconstruir el archivo completo con ``"\n".join(...)``.

> Cuidado: como ``write_text()`` sobreescribe el archivo entero, si el proceso se corta a mitad de camino (por ejemplo, el programa se cierra entre el ``read_text`` y el ``write_text``) se puede perder el contenido original. Para archivos importantes, conviene el patrón de "archivo temporal + rename" que usamos más abajo con el CSV.`

## Trabajar con archivos CSV

### Escribir un CSV

```python
import csv

with open("archivos/archivo.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Id", "userid", "text"])
    writer.writerow([100, 1, "tweet"])
    writer.writerow([101, 2, "teewt1"])
```

> ``newline=""`` es obligatorio en Windows al usar el módulo ``csv``. Sin este parámetro, Windows duplica los saltos de línea (``\r\n`` se convierte en ``\r\r\n``), generando una línea en blanco de más entre cada fila. Es la recomendación oficial de la documentación de Python para cualquier ``open()`` combinado con ``csv.reader/csv.writer``, tanto para lectura como para escritura.

### Leer un CSV

```python
with open("archivos/archivo.csv", "r", newline="") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
```

## Actualizar un CSV (patrón: archivo temporal + reemplazo)

Un CSV no se puede "editar una línea en el medio" directamente — hay que reescribirlo completo. El patrón estándar es: leer el original, escribir una copia modificada en un archivo temporal, y al final reemplazar el original por el temporal.

```python
import csv
import os

with open("archivos/archivo.csv", "r", newline="") as r, open("archivos/archivo_temp.csv", "w", newline="") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if not linea:                 # saltear líneas vacías (evita IndexError en linea[0])
            continue
        if linea[0] == "100":
            writer.writerow([100, 1, "texto modificado"])
        else:
            writer.writerow(linea)

# fuera del `with`: los archivos ya están cerrados, recién ahí se puede borrar/renombrar
os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
```

Dos detalles importantes de este patrón, aprendidos a los golpes:

- ``if not linea: continue`` — si el CSV tiene una línea vacía (común si se escribió sin newline="" en algún momento anterior), csv.reader la devuelve como lista vacía [], y linea[0] explota con IndexError: list index out of range. Este chequeo lo evita.

-``os.remove() y os.rename() van FUERA del bloque with.`` Mientras el ``with`` sigue abierto, el archivo original está en uso por el proceso — Windows no permite borrar ni renombrar un archivo que sigue abierto ``(PermissionError: [WinError 32])``. Recién al salir del with, Python cierra los archivos automáticamente y ahí se puede operar sobre ellos sin problema.

## Leer JSON

JSON (JavaScript Object Notation) es un formato de texto para representar datos estructurados — es el formato más usado para intercambiar información entre sistemas (APIs, archivos de configuración, etc.). En Python se trabaja con el módulo estándar ``json``, y la clave para entenderlo es un solo concepto: convertir entre objetos de Python y texto plano, en los dos sentidos.

### Escribir JSON

Para escribir JSON en Python debemos primero ``serializar`` el objeto (lista, diccionario, etc) en un ``string`` con formato JSON, para poder guardarlo en un archivo o enviarlo por una red

```python
import json
from pathlib import Path

productos = [
    {"id": 1, "nombre": "Surfboard"},
    {"id": 2, "nombre": "Snowboard"},
    {"id": 3, "nombre": "Skateboard"},
]

data = json.dumps(productos)  # convierte la lista de diccionarios en un string JSON
Path("archivos/productos.json").write_text(data)
```

``json.dumps()``(dump string) toma ``productos`` —una lista de diccionarios, una estructura 100% de Python— y devuelve un string con ese mismo contenido pero en formato JSON:

```python
data = '[{"id": 1, "nombre": "Surfboard"}, {"id": 2, "nombre": "Snowboard"}, {"id": 3, "nombre": "Skateboard"}]'
```

Ese string es lo que se escribe en el archivo con ``write_text()``.

> Nota: acá conviene sumar ``encoding="utf-8"`` en el ``write_text()`` (no está en el código original), para que nombres con tildes o "ñ" se guarden correctamente, igual que se hace en el ``read_text()`` de más abajo.

### Leer Json

Para leer JSON en Python debemos ``deserializar``, es decir, hacer el **proceso inverso**. Transformar el JSON a un Objeto Python

```python
data = Path("archivos/productos.json").read_text(encoding="utf-8")  # lee el archivo como texto plano
productos = json.loads(data)  # convierte el string JSON en una lista de diccionarios de Python
```

``json.loads()`` (load string) hace lo opuesto a ``dumps()``: recibe un string y devuelve la estructura de Python equivalente. Después de esta línea, ``productos`` vuelve a ser una lista de diccionarios normal — se puede indexar, iterar, modificar como cualquier lista de Python.

### Modificar datos y volver a guardar

Como productos ya es una lista de diccionarios de Python normal después del ``loads()``, se modifica con la sintaxis habitual:

```python
productos[0]["nombre"] = "Chancho"  # accede al primer diccionario y cambia su clave "nombre"
Path("archivos/productos.json").write_text(json.dumps(productos))
print(productos)
```

**El flujo completo, en resumen:** ``dumps()`` → Python a texto (para guardar). ``loads()`` → texto a Python (para trabajar). No hay forma de modificar el JSON "directamente" en el archivo — siempre hay que leerlo y deserializarlo a Python primero, modificar el objeto en memoria, y volver a serializarlo para guardar los cambios.

> Truco para recordar la diferencia: la versión con "s" al final (dumps, loads) trabaja con strings. La versión sin "s" (dump, load) trabaja directo con archivos. El código que estuviste viendo usa la versión con "s" porque combina json con pathlib (read_text/write_text), en vez de usar open() directamente.
