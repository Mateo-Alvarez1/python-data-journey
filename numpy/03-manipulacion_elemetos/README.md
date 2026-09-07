# Manipulacion de elementos

Los arrays multidimensionales de NumPy están indexados por unos ejes que establecen la forma en la que debemos acceder a sus elementos. Véase el siguiente diagrama:

![Dimensioness](image.png)

## Arrays de una dimensión

Pasrtimos del siguiente arrray unidimensional:

```python
>>>values = np.array(range(10, 16))
>>> values
##array([10, 11, 12, 13, 14, 15])
```

### Acceso

```python
>>> values[2]
## 12
>>> values[-3]
## 13
```

### Modificación

```python
>>> values[0] = values[1] + values[5] #26
>>> values
##array([26, 11, 12, 13, 14, 15])
```

### Borrado

```python
>>> np.delete(values, 2)
# array([26, 11, 13, 14, 15])
>>> np.delete(values, (2, 3, 4))
# array([26, 11, 15])
```

### Insertar

```python
>>> np.append(values, 16) # Insertar al final
# array([26, 11, 12, 13, 14, 15, 16])
>>> np.insert(values, 1, 101) # Insertar en la posición 1
# array([26, 101, 11, 12, 13, 14, 15])
```

## Arrays  Multidimensionales

Partimos del siguiente array bidimensional:

```python
>>> values = np.arange(1, 13).reshape(3, 4)
>>> values
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

### Acceso

```python
>>> values[1, 2] # Elemento de la fila 1 y columna 2
## 7
>>> values[-1, -1] # Elemento de la última fila y última columna
## 12
>>> values[1, 2] # Elemento de la fila 1 y columna 2
## 7
```

### Modificación

```python
>>> values
#array([[ 1,  2,  3,  4],
#       [ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])
>>> values[0, 0] = 100 # Reemplaza el elemento de la fila 0 y columna 0

>>> values[1] = [55, 66, 77, 88] # Reemplaza la fila 1

>>> values[:,2] = [30, 70, 110] # Reemplaza la columna 2

>>> values
#array([[100,   2,  30,   4],
#       [ 55,  66,  70,  88],
#       [  9,  10, 110,  12]])
```

### Borrado

```python
>>> values
#array([[ 1,  2,  3,  4],
#       [ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])
>>> np.delete(values, 0, axis=0) # Axis=0 hace referencia a las filas

#array([[ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])

>>> np.delete(values, (1, 3), axis=1) # Axis=1 hace referencia a las columnas (borramos la columna 1 y 3)
#array([[ 1,  3],
#       [ 5,  7],
#       [ 9, 11]])

```

### Insertar

```python
>>> values
# array([
#[1,2],
#[3,4],
# ]),
>>> np.append(values, [[5, 6]], axis=0) # Insertamos una fila al final
# array([
#[1,2],
#[3,4],
#[5,6]
# ]),
>>> np.append(values, [[5], [6]], axis=1) # Insertamos una columna al final
# array([
#[1,2,5],
#[3,4,6],
# ]),
```

Insertar elementos en posiciones arbitrarias del array:

```python
>>> values
# array([
#[1,2],
#[3,4],
# ]),
>>> np.insert(values, 1, [[5, 6]], axis=0) # Insertamos una fila en la posición 1
# array([
#[1,2],
#[5,6],
#[3,4],
# ]),
>>> np.insert(values, 1, [[5], [6]], axis=1) # Insertamos una columna en la posición 1
# array([
#[1,5,2],
#[3,6,4],
# ]),
```
