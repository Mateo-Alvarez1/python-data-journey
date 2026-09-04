# List Comprehensions

Las **List Comprehension** o comprension de listas  nos permiten **crear** listas de elementos en una sola linea de codigo.Por ejemplo podemos crear una lista con los cuadrados de los primeros 5 numeros de la siguiente forma.

```python
cuadrados = [i**2 for i in range(5)]
print(cuadrados) #[0, 1, 4, 9, 16]
```

Es lo mismo que hacer un for de la siguiente manera

```python
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
```

La sintaxis de una Comprension de Listas es la siguiente:

```python
# lista = [expresión for elemento in iterable]
```

> Es decir, por un lado tenemos el for elemento in iterable, que itera un determinado iterable y “almacena” cada uno de los elementos en elemento como vimos en este otro post sobre el for. Por otro lado, tenemos la expresión, que es lo que será añadido a la lista en cada iteración.

- Expresion -> Lo que va a ser *añadido* a la lista
- Elemento in iterable - Itera un determinado *iterable* y almacena cada uno de los *elementos*

```python
unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]
```

## Añadiendo condicionales

En la comprension de listas es posible agregar un condicional ``if`` para podes filtrar los elementos a guardar

La sintaxis es la siguiente:

```python
# lista = [expresión for elemento in iterable if condición]
````

```python
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']
```

> Lo que hace este codigo es iterar cada letra de la frase, y si es una `r` la agrega a la lista `erres`

## Set Comprehensions

Los *Set Comprehensions* son muy similares a las listas que hemos visto con anterioridad. La unica diferencia es que debemos cambiar el `()` por `{}`
Como resulta evidente, dado que los ``sets`` no pemriten duplicados, si intetamos añadir un elemento que ya existe, simplemente no se añadira

```python
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}
#{'r'}
```

## Dictionary Comprehensions

Y por último, también tenemos las *comprensiones de diccionarios*. Son muy similares a las anteriores, con la única diferencia que debemos especificar la *key* o llave. Veamos un ejemplo.

```python
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}
```

> Se puede ver, usando : asignamos un valor a una llave. Hemos usado también **zip()**, que **nos permite iterar dos listas paralelamente**. Por lo tanto, en este ejemplo estamos convirtiendo dos listas a un diccionario.
