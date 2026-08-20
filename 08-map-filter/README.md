# Map / Filter / Reduce

## Map

La funcion ``map`` toma dos entradas:

- Una lista o iterable que sera modificado en una nueva
- Una funcion, que sera aplicada a cada uno de los elementos de la lista o iterable anterior

Nos devuelve una nueva lista donde todos y cada uno de los elementos de la lista original han sido pasados por la condicion

```python
map(funcion_a_aplicar, entrada_iterable)
```

## Ejemplo usando Lambda

```python
lista = [1, 2, 3, 4, 5]
lista_pordos = list(map(lambda x: 2*x, lista))
print(lista_pordos) # [2, 4, 6, 8, 10]
```

## Filter

La funcion `filter` tambien recibe una funcion y una lista pero *el resultado es la lista inicial filtrada*.Es decir se pasa cada elemento de la lista por la funcion y solo si su resultado es `true`, se incluye en la nueva lista

```python
filter(funcion_filtrar, entrada_iterable)
```

Al igual que hacíamos antes, usamos las funciones lambda que nos permiten declarar y asignar una función en la misma línea de código. En el siguiente ejemplo filtramos los números pares.

```python
lista = [7, 4, 16, 3, 8]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)
```

## Reduce

El `reduce` lo vamos a utilizar para **reducir todos los elementos de la entrada a un unico valor** aplicando un criterio determinado.Por ejemplo podemos sumar todos los elementos de una lista de la siguiente manera.

```python
from functools import reduce
lista = [1, 2, 3, 4, 5]
suma = reduce(lambda acc, val: acc + val, lista)
print(suma) # 15
```

Es importante tener en cuenta que la funcion recibe dos valores:

- El **Acumulador** que es el valor devuelto de la iteracion anterior, va acumulando un resultado hasta que lleguemos al final
- El **Valor** es cada uno de los elementos de nuestra lista, que en nuestro caso vamos añadiendo al acumulador

> El uso de reduce es especialmente útil cuando tenemos por ejemplo una lista de diccionarios y queremos sumar todos los valores de un campo en concreto. Veamos un ejemplo donde calculamos la edad media de varias personas.

```python
from functools import reduce
personas = [
    {'Nombre': 'Alicia', 'Edad': 22},
    {'Nombre': 'Bob', 'Edad': 29},
    {'Nombre': 'Charlie', 'Edad': 33}
]
suma_edad = reduce(lambda total, p: total + p['Edad'], personas, 0)
print(suma_edad/len(personas)) # 28.0
```

## Ejemplos Programacion Funcional

```python
   from functools import reduce
personas = [
    {'Nombre': 'Alicia', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'},
]

hombres = list(filter(lambda x: x['Sexo'] == 'M', personas))
suma_edades = reduce(lambda suma, p: suma + p['Edad'], hombres, 0)
media_edad = suma_edades/(len(hombres))
print(media_edad) # 33.0 
```

> Tal vez no muy legible, pero todo lo anterior se podrá expresar en una única línea de código.

```python
media_edades = reduce(lambda suma, p: suma + p['Edad'], filter(lambda x: x['Sexo'] == 'M', personas), 0) / len(list(filter(lambda x: x['Sexo'] == 'M', personas)))
print(media_edades) # 33.0
```
