# Exploración de DataFrames

Antes de operar sobre un `DataFrame`, es habitual inspeccionar su contenido: revisar una muestra de filas, verificar su tamaño o navegar por sus datos de forma interactiva. Pandas ofrece varios métodos para esto, pensados para evitar imprimir un `DataFrame` completo cuando este contiene un volumen grande de filas.

## Primeras filas: `.head()`

`head()` devuelve las primeras `n` filas del `DataFrame`. Si no se indica el parámetro `n`, el valor por defecto es `5`.

```python
>>> df.head()
```

```python
>>> df.head(10)
```

### Parámetros

- `n` (`int`, opcional): cantidad de filas a devolver desde el inicio del `DataFrame`. Por defecto es `5`.

### Retorno

Un nuevo `DataFrame` con las primeras `n` filas.

## Últimas filas: `.tail()`

`tail()` devuelve las últimas `n` filas del `DataFrame`. Al igual que `head()`, el valor por defecto de `n` es `5`.

```python
>>> df.tail()
```

### Parámetros

- `n` (`int`, opcional): cantidad de filas a devolver desde el final del `DataFrame`. Por defecto es `5`.

### Retorno

Un nuevo `DataFrame` con las últimas `n` filas.

> **Consideración:** `head()` y `tail()` son métodos distintos: `head()` toma filas desde el inicio del `DataFrame` y `tail()` desde el final. No deben confundirse entre sí ni utilizarse indistintamente para el mismo propósito.

## Filas aleatorias: `.sample()`

`sample()` devuelve una selección aleatoria de filas del `DataFrame`. Es útil para inspeccionar datos sin el sesgo de mirar siempre el principio o el final del conjunto de datos.

```python
>>> df.sample(50)
```

### Parámetros

- `n` (`int`, opcional): cantidad de filas a devolver. Si no se indica, devuelve una única fila.
- `random_state` (`int`, opcional): semilla para hacer reproducible la selección aleatoria entre distintas ejecuciones.

### Retorno

Un nuevo `DataFrame` con `n` filas seleccionadas al azar, en orden de índice no necesariamente secuencial.

## Selección de un rango de filas por posición: `.iloc[]`

`.iloc[]` permite acceder a un subconjunto de filas según su posición numérica (índice entero), de forma independiente al valor de la etiqueta de índice. Acepta la misma sintaxis de slicing que las listas de Python.

```python
>>> df.iloc[500:550]
```

El ejemplo anterior devuelve las filas ubicadas entre la posición `500` (incluida) y la posición `550` (excluida).

### Consideraciones

- `.iloc[]` indexa por **posición**, no por el valor de la etiqueta del índice. Esto es relevante cuando el índice del `DataFrame` no es el rango por defecto (por ejemplo, luego de aplicar un filtro).
- Es un caso particular dentro de la selección e indexado de datos en Pandas, tema que se documentará en mayor profundidad (incluyendo `.loc[]` e indexado booleano) a medida que se incorporen notebooks que lo cubran.

## Visualización interactiva con `itables`

[`itables`](https://mwouts.github.io/itables/) es una librería externa, independiente de Pandas, que permite mostrar `DataFrame` y `Series` como tablas interactivas dentro de un notebook de Jupyter (con paginación, búsqueda y ordenamiento), en lugar de la salida de texto estática habitual.

```python
>>> from itables import init_notebook_mode
>>> init_notebook_mode(all_interactive=True)
>>> mining_warehouse
```

### Consideraciones

- `init_notebook_mode()` habilita el modo interactivo para la sesión actual del notebook.
- El parámetro `all_interactive=True` hace que **todos** los `DataFrame` y `Series` que se muestren a partir de ese punto en el notebook se rendericen automáticamente como tablas interactivas, sin necesidad de invocar una función adicional en cada celda.
- Requiere instalar la librería por separado (`pip install itables`); no forma parte de la instalación estándar de Pandas.

## Conceptos relacionados

- [Creación de DataFrames](../01-Dataframes/creacion_de_dataframes.md)
- [Atributos y métodos generales de un DataFrame](../01-Dataframes/atributos_de_dataframes.md)
- [Índice de Pandas](../INDEX.md)
