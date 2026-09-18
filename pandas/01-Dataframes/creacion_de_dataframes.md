# Creación de DataFrames

Un `DataFrame` es la estructura de datos principal de Pandas: una tabla bidimensional, etiquetada, con columnas que pueden ser de distinto tipo de dato. Puede pensarse como una colección de `Series` que comparten el mismo índice.

Antes de trabajar con Pandas, se importan las dos librerías habituales:

```python
import numpy as np
import pandas as pd
```

Existen varias formas de crear un `DataFrame`, dependiendo de dónde provienen los datos de origen.

## A partir de un array de NumPy

`pd.DataFrame()` acepta directamente un array de NumPy. Cada fila del array se convierte en una fila del DataFrame, y las columnas se numeran automáticamente empezando en `0` (salvo que se indique lo contrario con el parámetro `columns`).

```python
>>> array = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 19]])
>>> df = pd.DataFrame(array)
>>> df
   0   1
0  1   2
1  3   4
2  5   6
3  7   8
4  9  19
```

> Es importante asignar el resultado de `pd.DataFrame(...)` a una variable (por ejemplo `df`). Si no se guarda la referencia, el DataFrame no queda disponible para reutilizarlo en celdas o líneas posteriores.

## A partir de un diccionario

Cuando el origen de los datos es un diccionario de Python, cada **clave** se convierte en el nombre de una columna, y cada **valor** (una lista o secuencia) se convierte en los datos de esa columna. Todas las listas deben tener la misma longitud.

```python
>>> states = ["California", "Texas", "Arizona", "Florida"]
>>> population = [75432, 13456, 98765, 43212]

>>> dictionary = {"States": states, "Population": population}
>>> pd.DataFrame(dictionary)
       States  Population
0  California       75432
1       Texas       13456
2     Arizona       98765
3     Florida       43212
```

Esta forma de creación es especialmente útil cuando los datos ya están organizados conceptualmente por columna (por ejemplo, resultado de varias listas generadas por separado), en lugar de por fila.

## A partir de un archivo CSV

`pd.read_csv()` lee un archivo de valores separados por un delimitador y lo convierte en un `DataFrame`. Acepta la ruta del archivo como primer argumento.

```python
>>> df = pd.read_csv("datos/ventas.csv")
```

Por defecto, `read_csv()` asume que el delimitador es una coma (`,`). Cuando el archivo usa otro separador (por ejemplo `;`, habitual en archivos exportados con configuración regional en español), hay que indicarlo explícitamente con el parámetro `sep`:

```python
>>> df = pd.read_csv("datos/ventas.csv", sep=";")
```

### Consideraciones

- La primera fila del CSV se interpreta como encabezado (nombres de columnas) por defecto.
- `read_csv()` acepta muchos otros parámetros para casos particulares (codificación, columnas a usar como índice, tipos de dato por columna, filas a saltear, etc.), que se documentan a medida que aparezcan en los notebooks.

## Conceptos relacionados

- [Atributos y métodos generales de un DataFrame](atributos_de_dataframes.md)
- [Índice de Pandas](../INDEX.md)
