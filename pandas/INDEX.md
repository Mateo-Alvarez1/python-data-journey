# Pandas

Documentación técnica de referencia sobre la librería Pandas, generada a partir de los notebooks de práctica del proyecto.

## Contenidos

- [Creación de DataFrames](./01-Dataframes/creacion_de_dataframes.md): construcción de un `DataFrame` a partir de arrays de NumPy, diccionarios y archivos CSV.
- [Atributos y métodos generales de un DataFrame](./01-Dataframes/atributos_de_dataframes.md): `.shape`, `.index`, `.columns`, `.dtypes`, `.info()`, `.describe()`, `len()`, `type()` y `round()`.
- [Exploración de DataFrames](./02-Exploracion/exploracion_de_dataframes.md): inspección de un `DataFrame` con `.head()`, `.tail()`, `.sample()`, selección de un rango de filas con `.iloc[]` y visualización interactiva con `itables`.
- [Series](./03-Series/series.md): qué es una `Series`, cómo se obtiene a partir de un `DataFrame` y sus atributos/métodos básicos.
- [Selección y creación de columnas](./04-Seleccion/seleccion_de_columnas.md): selección de una o varias columnas y agregado de columnas nuevas a partir de valores escalares o arrays.
- [Operaciones con DataFrames y Series](./05-Operaciones/operaciones_con_dataframes.md): métodos de agregación (`.sum()`, `.count()`, `.mean()`, `.std()`, `.min()`, `.max()`) y operaciones aritméticas entre columnas.

Esta sección se irá ampliando a medida que se incorporen nuevos notebooks (selección avanzada con `.loc[]`, indexado booleano, limpieza, `groupby`, combinación de datasets, `value_counts()`, etc.).
