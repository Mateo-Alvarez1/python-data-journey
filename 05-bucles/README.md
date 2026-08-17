# Bucles

## While

El While nos permite **ejecutar una seccion de codigo repetidas veces**. El codigo se ejecutara **mientras** una condicion determinada se cumpla. Cuando deje de cumplir se saldra del bucle y se continuara la ejecucion normal.

```python
x = 5
while x > 0:
    x -=1
    print(x)

# Salida: 4,3,2,1,0
```

el bucle `while` tiene dos partes:

- La **condicion** que se tiene que cumplir para que se ejecute el codigo
- El bloque de codigo que se ejecutara mientras la condicion se cumpla

Es posible tener un ``while`` en una sola línea, algo muy útil si el bloque que queremos ejecutar es corto. En el caso de tener mas de una sentencia, las debemos separar con ``;``.

```python
x = 5
while x > 0: x-=1; print(x)
```

En este caso tenemos una lista que mientras no este vacía, vamos eliminando su primer elemento.

```python
x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)
#['Dos', 'Tres']
#['Tres']
#[]
```

## While Anidado

Es algo que resulta especialmente útil si por ejemplo queremos generar permutaciones de números, es decir, si queremos generar todas las combinaciones posibles.

```python
# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0
```

## Ejemplos While

Árbol de navidad en Python. Imprime un árbol de navidad formado con ``*`` haciendo uso del ``while`` y de la multiplicación de un entero por una cadena, cuyo resultado en Python es replicar la cadena.

```python
z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1
#      *     
#     ***    
#    *****   
#   *******  
#  *********
# ***********
```

> Sucesión de Fibonacci en Python. En matemáticas, la sucesión de fibonacci es una sucesión infinita de números naturales, donde el siguiente es calculado sumando los dos anteriores.

```python
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b
#1, 1, 2, 3, 5, 8, 13, 21
```

## Bucle For

El for es un tipo de bucle, parecido al `while` pero con ciertas diferencias. La principal es que el numero de iteraciones **esta definido** de antemano, que en un `while` no.

Mientras que en el while la condicion era evaluada en cada iteracion para decidir si volver a ejecutar el codigo o no, en el for no exite tal condicion, sino un `iterable` que define las veces que se ejecutara el codigo.

```python
for i in range(0, 5):
print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
```

> Si queremos tener un numero que va creciendo de 0 a n, hacerlo con un for nos ahorra alguna linea de codigo. por que no tenemos que escribir codigo para incremetar el numero.

Podemos hasta iterar un String

```python
for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n
```

## Iterables e Iteradores

- Los `iterables` son aquellos objetos que como su nombre indica pueden ser iterados, es decir pueden ser `indexados`
- Los `iteradores` son objetos que hacen referencia a un elemento, y que tienen un metodo `next` que permite hacer referencia al siguiente

Lo primero que tenemos que sabes es que despues de `for` va en `in` **(debe ser siempre un iterable)**

```python
#for <variable> in <iterable>:
#    <Código>
```

> Para saber si un elemento es iterable o no podemos usar `IsInstance()`

```python
from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False
```

## For Anidados

Es Posible **meter un for dentro de otro**. Esto puede ser muy util si queremos iterar algun objeto que en cada elemento, tiene a su vez otra clase iterable.Podemos tener por ejemplo una lista de listas

```python
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
```

Si iteramos usando un solo `for` estaremos **accediendo a la segunda lista** pero no estaremos **accediendo a sus elementos**.

```python
for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]
```

Para poder acceder a los elementos debemos `anidar` dos `for`. Uno va a iterar **columnas** y otro va a iterar **filas**

```python
for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3
```

## Range

El `range()` genera una secuencia de numeros que van del **0 (por defecto)** hasta el numero que se passa como parametro **menos 1**. Se pueden pasar hasta **3 parametros**

- Primer parametro: Inicio de la secuencia
- Segundo parametro: El Final
- Tercer parametro: Salto que se desea entre numeros

```python
#range(inicio, fin, salto)
```

Por lo tanto, si llamamos a ``range()`` con ``(5,20,2)``, se generarán números de 5 a 20 de dos en dos. Un truco es que el ``range()`` se puede convertir en `list`

```python
print(list(range(5, 20, 2)))
```

## Break & Continue

La sentencia ``break`` nos permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle.
Esto significa que una vez se encuentra la palabra ``break``, el bucle se habrá terminado.

El uso de ``continue`` al igual que el ya visto `break`, nos permite modificar el comportamiento de de los bucles while y for.

Concretamente, ``continue`` se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.

La diferencia entre el `break` y ``continue`` es que el ``continue`` no rompe el bucle, si no que pasa a la siguiente iteración saltando el **código pendiente**.
