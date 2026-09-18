# Series

Una `Series` es una estructura de datos unidimensional y etiquetada de Pandas: una secuencia de valores, cada uno asociado a una etiqueta de índice. Puede pensarse como una única columna de un `DataFrame`, o como un arreglo de NumPy al que se le agregan etiquetas.

## Obtener una Series a partir de un DataFrame

Seleccionar una única columna de un `DataFrame` con corchetes simples y el nombre de la columna devuelve una `Series`, no un `DataFrame`.

```python
>>> df['movement_type']
0          Transferencia Salida
1               Despacho a Mina
2               Despacho a Mina
...
Name: movement_type, Length: 129093, dtype: str
```

```python
>>> type(df['movement_type'])
pandas.Series
```

### Consideraciones

- El nombre de la columna original se conserva en el atributo `.name` de la `Series` (visible como `Name: ...` en la salida).
- Para seleccionar más de una columna a la vez (y obtener un `DataFrame` en lugar de una `Series`), ver [Selección de columnas](../04-Seleccion/seleccion_de_columnas.md).

## Atributos y métodos

Una `Series` comparte varios atributos y métodos con el `DataFrame`, ya que ambas estructuras heredan de una base común.

### `.index`

Devuelve las etiquetas de índice de la `Series`, igual que en un `DataFrame`.

```python
>>> df['movement_type'].index
RangeIndex(start=0, stop=129093, step=1)
```

### `.head(n)`

Devuelve los primeros `n` elementos de la `Series`. Se comporta de forma idéntica a `DataFrame.head()`.

```python
>>> df['movement_type'].head(5)
0    Transferencia Salida
1         Despacho a Mina
2         Despacho a Mina
3         Despacho a Mina
4         Despacho a Mina
Name: movement_type, dtype: str
```

#### Parámetros

- `n` (`int`, opcional): cantidad de elementos a devolver desde el inicio. Por defecto es `5`.

## Conceptos relacionados

- [Atributos y métodos generales de un DataFrame](../01-Dataframes/atributos_de_dataframes.md)
- [Exploración de DataFrames](../02-Exploracion/exploracion_de_dataframes.md)
- [Operaciones con DataFrames y Series](../05-Operaciones/operaciones_con_dataframes.md)
