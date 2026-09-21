# Operaciones con DataFrames y Series

## Métodos de agregación sobre una columna

Aplicados sobre una `Series` (por ejemplo, una columna numérica de un `DataFrame`), estos métodos devuelven un único valor calculado a partir de todos los elementos:

| Método | Descripción |
|---|---|
| `.sum()` | Suma de todos los valores. |
| `.count()` | Cantidad de valores no nulos (excluye `NaN`). |
| `.mean()` | Promedio de los valores. |
| `.std()` | Desviación estándar de los valores. |
| `.min()` | Valor mínimo. |
| `.max()` | Valor máximo. |

```python
>>> df['unit_cost_usd'].sum()
np.float64(179187306.13)

>>> df['unit_cost_usd'].mean()
np.float64(1388.0481988179065)

>>> df['unit_cost_usd'].std()
np.float64(5103.122799176936)

>>> df['unit_cost_usd'].min()
np.float64(3.18)

>>> df['unit_cost_usd'].max()
np.float64(81247.86)
```

### `.count()` no es un promedio

`.count()` devuelve la cantidad de valores **no nulos** de la `Series` (un número entero, como máximo igual a la longitud total de la `Series`). No calcula ningún promedio.

```python
>>> df['unit_cost_usd'].count()
129093
```

> **Corrección:** el notebook de origen muestra, para la celda de `.count()`, una salida idéntica a la de `.mean()` (`np.float64(1388.0481988179065)`). Esto no corresponde al comportamiento real de `.count()`; es una salida desactualizada, producto de haber re-ejecutado las celdas en un orden que dejó cacheado el resultado de una celda anterior. El valor real de `.count()` sobre una columna sin valores nulos coincide con la cantidad total de filas del `DataFrame` (`len(df)`).

### Calcular varias estadísticas a la vez

En lugar de invocar cada método de agregación por separado, `.describe()` calcula varios de una vez. Ver [Atributos y métodos generales de un DataFrame](../01-Dataframes/atributos_de_dataframes.md#resumen-estadístico-describe).

## Frecuencia de valores por categoría (`value_counts()`)

Aplicado sobre una `Series`, `value_counts()` cuenta cuántas veces aparece cada valor único y devuelve el resultado como una nueva `Series`: el índice contiene los valores únicos originales y los datos contienen la cantidad de apariciones de cada uno, ordenada de forma descendente por defecto.

```python
>>> df['year'].value_counts()
year
2024    43982
2025    43924
2026    30619
2023    10568
Name: count, dtype: int64
```

### Parámetro `normalize`

Con `normalize=True`, en lugar de la cantidad absoluta de apariciones, devuelve la frecuencia relativa de cada valor (la proporción que representa sobre el total, entre 0 y 1).

```python
>>> df['year'].value_counts(normalize=True)
year
2024    0.340700
2025    0.340251
2026    0.237186
2023    0.081863
Name: proportion, dtype: float64
```

```python
>>> df['reference_type'].value_counts(normalize=True)
reference_type
Pedido de Mina            0.451574
Orden de Transferencia    0.351622
Orden de Compra           0.192032
Ajuste de Inventario      0.004384
Nota de Devolución        0.000387
Name: proportion, dtype: float64
```

### Otros parámetros

- `sort`: si es `True` (valor por defecto), ordena el resultado por frecuencia. Si es `False`, conserva el orden de aparición de los valores únicos.
- `ascending`: si es `True`, ordena de menor a mayor frecuencia en lugar de mayor a menor.
- `dropna`: si es `True` (valor por defecto), excluye los valores `NaN` del conteo.

### Consideraciones

- A diferencia de `.count()` (que devuelve un único número: la cantidad de valores no nulos), `value_counts()` devuelve una `Series` con el conteo desagregado por cada valor único.
- La suma de todos los valores devueltos por `value_counts()` (sin `normalize`) es igual a `.count()` sobre la misma `Series`.

## Operaciones aritméticas entre columnas

Las columnas de un `DataFrame` (`Series`) admiten operadores aritméticos estándar (`+`, `-`, `*`, `/`, entre otros). La operación se aplica **elemento por elemento**, alineando los valores por índice, y devuelve una nueva `Series`.

```python
>>> df['total_value_usd'] + df['unit_cost_usd']
0          441.60
1         1108.80
2         2638.32
...
Length: 129093, dtype: float64
```

### Consideraciones

- Ambas `Series` deben compartir el mismo índice (o uno compatible) para que la alineación tenga sentido; si los índices no coinciden, el resultado incluye `NaN` en las posiciones sin correspondencia.
- El resultado de la operación no se guarda automáticamente como columna nueva del `DataFrame`; para conservarlo, debe asignarse explícitamente (por ejemplo, `df['suma'] = df['total_value_usd'] + df['unit_cost_usd']`), ver [Selección y creación de columnas](../04-Seleccion/seleccion_de_columnas.md).

## Ordenamiento de datos (`sort_values()`)

Aplicado sobre un `DataFrame` (o una `Series`), `sort_values()` devuelve una copia ordenada según los valores de una o más columnas.

```python
>>> df.sort_values('month', ascending=False)
```

### Sintaxis

```python
df.sort_values(by, ascending=True, inplace=False, key=None)
```

### Parámetros

- `by` (`str` o lista de `str`): nombre de la columna, o lista de nombres de columnas, por la cual ordenar. Si se indica una lista, el ordenamiento se aplica en el orden dado (primero por la primera columna, luego por la segunda para desempatar, y así sucesivamente).
- `ascending` (`bool` o lista de `bool`, opcional): dirección del ordenamiento. Por defecto es `True` (ascendente). Cuando `by` es una lista y `ascending` es un único booleano, esa dirección se aplica a todas las columnas indicadas; también puede pasarse una lista de booleanos, uno por cada columna de `by`.
- `inplace` (`bool`, opcional): si es `True`, ordena el `DataFrame` original y no devuelve nada (`None`). Por defecto es `False`, en cuyo caso `sort_values()` devuelve un nuevo `DataFrame` ordenado y el original permanece sin cambios.
- `key` (`callable`, opcional): función aplicada a los valores de la(s) columna(s) antes de ordenar. A diferencia del parámetro `key` de `sorted()` en Python puro, esta función recibe la columna completa como una `Series` (no cada valor por separado) y debe devolver una `Series` o un array del mismo tamaño.

### Retorno

Un nuevo `DataFrame` ordenado, o `None` si `inplace=True`.

### Ejemplos

Ordenar por una sola columna, de forma descendente:

```python
>>> df.sort_values('month', ascending=False)
```

Ordenar por varias columnas (primero por `month`, luego por `year` para los valores empatados):

```python
>>> df.sort_values(['month', 'year'], ascending=True)
```

Ordenar y aplicar el resultado directamente sobre el `DataFrame` original:

```python
>>> df.sort_values(['month', 'year'], ascending=True, inplace=True)
```

Ordenar utilizando una función `key` (por ejemplo, para ignorar mayúsculas/minúsculas en una columna de texto):

```python
>>> df.sort_values('day_of_week', ascending=True, key=lambda col: col.str.lower())
```

### Consideraciones

- Por defecto, `sort_values()` no modifica el `DataFrame` original; para conservar el resultado hay que asignarlo a una variable o utilizar `inplace=True`.
- `key` se aplica de forma vectorizada sobre toda la columna, no elemento por elemento.

## Conceptos relacionados

- [Atributos y métodos generales de un DataFrame](../01-Dataframes/atributos_de_dataframes.md)
- [Series](../03-Series/series.md)
- [Selección y creación de columnas](../04-Seleccion/seleccion_de_columnas.md)
