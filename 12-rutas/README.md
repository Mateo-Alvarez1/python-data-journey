# Rutas con ``Pathlib``

pathlib es el modulo estandar de python para trabajar con rutas de archivos de forma orientada a objetos, en vez de manipular strings a mano (como se hacia antes con ``os.path``). Funciona igual en windows, linux y Mac, adaptando el separador de rutas automaticamente

## Crear rutas

```python
from pathlib import Path

Path(r"C:\Archivos de programa\cs")  # ruta absoluta en Windows (con raw string por las barras invertidas)
Path("/usr/bin")                      # ruta absoluta en Linux/Mac
Path()                                 # ruta al directorio actual
Path.home()                            # ruta a la carpeta del usuario (ej: /home/usuario o C:\Users\usuario)
Path("one/__init__.py")               # ruta relativa
```

> Nota: en Windows conviene usar r"..." (raw string) para evitar que \ se interprete como carácter de escape.

## Verificar el tipo de ruta

```python
path = Path("Python/mi-archivo.py")

path.is_file()   # True si la ruta apunta a un archivo existente
path.is_dir()    # True si la ruta apunta a un directorio existente
path.exists()    # True si la ruta existe, sea archivo o directorio
```

## Propiedades de una ruta

```python
print(
    path.name,      # nombre completo del archivo: "mi-archivo.py"
    path.stem,      # nombre sin extensión: "mi-archivo"
    path.suffix,    # extensión: ".py"
    path.parent,    # carpeta contenedora: "Python"
    path.absolute() # ruta absoluta completa desde la raíz del sistema
)
```

## Modificar partes de una ruta (sin mutar la original)

``with_name``, ``with_suffix`` y ``with_stem`` devuelven una ruta nueva — no modifican el archivo en disco ni la variable original.

```python
p = path.with_name('hola.exe')   # reemplaza el nombre completo → "Python/hola.exe"
print(p)

p = path.with_suffix('.py')      # reemplaza solo la extensión
print(p)

p = path.with_stem('chau')       # reemplaza solo el nombre, conserva la extensión → "Python/chau.py"
print(p)
```

## Directorios

```python
path = Path("rutas")

path.exists()             # verifica si el directorio existe
path.mkdir()               # crea el directorio (falla si ya existe, salvo exist_ok=True)
path.rmdir()                # elimina el directorio (solo si está vacío)
path.rename("directorio-1") # renombra el directorio
```

## Listar contenido de un directorio

```python
# Todos los elementos que NO son subdirectorios (o sea, archivos)
archivos = [p for p in path.iterdir() if not p.is_dir()]

# Filtrar por patrón: todos los .py que empiezan con "01-"
archivos = [p for p in path.glob("01-*.py")]

print(archivos)
```

- ``iterdir()`` lista todo el contenido directo del directorio (sin filtrar por patrón).
- ``glob(patrón)`` filtra usando comodines (*, ?, ** para búsqueda recursiva).

## Inyeccion de dependencias

La inyeccion de dependencias es un principio de diseño: en vez de que una funcion u objeto cree o importe directamente lo que necesita para funcionar, se lo recibe como parametro desde afuera. Esto reduce el acoplamiento y facilita testear el codigo

### Sin inyección de dependencias (acoplado)

```python
import usuario

def guardar():
    usuario.guardar()
```

Acá ``guardar()`` depende directamente del módulo ``usuario``. Problemas de este enfoque:

- No se puede reutilizar la función con otra entidad distinta a ``usuario`` sin reescribirla.
- Para testear ``guardar()`` de forma aislada, hay que testear también usuario (o simular/mockear el módulo entero).

### Con inyección de dependencias (desacoplado)

```python
def guardar(entidad):
    entidad.guardar()
```

Acá ``guardar()`` no sabe ni le importa qué es ``entidad`` concretamente — solo espera que tenga un método .guardar(). Esto permite:

- Reutilizar la misma función con cualquier objeto que cumpla ese "contrato" (duck typing).
- Testear pasando un objeto simulado (mock) sin depender del módulo real.

```python
guardar(usuario)   # funciona si usuario tiene método .guardar()
guardar(producto)  # funciona igual con cualquier otra entidad compatible
```
