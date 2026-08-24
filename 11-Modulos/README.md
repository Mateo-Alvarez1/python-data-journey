# Modulos & Paquetes

## Modulos

Un **Módulo** es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.

Consideremos por ejemplo, un archivo `aritmetica.py` que contenga estas definiciones:

```python
  def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a /   
```

Podemos acceder a ellas desde otro archivo de python ubicado en la misma ruta *importando* el modulo

```python
import aritmetica

print(aritmetica.sumar(7, 5))
```

Una Forma alternativa puede ser

```python
from aritmetica import sumar

print(sumar(7, 5))
```

Nótese que, en este segundo caso, no se prefija el nombre del módulo al invocar al objeto importado. Podemos importar varios objetos separándolos por comas.

```python
from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))
```

## Paquetes

Un **Paquete** es una carpeta que contiene varios modulos.Siguiendo el ejemplo anterior, podemos diseñar un paquete *matematica* creando una carpeta con la siguiente estructura.

```python
matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py
```

Debe contener siempre un archivo ``__init__``.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.

```python
import matematica.aritmetica

print(matematica.aritmetica.sumar(7, 5))
```

O de esta manera

```python
from matematica.aritmetica import sumar

print(sumar(7, 5))
```

## Imports condicionados

Son imports que se ejecutan solo si se cumple una condición, en vez de hacerse siempre al principio del archivo de forma incondicional.

```python

if __name__ != "__main__":
    from matematica.aritmetica import suma
    from matematica.aritmetica import resta

    print(__name__)
if __name__ == "__main__"_
print('Haciendo otras operaciones')
```
