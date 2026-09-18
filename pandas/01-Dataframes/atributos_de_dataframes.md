# Atributos y métodos generales de un DataFrame

Una vez creado un `DataFrame`, Pandas ofrece un conjunto de atributos y métodos para conocer su estructura general: cantidad de filas y columnas, tipo de dato de cada columna, resumen estadístico, etc. Estos son el punto de partida habitual antes de operar sobre los datos.

## Dimensiones: `.shape`

`shape` devuelve una tupla `(filas, columnas)` con el tamaño de cada eje del `DataFrame`.

```python
>>> df.shape
(129093, 38)
```

### Retorno

Una tupla de dos enteros: `(cantidad_de_filas, cantidad_de_columnas)`.

## Índice: `.index`

`index` devuelve las etiquetas de fila del `DataFrame`. Cuando no se especificó un índice propio al crear el `DataFrame`, Pandas asigna por defecto un `RangeIndex` (una secuencia numérica consecutiva, similar a `range()`).

```python
>>> df.index
RangeIndex(start=0, stop=129093, step=1)
```

Al ser un objeto iterable, admite funciones incorporadas de Python como `len()`, `min()` y `max()`:

```python
>>> len(df)
129093

>>> min(df.index)
0

>>> max(df.index)
129092
```

`len(df)` es equivalente a `df.shape[0]`: la cantidad de filas del `DataFrame`.

## Columnas: `.columns`

`columns` devuelve las etiquetas de columna del `DataFrame`, como un objeto `Index`.

```python
>>> df.columns
Index(['movement_id', 'movement_date', 'year', ...], dtype='str')
```

## Tipo de dato por columna: `.dtypes`

`dtypes` devuelve una `Series` que asocia cada columna con su tipo de dato (`dtype`).

```python
>>> df.dtypes
movement_id     str
year           int64
unit_cost_usd  float64
dtype: object
```

### Consideraciones

- Es habitual que columnas numéricas se infieran como `int64` o `float64`, y columnas de texto como `str` u `object`, según la versión de Pandas.
- Revisar `dtypes` permite detectar columnas que deberían ser numéricas o de fecha pero fueron leídas como texto (por ejemplo, al importar un CSV), un problema frecuente al usar `pd.read_csv()`.

## Resumen general: `.info()`

`info()` imprime un resumen conciso del `DataFrame`: cantidad de entradas, columnas con su tipo de dato y cantidad de valores no nulos, y uso de memoria aproximado.

```python
>>> df.info()
<class 'pandas.DataFrame'>
RangeIndex: 129093 entries, 0 to 129092
Data columns (total 38 columns):
 #   Column        Non-Null Count   Dtype
---  ------        --------------   -----
 0   movement_id   129093 non-null  str
 ...
dtypes: float64(3), int64(4), str(31)
memory usage: ...
```

### Consideraciones

- `info()` es un **método** y requiere ser invocado con paréntesis (`df.info()`). Escribir `df.info` sin paréntesis no ejecuta el método: devuelve una referencia al método en sí (`<bound method DataFrame.info of ...>`), no el resumen. Es un error frecuente al escribirlo apurado.
- A diferencia de `.describe()`, `.info()` es la forma indicada para detectar rápidamente columnas con valores nulos (comparando la cantidad total de filas contra el "Non-Null Count" de cada columna).

## Resumen estadístico: `.describe()`

`describe()` devuelve un nuevo `DataFrame` con estadísticas descriptivas (`count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max`) calculadas sobre las columnas numéricas.

```python
>>> df.describe()
              year         quantity
count  129093.000  129093.000000
mean     2024.733      23.019986
std         0.913      40.274099
min      2023.000       1.000000
...
```

### Consideraciones

- Por defecto, `describe()` solo incluye columnas numéricas (`int`, `float`). Las columnas de texto se excluyen del resultado.
- Puede combinarse con `round()` para reducir la cantidad de decimales mostrados: `df.describe().round(2)`.

## Tipo del objeto: `type()`

La función incorporada `type()` de Python permite confirmar la clase de un objeto de Pandas.

```python
>>> type(df)
pandas.DataFrame
```

Este patrón es útil para verificar si el resultado de una operación sigue siendo un `DataFrame` o pasó a ser una `Series` (por ejemplo, al seleccionar una sola columna).

## Redondeo de valores: `round()`

La función incorporada `round()` de Python, al recibir un `DataFrame`, redondea los valores de todas sus columnas numéricas a la cantidad de decimales indicada.

```python
>>> round(df, 2)
```

### Parámetros

- `decimals` (`int`): cantidad de decimales a los que se redondea cada valor numérico.

### Retorno

Un nuevo `DataFrame` con los valores numéricos redondeados. Las columnas no numéricas permanecen sin cambios.

## Conceptos relacionados

- [Exploración de DataFrames](../02-Exploracion/exploracion_de_dataframes.md)
- [Series](../03-Series/series.md)
- [Índice de Pandas](../INDEX.md)
