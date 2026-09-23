# Pandas

Documentación técnica de referencia sobre la librería Pandas, generada a partir de los notebooks de práctica del proyecto.

## Contenidos

- [Creación de DataFrames](./01-Dataframes/creacion_de_dataframes.md): construcción de un `DataFrame` a partir de arrays de NumPy, diccionarios y archivos CSV.
- [Atributos y métodos generales de un DataFrame](./01-Dataframes/atributos_de_dataframes.md): `.shape`, `.index`, `.columns`, `.dtypes`, `.info()`, `.describe()`, `len()`, `type()` y `round()`.
- [Exploración de DataFrames](./02-Exploracion/exploracion_de_dataframes.md): inspección de un `DataFrame` con `.head()`, `.tail()`, `.sample()`, selección de un rango de filas con `.iloc[]` y visualización interactiva con `itables`.
- [Series](./03-Series/series.md): qué es una `Series`, cómo se obtiene a partir de un `DataFrame` y sus atributos/métodos básicos.
- [Selección y creación de columnas](./04-Seleccion/seleccion_de_columnas.md): selección de una o varias columnas y agregado de columnas nuevas a partir de valores escalares o arrays.
- [Operaciones con DataFrames y Series](./05-Operaciones/operaciones_con_dataframes.md): métodos de agregación (`.sum()`, `.count()`, `.mean()`, `.std()`, `.min()`, `.max()`), conteo de frecuencias por categoría (`value_counts()`, incluyendo el parámetro `normalize`), ordenamiento con `sort_values()` (una o varias columnas, `ascending`, `inplace`, `key`) y operaciones aritméticas entre columnas.
- [Visualización de DataFrames](./06-Visualizacion/visualizacion_de_dataframes.md): gráficos generados directamente desde un `DataFrame` con `.plot(kind='scatter')`.
- [Regresión lineal sobre datos de Pandas](./07-Analisis-Estadistico/regresion_lineal.md): construcción de un modelo de regresión lineal simple con `statsmodels` (`sm.add_constant()`, `sm.OLS()`, `.fit()`, `.predict()`, `.summary()`) a partir de columnas de un `DataFrame`.
- [Regresión lineal: fundamentos matemáticos y visualización](./07-Analisis-Estadistico/teoria_regresion_lineal.md): la teoría de la regresión lineal simple explicada en lenguaje simple, con un glosario que traduce cada símbolo (`β0`, `β1`, `Σ`, `x̄`, `R²`, etc.), un ejemplo numérico resuelto paso a paso, y ejemplos de visualización con `matplotlib`/`seaborn` (incluyendo `sns.regplot()`).

Esta sección se irá ampliando a medida que se incorporen nuevos notebooks (selección avanzada con `.loc[]`, indexado booleano, limpieza, `groupby`, combinación de datasets, etc.).
