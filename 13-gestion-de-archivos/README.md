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
