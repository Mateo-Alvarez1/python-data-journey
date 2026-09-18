# Selección y creación de columnas

## Seleccionar una columna

Indexar un `DataFrame` con corchetes simples y el nombre de una columna devuelve esa columna como una `Series`.

```python
>>> df['movement_type']
```

Ver [Series](../03-Series/series.md) para más detalle sobre el resultado de esta operación.

## Seleccionar varias columnas

Indexar un `DataFrame` con una **lista** de nombres de columna (por eso el doble corchete: los corchetes externos indexan el `DataFrame`, y los internos definen la lista de nombres) devuelve un nuevo `DataFrame` que contiene únicamente esas columnas, en el orden indicado.

```python
>>> df[['movement_id', 'movement_type']]
        movement_id          movement_type
0       MOV-0000001   Transferencia Salida
1       MOV-0000002        Despacho a Mina
...

[129093 rows x 2 columns]
```

Puede indicarse cualquier cantidad de columnas:

```python
>>> df[['movement_id', 'movement_type', 'reference_type', 'mine_id']]
```

### Retorno

- `df['col']` (nombre de columna suelto): una `Series`.
- `df[['col1', 'col2', ...]]` (lista de nombres de columna): un `DataFrame`.

### Consideraciones

- El orden de las columnas en el resultado sigue el orden indicado en la lista, no necesariamente el orden original del `DataFrame`.
- Seleccionar una columna que no existe genera un `KeyError`.

## Agregar una columna nueva

Asignar a `df['nombre_de_columna']` crea la columna si no existe, o sobrescribe sus valores si ya existe.

### A partir de un valor escalar

Si el valor asignado es un escalar (un único valor), Pandas lo repite (broadcast) en todas las filas de la nueva columna.

```python
>>> df['calidad_material'] = 'Buena'
```

Todas las filas de `calidad_material` quedan con el valor `'Buena'`.

### A partir de un array o secuencia

Si el valor asignado es un array de NumPy, una lista o una `Series`, cada elemento se asigna a la fila correspondiente, en el mismo orden.

```python
>>> import numpy as np
>>> array = np.arange(0, 129093)
>>> df['coords'] = array
```

### Consideraciones

- Cuando se asigna un array o una lista, su longitud debe coincidir con la cantidad de filas del `DataFrame` (`len(df)`); de lo contrario, Pandas genera un error.
- Cuando se asigna una `Series`, la asignación se alinea por índice (no por posición): los valores se ubican según coincidencia de etiquetas de índice, y las filas sin coincidencia quedan como `NaN`.

## Conceptos relacionados

- [Series](../03-Series/series.md)
- [Atributos y métodos generales de un DataFrame](../01-Dataframes/atributos_de_dataframes.md)
- [Operaciones con DataFrames y Series](../05-Operaciones/operaciones_con_dataframes.md)
