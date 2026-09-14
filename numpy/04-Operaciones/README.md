# Operaciones sobre Arrays

En esta seccion vemos las distintas operaciones que se pueden realizar sobre los `ndarray`: operaciones logicas (filtrado y condiciones), operaciones de conjunto, ordenacion, conteo de valores, operaciones aritmeticas, operaciones unarias y la vectorizacion de funciones propias.

## Operaciones logicas

### Indexado booleano

El indexado booleano permite saber, elemento a elemento, si un array cumple o no una determinada condicion. El resultado es un array de `True`/`False` con la misma forma que el original.

```python
>>> values = np.array([[73, 86, 90, 20],
...                     [96, 55, 15, 48],
...                     [38, 63, 96, 95],
...                     [13, 87, 32, 96]])

>>> values > 50
array([[ True,  True,  True, False],
       [ True,  True, False, False],
       [False,  True,  True,  True],
       [False,  True, False,  True]])
```

Lo interesante es que podemos usar ese array booleano para **filtrar** directamente los elementos que cumplen la condicion:

```python
>>> values[values > 50]
array([73, 86, 90, 96, 55, 63, 96, 95, 87, 96])
```

Tambien sirve para **modificar** solo los elementos que cumplen la condicion:

```python
>>> values[values > 50] = -1
>>> values
array([[-1, -1, -1, 20],
       [-1, -1, 15, 48],
       [38, -1, -1, -1],
       [13, -1, 32, -1]])
```

> Se pueden combinar varias condiciones con los operadores `&` (and) y `|` (or), siempre entre parentesis: `(values < 25) & (values > 0)`.

### Comparando arrays y `np.where()`

Cuando lo que nos interesa no es el valor sino la **posicion** de los elementos que cumplen una condicion, usamos `np.where()`. Devuelve una tupla con los indices (uno por cada dimension):

```python
>>> idx = np.where(values > 50)
>>> idx
(array([0, 1, 1, 2, 3, 3]), array([0, 1, 3, 0, 1, 3]))

>>> values[idx]
array([73, 86, 96, 63, 87, 96])
```

## Operaciones de conjunto

NumPy tambien permite tratar los arrays como si fueran **conjuntos** matematicos, aplicando union, interseccion y diferencia.

```python
>>> x = np.array([9, 4, 11, 3, 14, 5, 13, 12, 7])
>>> y = np.array([17, 9, 19, 4, 18, 7, 13, 11, 10])
```

### Union

```python
>>> np.union1d(x, y)
array([ 3,  4,  5,  7,  9, 10, 11, 12, 13, 14, 17, 18, 19])
```

### Interseccion

```python
>>> np.intersect1d(x, y)
array([ 4,  7,  9, 11, 13])
```

### Diferencia

```python
>>> np.setdiff1d(x, y)
array([ 3,  5, 12, 14])
```

## Ordenacion de arrays

Al igual que con otras estructuras de Python, hay dos formas de ordenar: una **no destructiva** (devuelve un array nuevo, ordenado) y otra **destructiva** (ordena "in-situ", modificando el array original).

```python
>>> values = np.array([23, 24, 92, 88, 75, 68, 12, 91, 94, 24, 9, 21, 42, 3, 66])

>>> np.sort(values)          # No destructiva: devuelve una copia ordenada
array([ 3,  9, 12, 21, 23, 24, 24, 42, 66, 68, 75, 88, 91, 92, 94])

>>> values                    # El original no cambia
array([23, 24, 92, 88, 75, 68, 12, 91, 94, 24,  9, 21, 42,  3, 66])

>>> values.sort()             # Destructiva: modifica el array original
>>> values
array([ 3,  9, 12, 21, 23, 24, 24, 42, 66, 68, 75, 88, 91, 92, 94])
```

En arrays multidimensionales se puede indicar el eje (`axis`) sobre el que se quiere ordenar.

## Contando valores

Para saber que valores distintos hay en un array (y opcionalmente cuantas veces aparece cada uno) usamos `np.unique()`:

```python
>>> values = np.random.randint(1, 11, size=1000)

>>> np.unique(values)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

Si ademas queremos la frecuencia de cada valor, usamos el parametro `return_counts=True`:

```python
>>> valores, frecuencias = np.unique(values, return_counts=True)
>>> dict(zip(valores, frecuencias))
{1: 98, 2: 104, 3: 97, 4: 101, 5: 99, 6: 103, 7: 96, 8: 102, 9: 100, 10: 100}
```

Tambien existe `np.count_nonzero()` para contar cuantos elementos son distintos de cero (o cuantos cumplen una condicion, ya que las condiciones internamente son booleanas y `True` equivale a `1`):

```python
>>> np.count_nonzero(values)
1000
>>> np.count_nonzero(values > 5)
498
```

## Operaciones aritmeticas

Una de las grandes ventajas de NumPy es poder operar con arrays completos como si fueran "numeros simples", aprovechando la **aritmetica vectorial**: las operaciones se aplican elemento a elemento.

### Arrays con la misma dimension

```python
>>> m1 = np.array([[21, 86, 45], [31, 36, 78], [31, 64, 70]])
>>> m2 = np.array([[58, 67, 17], [99, 53, 9], [92, 42, 75]])

>>> m1 + m2
array([[ 79, 153,  62],
       [130,  89,  87],
       [123, 106, 145]])

>>> m1 - m2
array([[-37,  19,  28],
       [-68, -17,  69],
       [-61,  22,  -5]])

>>> m1 * m2       # multiplicacion elemento a elemento (NO es producto matricial)
array([[1218, 5762,  765],
       [3069, 1908,  702],
       [2852, 2688, 5250]])

>>> m1 / m2
array([[0.36206897, 1.28358209, 2.64705882],
       [0.31313131, 0.67924528, 8.66666667],
       [0.33695652, 1.52380952, 0.93333333]])

>>> m1 // m2      # division entera
array([[0, 1, 2],
       [0, 0, 8],
       [0, 1, 0]])
```

### Arrays y escalares (broadcasting)

Cuando operamos un array con un escalar, NumPy "expande" el escalar para aplicarlo a todos los elementos:

```python
>>> m1 + 10
array([[31, 96, 55],
       [41, 46, 88],
       [41, 74, 80]])

>>> m1 * 2
array([[ 42, 172,  90],
       [ 62,  72, 156],
       [ 62, 128, 140]])
```

> Esto se conoce como **broadcasting**: NumPy compara las formas de ambos operandos y, cuando es posible, "estira" el mas pequeño para que encajen. Con arrays de distinta dimension aplica las mismas reglas, siempre que las dimensiones sean compatibles.

## Operaciones unarias

Son operaciones que se aplican sobre un unico array.

### Funciones universales (ufunc)

Las funciones universales operan **elemento a elemento** sobre uno (o dos) arrays. NumPy trae un monton de ellas ya definidas:

```python
>>> values = np.array([[48.32, 24.89, 77.49],
...                     [77.81, 22.54, 65.11],
...                     [ 5.54, 59.06, 62.52]])

>>> np.sqrt(values)
array([[6.95138287, 4.98964037, 8.80325181],
       [8.82149318, 4.74768522, 8.06925179],
       [2.35575992, 7.68551905, 7.9074757 ]])

>>> np.ceil(values)
array([[49., 25., 78.],
       [78., 23., 66.],
       [ 6., 60., 63.]])

>>> np.floor(values)
array([[48., 24., 77.],
       [77., 22., 65.],
       [ 5., 59., 62.]])

>>> np.log(values)
array([[3.87788123, 3.21472768, 4.35024235],
       [4.3543823 , 3.11531435, 4.17612153],
       [1.71372672, 4.07867583, 4.13561721]])
```

### Funciones estadisticas, maximos y minimos

```python
>>> values.sum()          # Suma de todos los elementos
443.28
>>> values.mean()         # Media
49.25...
>>> values.std()          # Desviacion tipica
21.9...
>>> values.max()          # Maximo
77.81
>>> values.min()          # Minimo
5.54
>>> values.argmax()       # Indice (aplanado) del maximo
3
>>> values.argmin()       # Indice (aplanado) del minimo
6
```

> La mayoria de estas funciones aceptan el parametro `axis` para reducir por filas (`axis=1`) o por columnas (`axis=0`) en lugar de sobre todo el array.

## Vectorizando funciones

Cuando necesitamos aplicar una logica propia (no cubierta por las funciones de NumPy) a cada elemento de un array, lo ideal es **vectorizarla** para no perder rendimiento con bucles clasicos.

Supongamos que queremos aplicar esta logica entre dos matrices `A` y `B`:

- Si `A[i,j] > B[i,j]` -> `A[i,j] + B[i,j]`
- Si `A[i,j] < B[i,j]` -> `A[i,j] - B[i,j]`
- Si son iguales -> `0`

```python
def customf(a, b):
    if a > b:
        return a + b
    elif a < b:
        return a - b
    else:
        return 0
```

Con bucles anidados esto es lento (recorremos elemento a elemento en Python puro):

```python
>>> A = np.random.randint(-100, 100, size=(3000, 3000))
>>> B = np.random.randint(-100, 100, size=(3000, 3000))
>>> result = np.zeros_like(A)

>>> for i in range(A.shape[0]):
...     for j in range(A.shape[1]):
...         result[i, j] = customf(A[i, j], B[i, j])
# 2.31 s de media
```

## Mejorando rendimiento con funciones vectorizadas

Basta con decorar la funcion con `np.vectorize` para convertirla en una funcion que NumPy sabe aplicar de forma optimizada sobre arrays completos:

```python
@np.vectorize
def customf(a, b):
    if a > b:
        return a + b
    elif a < b:
        return a - b
    else:
        return 0

>>> customf(A, B)
# 1.16 s de media -> practicamente la mitad de tiempo
```

> Cuanto mas grandes son las matrices, mayor es la mejora de rendimiento al vectorizar. Tambien se pueden vectorizar funciones `lambda`: `np.vectorize(lambda a, b: a + b)`.

## Fuente

Contenido basado en la seccion [NumPy](https://aprendepython.es/paquetes/ciencia-datos/numpy/) de *Aprende Python*.
