# Visualización de DataFrames

Pandas incluye el método `.plot()`, una interfaz simplificada sobre `matplotlib` que permite generar gráficos directamente a partir de un `DataFrame` o una `Series`, sin necesidad de invocar `matplotlib` de forma explícita para los casos más simples.

## Gráfico de dispersión: `.plot(kind='scatter')`

Permite representar la relación entre dos columnas numéricas de un `DataFrame` como un gráfico de dispersión (un punto por fila).

### Sintaxis

```python
df.plot(kind='scatter', x='columna_x', y='columna_y')
```

### Parámetros

- `kind` (`str`): tipo de gráfico a generar. `'scatter'` produce un gráfico de dispersión. Otros valores admitidos incluyen `'line'` (por defecto), `'bar'`, `'hist'`, entre otros.
- `x` (`str`): nombre de la columna a utilizar en el eje X. Es obligatorio cuando `kind='scatter'`.
- `y` (`str`): nombre de la columna a utilizar en el eje Y. Es obligatorio cuando `kind='scatter'`.

### Retorno

Un objeto `Axes` de `matplotlib`, sobre el cual pueden seguir aplicándose métodos de personalización adicionales (límites de ejes, títulos, etc.).

### Ejemplo

```python
>>> df.plot(kind='scatter', x='stock_before', y='quantity')
```

Genera un gráfico de dispersión que permite observar visualmente si existe una relación entre el stock disponible antes de un movimiento (`stock_before`) y la cantidad movida (`quantity`).

### Consideraciones

- Requiere tener `matplotlib` instalado, aunque no sea importado explícitamente.
- Para gráficos con mayor nivel de personalización (múltiples series, colores condicionales, líneas superpuestas), suele combinarse `matplotlib` y `seaborn` directamente sobre las columnas del `DataFrame`. Ver la documentación de [matplotlib](../../matplotbit/INDEX.md).

## Conceptos relacionados

- [Selección y creación de columnas](../04-Seleccion/seleccion_de_columnas.md)
- [Operaciones con DataFrames y Series](../05-Operaciones/operaciones_con_dataframes.md)
