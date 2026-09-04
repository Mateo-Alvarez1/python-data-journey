# Tipos Avanzados

Dentro de los tipos de datos que hemos visto hasta ahora, existen algunos que son más complejos y que nos permiten modelar estructuras de datos más sofisticadas. En esta sección, exploraremos algunos de estos tipos avanzados y cómo utilizarlos en nuestros programas.

## Listas

Las listas son un tipo de dato que permite almacenar datos de cualquier tipo. Son MUTABLES y DINAMICAS, lo cual es la principal diferencia con los sets y tuplas.
Se definen utilizando corchetes `[]` y los elementos se separan por comas. Las listas pueden contener elementos de diferentes tipos, incluyendo otras listas.

Sintaxis:

```python
mi_lista = [1, 2, 3, 4, 5]
```

Tambien podemos crealas listas utilizando la función `list()`:

```python
mi_lista = list((1, 2, 3, 4, 5))
```

Algunas Propiedades

- Son **ordenadas** , Mantienen el orden con el que se agregan los elementos.
- Pueden ser formadas por tipos **arbitrarios**
- Pueden ser **indexadas** con `[i]`, esto significa que podemos acceder a un elemento en particular de la lista utilizando su índice.
- Se pueden **anidar**, es decir meter una lista dentro de otra
- Son **Mutables**, ya que sus elementos pueden ser modificados después de su creación.
- Son **Dinamicas**, ya que se pueden añadir o eliminar elementos de la lista en cualquier momento.

## Acceder a elementos de una lista

Si tenemos una lista a con 3 elementos almacenados en ellas, podemos acceder a los mismos usando corchetes `[]`  y un indice, que va desde el `0` hasta el `n-1`, donde `n` es la cantidad de elementos en la lista.

```python
a = [90, "Python", 3.87]
print(a[0]) #90
print(a[1]) #Python
print(a[2]) #3.87
```

Tambien se puede acceder al ultimo elemento usando el indice `-1`, al penultimo con `-2` y asi sucesivamente.

```python
a = [90, "Python", 3.87]
print(a[-1]) #3.87
print(a[-2]) #Python
```

Y si queremos modificar un elemento de la lista, basta con asignar con el operador `=` a la posición que queremos modificar.

```python
a = [90, "Python", 3.87]
a[1] = "Java"
print(a) # [90, "Java", 3.87]
```

Un elemento puede ser eliminado con diferentes metodos como `del`, `remove()` o `pop()`

```python
a = [90, "Python", 3.87]
del a[1] # Elimina el elemento en la posición 1
a.remove(3.87) # Elimina el elemento 3.87
a.pop() # Elimina el ultimo elemento de la lista
```

También podemos tener listas anidadas, es decir, una lista dentro de otra. Incluso podemos tener una lista dentro de otra lista y a su vez dentro de otra lista. Para acceder a sus elementos sólo tenemos que usar [] tantas veces como niveles de anidado tengamos.

```python
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])    #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7
```

También es posible crear sublistas más pequeñas de una más grande. Para ello debemos de usar : entre corchetes, indicando a la izquierda el valor de inicio, y a la izquierda el valor final que no está incluido

```python
l = [1, 2, 3, 4, 5, 6]
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]
```

Y de la misma manera podemos modificar múltiples valores de la lista a la vez usando :.

```python
l = [1, 2, 3, 4, 5, 6]
l[0:3] = [0, 0, 0]
print(l) #[0, 0, 0, 4, 5, 6]
```

Y una funcionalidad muy interesante es que se puede asignar una lista con n elementos a n variables.Tambien llamada **desempaquetado de listas**

```python
l = [1, 2, 3]
x, y, z = l
print(x, y, z) #1 2 3
```

## Metodos De Listas

### append(obj)

El método append() añade un elemento al final de la lista.

```python
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]
```

### extend(iterable)

El método extend() añade múltiples elementos al final de la lista.

```python
l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]
```

### insert(index, obj)

El método insert() añade un elemento en una posición específica de la lista.

```python
l = [1, 2, 3]
l.insert(1, 1.5)
print(l) #[1, 1.5, 2, 3]
```

### remove((obj))

El método remove() elimina la primera aparición de un elemento en la lista.

```python
l = [1, 2, 3, 2]
l.remove(2)
print(l) #[1, 3, 2]
```

### pop(index=-1)

El método pop() elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último

```python
l = [1, 2, 3]
l.pop()
print(l) #[1, 2]
```

### reverse()

El método reverse() inverte el órden de la lista.

```python
l = [1, 2, 3]
l.reverse()
print(l) #[3, 2, 1]
```

### sort()

El método sort() ordena los elementos de menos a mayor por defecto.

```python
l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]
```

Tambien se puede ordenar de mayor a menor pasando el parametro `reverse=True`

```python
l = [3, 1, 2]
l.sort(reverse=True)
print(l) #[3, 2, 1]
```

### index(obj[,index])

El método index() recibe como parámetro un objeto y devuelve el índice de su primera aparición. Como hemos visto en otras ocasiones, el índice del primer elemento es el 0.

```python
l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals"))
```

## Tuplas

Las tuplas son un tipo o estructura de dato que permite almacenar datos de una manera muy parecida a las listas , con la salvedad de que son **inmutables**, es decir, una vez creada no se puede modificar. Esto significa que no podemos añadir, eliminar o cambiar elementos de una tupla después de su creación.

En lugar de inicializarce con corchetes `[]`, las tuplas se inicializan con paréntesis `()` y los elementos se separan por comas. Al igual que las listas, las tuplas pueden contener elementos de diferentes tipos, incluyendo otras tuplas.

```python
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
```

También pueden declararse sin (), separando por , todos sus elementos.

```python
tupla = 1, 2, 3
print(tupla) #(1, 2, 3)
```

## Operaciones con tuplas

Las tuplas tambien pueden ser anidadas al igual que las listas, y podemos acceder a sus elementos de la misma manera.

```python
tupla = (1, 2, (3, 4))
print(tupla[2][0]) #3
```

Tambien es posible convertir una lista en tuplas haciendo uso de la funcion `tuple()`

```python
mi_lista = [1, 2, 3]
mi_tupla = tuple(mi_lista)
print(mi_tupla) #(1, 2, 3)
```

Y se puede también asignar el valor de una tupla con n elementos a n variables.

```python
tupla = (1, 2, 3)
x, y, z = tupla
print(x, y, z) #1 2 3
```

Aunque tal vez no tenga mucho sentido a nivel práctico, es posible crear una tupla de un solo elemento. Para ello debes usar , antes del paréntesis, porque de lo contrario (2) sería interpretado como int.

```python
tupla = (2,)
print(tupla) #(2,)
print(type(tupla)) #<class 'tuple'>
```

## Metodos

### count(obj)

El método count() devuelve el número de veces que un elemento aparece en la tupla.

```python
tupla = (1, 2, 3, 2)
print(tupla.count(2)) #2
```

### index(obj,[,index])

El método index() devuelve el índice de la primera aparición de un elemento en la tupla.

```python
tupla = (1, 2, 3, 2)
print(tupla.index(2)) #1
```

También podemos pasarle un segundo parámetro que indica el índice desde el cual queremos buscar el elemento.

```python
tupla = (1, 2, 3, 2)
print(tupla.index(2, 2)) #3
```

## Diccionario

Los diccionarios en Python son un tipo de dato que permite almacenar pares de clave-valor. Son MUTABLES y DINAMICOS, lo cual es la principal diferencia con los sets y tuplas.
Se definen utilizando llaves `{}` y los elementos se separan por comas.

```python
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
```

Otra forma equivalente de crear diccionarios es usando la función `dict()`:

```python
d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])
print(d2)
#{'Nombre': 'Sara', 'Edad': '27', 'Documento': '1003882'}
```

## Algunas de las propiedades de los diccionarios son

- Son **Dinamicos**, ya que se pueden añadir o eliminar elementos en cualquier momento.
- Son **Indexados**, ya que podemos acceder a un elemento en particular del diccionario utilizando su clave.
- Y Son **Anidados**, es decir, podemos tener un diccionario dentro de otro diccionario.

## Acceder y modificar elementos

Se puede acceder a sus elementos con usar `[]` con el nombre del `key` y asignar el valor que queremos.

```python
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}  
d1["Edad"] = 28
print(d1) #{'Nombre': 'Sara', 'Edad': 28, 'Documento': 1003882}
```

Si el `key` al que accedimos no existe, se creará un nuevo par clave-valor en el diccionario.

```python
d1['Direccion'] = "Calle 123"
print(d1)
#{'Nombre': 'Laura', 'Edad': 27, 'Documento': 1003882, 'Direccion': 'Calle 123'}
```

## Diccionarios anidados

Se pueden crear diccionarios dentro de otros diccionarios, lo que permite modelar estructuras de datos más complejas.

```python
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}
```

## Metodos de diccionarios

### clear()

El método clear() elimina todo el contenido del diccionario.

```python
d = {"a": 1, "b": 2}
d.clear()
print(d) #{}
```

### get(key[, default])

El método get() devuelve el valor asociado a una clave específica. Si la clave no existe, devuelve un valor predeterminado (por defecto es None).

```python
d = {"a": 1, "b": 2}
print(d.get("a")) #1
print(d.get("c")) #None
print(d.get("c", "No encontrado")) #No encontrado
```

### items()

El método items() devuelve una vista de todos los pares clave-valor del diccionario.

```python
d = {"a": 1, "b": 2}
print(d.items()) #dict_items([('a', 1), ('b', 2)])
```

### keys()

El método **keys()** devuelve una vista de todas las claves del diccionario.

```python
d = {"a": 1, "b": 2}
print(d.keys()) #dict_keys(['a', 'b'])
```

### values()

El método **values()** devuelve una vista de todos los valores del diccionario.

```python
d = {"a": 1, "b": 2}    
print(d.values()) #dict_values([1, 2])
```

### pop(key[, default])

El método pop() elimina un par clave-valor del diccionario y devuelve el valor asociado a la clave. Si la clave no existe, devuelve un valor predeterminado (por defecto es None).

```python
d = {"a": 1, "b": 2}
print(d.pop("a")) #1
print(d) #{'b': 2}
```

### popitem()

El método popitem() elimina y devuelve un par clave-valor aleatorio del diccionario. Si el diccionario está vacío, genera un error.

```python
d = {"a": 1, "b": 2}
print(d.popitem()) #('b', 2)
```

### update([other])

El método update() actualiza el diccionario con los pares clave-valor de otro diccionario o iterable de pares clave-valor.

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1) #{'a': 1, 'b': 3, 'c': 4}
```

> Reemplaza los valores del diccionario original con los valores del diccionario pasado como argumento si las claves coinciden. Si la clave no existe en el diccionario original, se agrega un nuevo par clave-valor.

## Sets

Los Sets en Python son una estructura usada para almacenar elementos de una manera similar a las listas, pero con ciertas diferencias.

Los sets permiten almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias

- Los elementos de un set son **únicos**, es decir, no pueden repetirse.
- Los sets son **desordenados**, lo que significa que no mantienen un orden específico de los elementos.
- Sus elementos deben ser inmutables, es decir, no pueden ser modificados después de su creación. Por ejemplo, no se puede tener un set que contenga listas o diccionarios como elementos-

Para crear un set en python, se utilizan llaves `{}` o la función `set()`. Por ejemplo:

```python
s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>
```

### Opciones con Sets

A diferencia de las listas con set no podemos acceder a un elemento a traves de su indice . Si lo intentamos tendremos un , TypeError

```python
s = set([5, 6, 7, 8])
#s[0] = 3 #Error! TypeError
```

Los elementos de un set deben ser inmutables, por lo que un elemento de un set no puede ser ni un diccionario ni una lista. Si lo intentamos tendremos un TypeError

```python
lista = ["Perú", "Argentina"]
#s = set(["México", "España", lista]) #Error! TypeError
```

Con la funcion `len()` podemos saber la longitud total del `set`.Los duplicados son eliminados

```python
s = set([1, 2, 2, 3, 4])
print(len(s)) #4
```

Tambien podemos saber si un elemento esta presente en un set con el operador  `in`. Si el valor existe en el set se devolvera, `True`.

```python
s = set(["Guitarra", "Bajo"])
print("Guitarra" in s) #True
```

## Funcionalidades Sets

```python
primer = {1,1,2,2,3,4}
segundo = [3,4,5]
segundo = set(segundo)

print(primer | segundo ) # Operador de Union --> Crea otro set con la union de los dos  
print(primer & segundo) # Interseccion -> Crea otro set solo con los valores repetidos en cada uno
print(primer - segundo) # Diferencia -> Crea otro set con los del primero excluidos los que se encuetren en el otro set
print(primer ^ segundo) # Diferencia Simetrica --> Crea otro set con los elementos que estan en los dos sets pero no que estan en ambos
```

## Metodos Sets

### add(element)

El método add() permite añadir un elemento al `set`.

```python
l = set([1, 2])
l.add(3)
print(l) #{1, 2, 3}
```

### remove(element)

El método remove() elimina el elemento que se pasa como parámetro. Si no se encuentra, se lanza la excepción KeyError.

```python
s = set([1, 2])
s.remove(2)
print(s) #{1}
```

### discard(element)

El método discard() es muy parecido al remove(), borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada.

```python
s = set([1, 2])
s.discard(3)
print(s) #{1, 2}
```

### pop()

El método pop() elimina un elemento aleatorio del set.

```python
s = set([1, 2])
s.pop()
print(s) #{2}
```

### clear(-)

El método clear() elimina todos los elementos de set.

```python
s = set([1, 2])
s.clear()
print(s) #set()
```
