# Regresión lineal sobre datos de Pandas

## Qué es

La regresión lineal es un método estadístico que evalúa la relación entre una variable dependiente y una o más variables independientes, ajustando una recta que minimiza el error entre los valores observados y los valores predichos.

Esta sección documenta el flujo habitual para construir un modelo de regresión lineal simple a partir de columnas (`Series`) de un `DataFrame` de Pandas, utilizando la librería externa [`statsmodels`](https://www.statsmodels.org/). `statsmodels` no forma parte de Pandas, pero opera directamente sobre objetos `Series` y `DataFrame`.

```python
import statsmodels.api as sm
```

## Definir las variables del modelo

Se definen la variable dependiente (`y`, lo que se quiere predecir) y la variable independiente (`x`, la que se utiliza para predecir), cada una como una `Series` extraída del `DataFrame`.

```python
y = df['quantity']
x = df['stock_before']
```

## Agregar la constante: `sm.add_constant()`

`sm.OLS()` no agrega automáticamente un término independiente (intercepto) al modelo. `sm.add_constant()` agrega una columna adicional con el valor `1` en todas las filas, que actúa como el coeficiente independiente de la recta.

### Sintaxis

```python
sm.add_constant(x)
```

### Retorno

Un `DataFrame` con una columna `const` (todos sus valores en `1`) agregada a la(s) columna(s) originales de `x`.

### Consideraciones

- Si se omite este paso, el modelo ajusta la recta forzándola a pasar por el origen (`0,0`), lo cual generalmente no refleja la relación real entre las variables.

## Ajustar el modelo: `sm.OLS()` y `.fit()`

`sm.OLS(y, x)` construye un modelo de regresión lineal por mínimos cuadrados ordinarios (*Ordinary Least Squares*). `.fit()` ajusta el modelo a los datos y devuelve un objeto con los resultados.

### Sintaxis

```python
lm = sm.OLS(y, x).fit()
```

### Parámetros

- Primer argumento: la variable dependiente (`y`), como `Series` o array.
- Segundo argumento: la(s) variable(s) independiente(s) (`x`), incluyendo la columna `const` agregada previamente.

### Retorno

Un objeto de resultados del modelo ajustado, con métodos como `.predict()` y `.summary()`.

## Generar predicciones: `.predict()`

Devuelve los valores predichos por el modelo para cada fila de `x`.

```python
>>> predict = lm.predict(x)
>>> predict
0         61.729879
1         15.530687
2         10.030784
...
Length: 129093, dtype: float64
```

## Resumen del modelo: `.summary()`

Devuelve una tabla con las estadísticas del modelo ajustado: coeficientes, error estándar, significancia estadística (`p-values`), intervalos de confianza y medidas de bondad de ajuste.

```python
>>> lm.summary()
```

Del resumen se destacan, entre otros valores:

- **`R-squared`**: proporción de la variabilidad de `y` que es explicada por `x`. Va de `0` a `1`; cuanto más cercano a `1`, mejor explica el modelo la variable dependiente. En el ejemplo anterior, `R-squared = 0.486`.
- **`coef`**: los coeficientes estimados de la recta. En el ejemplo, `const = 9.2975` (intercepto) y `stock_before = 0.3667` (pendiente).
- **`P>|t|`**: p-value de cada coeficiente; un valor bajo (habitualmente menor a `0.05`) indica que el coeficiente es estadísticamente significativo.

## Ecuación de la recta

A partir de los coeficientes obtenidos en `.summary()`, la recta de regresión puede expresarse y calcularse de forma manual con la fórmula `y = coef_x * x + intercepto`:

```python
# coef constante = 9.2975
# coef stock_before = 0.3667
y_pred = 0.3667 * x['stock_before'] + 9.2975
```

Este cálculo manual produce el mismo resultado que `lm.predict(x)`, y resulta útil para graficar la recta de regresión superpuesta sobre los datos (ver [matplotlib](../../matplotbit/INDEX.md)).

## Conceptos relacionados

- [Operaciones con DataFrames y Series](../05-Operaciones/operaciones_con_dataframes.md)
- [Visualización de DataFrames](../06-Visualizacion/visualizacion_de_dataframes.md)
