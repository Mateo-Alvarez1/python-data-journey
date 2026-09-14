# Algebra Lineal

NumPy tiene un submodulo dedicado al algebra lineal, `np.linalg`, con funciones muy utiles cuando trabajamos con matrices: producto matricial, determinante, inversa, traspuesta, potencias de matrices y resolucion de sistemas de ecuaciones lineales.

## Producto de matrices

El operador `*` entre dos arrays multiplica **elemento a elemento** (ya lo vimos en la seccion de operaciones aritmeticas). Para el producto matricial "clasico" (el del algebra lineal) usamos `np.dot()` o, desde Python 3.5, el operador `@`:

```python
>>> m1 = np.array([[1, 8, 4], [8, 7, 1], [1, 3, 8]])
>>> m2 = np.array([[1, 5, 7], [9, 4, 2], [1, 4, 2]])

>>> np.dot(m1, m2)
array([[77, 53, 31],
       [72, 72, 72],
       [36, 49, 29]])

>>> m1 @ m2          # Equivalente y mas legible
array([[77, 53, 31],
       [72, 72, 72],
       [36, 49, 29]])
```

## Determinante de una matriz

El determinante se calcula con `np.linalg.det()`:

```python
>>> m = np.array([[4, 1, 6], [4, 8, 8], [2, 1, 7]])

>>> np.linalg.det(m)
108.00000000000003
```

> El resultado puede venir con pequenos errores de precision (coma flotante), por eso no da un `108` exacto.

## Inversa de una matriz

La inversa de una matriz cuadrada (cuando existe, es decir, cuando el determinante es distinto de 0) se calcula con `np.linalg.inv()`:

```python
>>> m_inv = np.linalg.inv(m)
>>> m_inv
array([[ 0.44444444, -0.00925926, -0.37037037],
       [-0.11111111,  0.14814815, -0.07407407],
       [-0.11111111, -0.01851852,  0.25925926]])
```

Una propiedad clave: si multiplicamos una matriz por su inversa, obtenemos la matriz identidad (`A * A^-1 = I`):

```python
>>> np.dot(m, m_inv)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

## Traspuesta de una matriz

Trasponer una matriz consiste en intercambiar filas por columnas. En NumPy es tan simple como acceder al atributo `.T`:

```python
>>> m = np.array([[1, 2, 3], [4, 5, 6]])

>>> m.T
array([[1, 4],
       [2, 5],
       [3, 6]])
```

## Elevar matriz a potencia

Elevar una matriz a una potencia (multiplicarla por si misma `n` veces usando el producto matricial, no elemento a elemento) se hace con `np.linalg.matrix_power()`:

```python
>>> m = np.array([[4, 1, 6], [4, 8, 8], [2, 1, 7]])

>>> np.linalg.matrix_power(m, 3)
array([[ 348,  250,  854],
       [ 848,  816, 2000],
       [ 310,  231,  775]])
```

## Sistemas de ecuaciones lineales

NumPy permite resolver sistemas de ecuaciones lineales modelandolos como `A @ X = B`, donde `A` es la matriz de coeficientes y `B` el vector de resultados.

Por ejemplo, para resolver:

```python
x1 + 2*x3 = 1
x1 - x2 = -2
x2 + x3 = -1
```

Definimos las matrices y usamos `np.linalg.solve()`:

```python
>>> A = np.array([[1, 0, 2], [1, -1, 0], [0, 1, 1]])
>>> B = np.array([1, -2, -1]).reshape(-1, 1)

>>> np.linalg.solve(A, B)
array([[-7.],
       [-5.],
       [ 4.]])
```

La solucion tambien se puede obtener manualmente despejando `X = A^-1 * B`, y el resultado debe coincidir:

```python
>>> np.dot(np.linalg.inv(A), B)
array([[-7.],
       [-5.],
       [ 4.]])
```

> `np.linalg.solve()` es preferible a calcular la inversa manualmente: es mas eficiente y mas estable numericamente.
