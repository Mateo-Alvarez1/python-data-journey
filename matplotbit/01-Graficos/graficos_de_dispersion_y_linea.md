# Gráficos de dispersión y línea (Matplotlib y Seaborn)

`matplotlib` es la librería base de visualización en Python. `seaborn` es una librería construida sobre `matplotlib` que simplifica la creación de gráficos estadísticos, aceptando directamente columnas (`Series`) de un `DataFrame` de Pandas como argumentos.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

## Crear una figura: `plt.figure()`

Crea una nueva figura (el lienzo sobre el que se dibuja el gráfico) antes de graficar.

### Sintaxis

```python
plt.figure(figsize=(ancho, alto), tight_layout=True)
```

### Parámetros

- `figsize` (`tuple`, opcional): tamaño de la figura en pulgadas, como `(ancho, alto)`.
- `tight_layout` (`bool`, opcional): si es `True`, ajusta automáticamente el espaciado entre los elementos de la figura para evitar que se superpongan o se corten (por ejemplo, etiquetas de ejes).

## Gráfico de dispersión: `sns.scatterplot()`

Dibuja un gráfico de dispersión (un punto por observación) a partir de dos variables.

### Sintaxis

```python
sns.scatterplot(x=x, y=y)
```

### Parámetros

- `x`: valores para el eje X (por ejemplo, una columna/`Series` de un `DataFrame`).
- `y`: valores para el eje Y.

## Gráfico de línea: `sns.lineplot()`

Dibuja una línea que conecta una secuencia de puntos. Se utiliza habitualmente junto con `scatterplot()` para superponer, por ejemplo, una recta de regresión sobre los datos observados.

### Sintaxis

```python
sns.lineplot(x=x, y=y_pred, color='red')
```

### Parámetros

- `x`: valores para el eje X.
- `y`: valores para el eje Y (por ejemplo, los valores predichos por un modelo).
- `color` (`str`, opcional): color de la línea.

## Límites de los ejes: `plt.xlim()` y `plt.ylim()`

Establecen los límites visibles del eje X y del eje Y respectivamente.

```python
plt.xlim(0)
plt.ylim(0)
```

Al pasar un único valor, ese valor se utiliza como límite inferior del eje, dejando el límite superior determinado automáticamente por los datos.

## Guardar la figura: `plt.savefig()`

Guarda la figura actual como un archivo de imagen.

### Sintaxis

```python
plt.savefig('nombre_del_archivo')
```

### Consideraciones

- Debe invocarse **antes** de `plt.show()`: en algunos entornos, mostrar la figura con `plt.show()` puede liberar los recursos de la figura, por lo que guardarla después podría producir un archivo vacío o incorrecto.
- Si no se especifica una extensión en el nombre del archivo, `matplotlib` utiliza un formato por defecto (habitualmente PNG).

## Mostrar la figura: `plt.show()`

Renderiza y muestra la figura construida con las instrucciones anteriores.

```python
plt.show()
```

## Ejemplo completo

Superponer una recta de regresión sobre un gráfico de dispersión:

```python
plt.figure(figsize=(6, 4), tight_layout=True)

sns.scatterplot(x=x['stock_before'], y=y)
sns.lineplot(x=x['stock_before'], y=y_pred, color='red')

plt.xlim(0)
plt.ylim(0)
plt.savefig('linear_regression')
plt.show()
```

## Conceptos relacionados

- [Visualización de DataFrames](../../pandas/06-Visualizacion/visualizacion_de_dataframes.md)
- [Regresión lineal sobre datos de Pandas](../../pandas/07-Analisis-Estadistico/regresion_lineal.md)
