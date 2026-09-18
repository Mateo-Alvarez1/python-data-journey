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

## Conceptos relacionados

- [Atributos y métodos generales de un DataFrame](../01-Dataframes/atributos_de_dataframes.md)
- [Series](../03-Series/series.md)
- [Selección y creación de columnas](../04-Seleccion/seleccion_de_columnas.md)
