# Fundamentos Basicos

## 1. ¿Qué es un ndarray?

El objeto central de NumPy es el **ndarray** (*n-dimensional array*), una estructura de datos que permite almacenar colecciones de elementos del mismo tipo (generalmente numéricos) organizados en una o más dimensiones. A diferencia de las listas de Python, los ndarray están optimizados para operaciones matemáticas y de álgebra lineal, siendo mucho más eficientes en memoria y velocidad.

Para empezar a trabajar con NumPy, primero hay que importar la librería:

```python
import numpy as np
```

## 2. Creación de arrays

### 2.1. Array vacío: `np.empty()`

Crea un array sin inicializar sus valores, es decir, reserva el espacio en memoria pero los valores que contiene son "basura" (lo que hubiera en esa memoria previamente). Es más rápido que otras funciones porque no pierde tiempo asignando valores, pero hay que tener cuidado porque el contenido es impredecible.

```python
np.empty((4,8))
# array([[ 6.23773039e-312, 1.05730048e-321, 0.00000000e+000, ...],
# [ 1.04855524e-042, 2.31657134e-052, 3.92362787e-033, ...],
# [ 5.49109388e-143, 1.06396443e+224, 3.96041428e+246, ...],
# [ 2.24151504e+174, 3.36163259e-067, 1.26189067e-076, ...]])
```

### 2.2. Array de ceros: `np.zeros()`

Crea un array completamente inicializado en `0`. Es útil cuando se necesita una estructura "en blanco" para ir llenando después.

```python
np.zeros((1,3))
#array([[0., 0., 0.]])
```

### 2.3. Array de unos: `np.ones()`

Similar a `zeros()`, pero inicializa todos los valores en `1`.

```python
np.ones((2,2))
#array([[1., 1.],
#      [1., 1.]])
```

### 2.4. Array con un valor constante: `np.full()`

Permite crear un array con una forma determinada, relleno con un valor específico que uno elige.

```python
np.full((4,8), 23)
#array([[23, 23, 23, 23, 23, 23, 23, 23],
#      [23, 23, 23, 23, 23, 23, 23, 23],
#      [23, 23, 23, 23, 23, 23, 23, 23],
#      [23, 23, 23, 23, 23, 23, 23, 23]])
```

### 2.5. Creación a partir de listas: `np.array()`

Convierte una lista (o lista de listas) de Python en un ndarray.

```python
np.array([
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
])
# array([[1, 2, 3, 4, 5, 6],
#      [1, 2, 3, 4, 5, 6]])
```

## 3. Reestructurar arrays: `np.reshape()`

`reshape()` permite cambiar la forma (dimensiones) de un array sin modificar sus datos, siempre y cuando la nueva forma sea compatible con la cantidad total de elementos.

En este ejemplo se generan 32 números aleatorios enteros entre 0 y 10, y luego se reorganizan en una matriz de 4 filas por 8 columnas:

```python
my_array = np.random.randint(0, 10, 32)
my_array_reshape = np.reshape(my_array, (4,8))
print(my_array_reshape)

# [[6 5 5 7 5 7 5 5]
#  [9 9 6 3 8 3 6 3]
#  [4 3 5 4 1 5 5 5]
#  [8 8 3 6 8 5 0 9]]
```

## 4. Guardar y cargar arrays

NumPy permite persistir arrays en disco en formato binario `.npy` mediante `np.save()`, y recuperarlos luego con `np.load()`.

```python
m = np.array(range(1,13)).reshape(3,4)
np.save("mi_matriz", m)          # Guardamos la matriz
M_reloaded = np.load('mi_matriz.npy')   # La cargamos
print(M_reloaded)

#[[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]
```

## 5. Valores aleatorios

El submódulo `np.random` ofrece varias funciones para generar números aleatorios, ya sea con distribución uniforme, enteros dentro de un rango, o siguiendo distribuciones de probabilidad específicas.

### 5.1. Números aleatorios uniformes: `np.random.rand()`

Genera valores flotantes aleatorios entre 0 y 1, siguiendo una distribución uniforme.

```python
np.random.rand(3,3)

#array([[0.19298778, 0.87955415, 0.95711903],
#      [0.91836519, 0.47830142, 0.88391669],
#      [0.92349573, 0.5068043 , 0.45559153]])
```

### 5.2. Enteros aleatorios: `np.random.randint()`

Genera números enteros aleatorios dentro de un rango definido (`low`, `high`), y opcionalmente con una cantidad determinada de elementos.

```python
my_array = np.random.randint(0, 10, 32)
```

En este caso se generaron 32 enteros aleatorios entre 0 (inclusive) y 10 (exclusive), que luego se reorganizaron con `reshape()` como se vio en el punto 3.

### 5.3. Otras distribuciones de probabilidad

Además de `rand()` y `randint()`, `np.random` incluye generadores para otras distribuciones estadísticas, entre las más comunes:

- `np.random.randn()`: distribución normal estándar (media 0, desvío 1).
- `np.random.normal(loc, scale, size)`: distribución normal con media y desvío configurables.
- `np.random.uniform(low, high, size)`: distribución uniforme continua en un rango elegido.
- `np.random.choice(a, size)`: selección aleatoria de elementos a partir de un array o rango dado.

Estas funciones son especialmente útiles para simulaciones, generación de datos sintéticos y pruebas estadísticas.

### 5.4. Distribución normal estándar: `np.random.randn()`

`np.random.randn()` genera números aleatorios siguiendo una **distribución normal estándar** (media 0, desvío estándar 1). A diferencia de `rand()`, que devuelve valores uniformes entre 0 y 1, `randn()` puede devolver tanto valores positivos como negativos, concentrados alrededor del 0.

```python
np.random.randn(3,3)

#array([[ 1.69052570e+00, -4.65937371e-01, 3.28201637e-02],
#      [ 4.07516283e-01, -7.88923029e-01, 2.06557291e-03],
#      [-8.90385858e-04, -1.75472431e+00, 1.01765801e+00]])
```

Si se necesita una distribución normal con media y desvío distintos a 0 y 1, se usa `np.random.normal(loc, scale, size)`, donde `loc` es la media deseada y `scale` el desvío estándar.

## 6. Reshape con `-1`: dejar que NumPy calcule la dimensión

Al usar `reshape()`, se le puede pasar `-1` en una de las dimensiones para indicarle a NumPy que **calcule automáticamente** ese valor en base a la cantidad total de elementos y las demás dimensiones especificadas. Es útil cuando no queremos hacer la cuenta a mano o cuando el tamaño del array puede variar.

```python
arr = np.array(range(1,13))

arr.reshape(3, -1)   # 12 elementos / 3 filas = 4 columnas

#array([[ 1, 2, 3, 4],
#      [ 5, 6, 7, 8],
#      [ 9, 10, 11, 12]])
```

## 6. El uso de `-1` en `reshape()`: dimensiones automáticas

Cuando usamos `reshape()`, normalmente tenemos que indicar todas las dimensiones nuevas del array (por ejemplo, `(3,4)`). Sin embargo, NumPy permite reemplazar **una** de esas dimensiones por `-1`, y automáticamente calcula el valor que le corresponde en base a:

- La cantidad total de elementos del array original.
- Las demás dimensiones que sí especificamos.

Esto evita tener que hacer la cuenta manualmente y es muy útil cuando el tamaño del array puede variar o simplemente no queremos calcularlo a mano.

NumPy despeja la dimensión marcada con `-1` a partir de esa ecuación.

### 6.1. Ejemplo base

```python
arr = np.array(range(1,13))   # 12 elementos en total
```

### 6.2. Dejando que NumPy calcule las columnas

Le decimos que queremos 3 filas, y que calcule solo cuántas columnas hacen falta:

```python
arr.reshape(3, -1)

#array([[ 1, 2, 3, 4],
#      [ 5, 6, 7, 8],
#      [ 9, 10, 11, 12]])
```

*(12 elementos ÷ 3 filas = 4 columnas)*

### 6.3. Dejando que NumPy calcule las filas

Ahora al revés: fijamos 4 columnas y dejamos que calcule las filas:

```python
arr.reshape(-1, 4)

#array([[ 1, 2, 3, 4],
#      [ 5, 6, 7, 8],
#      [ 9, 10, 11, 12]])
```

*(12 elementos ÷ 4 columnas = 3 filas)*

### 6.4. Otro ejemplo, con 2 filas

```python
arr.reshape(2, -1)

#array([[ 1, 2, 3, 4, 5, 6],
#      [ 7, 8, 9, 10, 11, 12]])
```

*(12 elementos ÷ 2 filas = 6 columnas)*

### 6.5. Reglas importantes

- Solo se puede usar `-1` en **una** dimensión por vez. Si se ponen dos o más `-1`, NumPy no tiene forma de resolver la ecuación y lanza un error.
- La cantidad total de elementos del array original debe ser **divisible exactamente** entre las dimensiones fijas que especificamos. Si no lo es, `reshape()` lanza un `ValueError`, porque no puede armar una matriz "pareja" con los elementos sobrantes.
- Es especialmente útil cuando se trabaja con datos cuyo tamaño no se conoce de antemano (por ejemplo, al leer un dataset), ya que evita tener que calcular una dimensión a mano cada vez.
