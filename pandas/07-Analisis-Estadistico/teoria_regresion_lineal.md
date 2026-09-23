# Regresión lineal: fundamentos matemáticos y visualización

## Qué es

Imaginá que anotás, para varios estudiantes, cuántas horas estudiaron para un examen y qué nota sacaron. Si lo graficás en puntitos, probablemente veas que "a más horas, nota más alta", más o menos en línea recta.

La regresión lineal es la técnica que encuentra **esa recta que mejor pasa cerca de todos los puntos**. Una vez que la tenés, podés usarla para adivinar la nota de alguien nuevo con solo saber cuántas horas estudió, aunque esa persona no esté en la lista original.

Este documento complementa a [Regresión lineal sobre datos de Pandas](./regresion_lineal.md), que muestra el código con `statsmodels`. Acá se explica, en lenguaje simple, qué significan los símbolos de las fórmulas, con un ejemplo numérico resuelto paso a paso y ejemplos de gráficos con `matplotlib`/`seaborn`.

## Antes de las fórmulas: qué significa cada símbolo

Las fórmulas de estadística usan letras griegas y algunos signos raros. Antes de mostrar cualquier fórmula, esta es la traducción de cada símbolo a algo entendible:

| Símbolo | Cómo se lee | Qué significa, en criollo |
|---|---|---|
| `y` | "y" | El resultado que querés adivinar (en el ejemplo: la nota del examen) |
| `x` | "equis" | El dato que ya conocés y usás para adivinar (en el ejemplo: las horas estudiadas) |
| `β0` | "beta cero" | El **número base**: la nota que le pondría el modelo a alguien que estudió 0 horas |
| `β1` | "beta uno" | **Cuánto sube la nota por cada hora** que se estudia |
| `ε` | "épsilon" | El **error**: la diferencia entre lo que pasó de verdad y lo que la recta adivinó |
| `Σ` | "sigma" | Quiere decir **"sumá todos estos números"**. Por ejemplo, en vez de escribir `1+2+3+4+5`, en las fórmulas se escribe `Σ` y ya se sabe que hay que sumar todos los valores de la lista |
| `x̄` | "equis con rayita" (media de x) | El **promedio** de todos los valores de `x` |
| `ȳ` | "y con rayita" (media de y) | El **promedio** de todos los valores de `y` |
| `ŷ` | "y con sombrerito" | La nota que **adivina la recta**, para diferenciarla de la nota real `y` |
| `R²` | "erre cuadrado" | Un puntaje de `0` a `1` que dice **qué tan buena es la recta** para adivinar |

Con esta tabla a mano, las fórmulas de las siguientes secciones se pueden leer reemplazando cada símbolo por su significado.

## La fórmula de la recta

En criollo, la recta que arma el modelo dice:

```
nota adivinada = número base + (cuánto sube por hora × horas estudiadas)
```

En símbolos (es exactamente la misma idea, solo que más corta de escribir):

```
y = β0 + β1 · x
```

- Si alguien estudió `0` horas, el modelo le pone la nota `β0` (el número base).
- Por cada hora extra que estudia, la nota sube `β1` puntos.

Nadie acierta la nota exacta siempre: la diferencia entre la nota real y la nota adivinada por la recta es el error, `ε`.

## Cómo se elige "la mejor" recta

Se podrían dibujar mil rectas distintas que pasen más o menos cerca de los puntos. ¿Cómo se elige cuál es la mejor?

La idea (llamada "mínimos cuadrados") es como un juego con estas reglas:

1. Para cada punto del gráfico, se mide qué tan lejos quedó de la recta (hacia arriba o hacia abajo). Esa distancia es el error de ese punto.
2. Ese error se eleva al cuadrado (se multiplica por sí mismo). Esto hace dos cosas: evita que un error "hacia arriba" cancele a uno "hacia abajo" al sumarlos, y castiga más fuerte a los puntos que quedaron muy lejos.
3. Se suman todos esos errores al cuadrado, de todos los puntos.
4. Se elige la recta que da la suma más chica posible.

Esa suma tiene nombre: `RSS` (la suma de los errores al cuadrado). Y esas dos reglas para calcular la mejor recta (el número base `β0` y cuánto sube por hora `β1`) son:

```
cuánto sube por hora = suma de[ (cada x − promedio de x) × (cada y − promedio de y) ]
                        ─────────────────────────────────────────────────────────────
                        suma de[ (cada x − promedio de x) al cuadrado ]

número base = promedio de y − (cuánto sube por hora × promedio de x)
```

En símbolos, lo mismo se escribe así:

```
β1 = Σ (xi − x̄)(yi − ȳ) / Σ (xi − x̄)²

β0 = ȳ − β1·x̄
```

(El `i` chiquito solo indica "cada dato de la lista, uno por uno": `x1` es el primer valor de `x`, `x2` el segundo, y así.)

## Ejemplo resuelto paso a paso

Datos de 5 estudiantes: horas de estudio (`x`) y nota del examen (`y`).

| x (horas) | y (nota) |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 4 |
| 5 | 5 |

**Paso 1 — Calcular los promedios.**

Promedio de horas: `(1+2+3+4+5) / 5 = 3`
Promedio de notas: `(2+4+5+4+5) / 5 = 4`

**Paso 2 — Para cada estudiante, ver cuánto se aleja del promedio.**

| x | y | x − promedio_x | y − promedio_y | los dos multiplicados | (x − promedio_x) al cuadrado |
|---|---|---|---|---|---|
| 1 | 2 | −2 | −2 | 4 | 4 |
| 2 | 4 | −1 | 0 | 0 | 1 |
| 3 | 5 | 0 | 1 | 0 | 0 |
| 4 | 4 | 1 | 0 | 0 | 1 |
| 5 | 5 | 2 | 1 | 2 | 4 |
| | | | **suma →** | **6** | **10** |

**Paso 3 — Calcular cuánto sube la nota por hora, y el número base.**

```
cuánto sube por hora = 6 / 10 = 0.6
número base = 4 − (0.6 × 3) = 2.2
```

**Paso 4 — Armar la recta:**

```
nota adivinada = 2.2 + 0.6 × horas estudiadas
```

Es decir: alguien que no estudia nada arrancaría con un `2.2`, y suma `0.6` puntos por cada hora que estudió.

**Paso 5 — Probar la recta con cada estudiante:**

| x (horas) | nota adivinada = 2.2 + 0.6·x |
|---|---|
| 1 | 2.8 |
| 2 | 3.4 |
| 3 | 4.0 |
| 4 | 4.6 |
| 5 | 5.2 |

Comparando con las notas reales (`2, 4, 5, 4, 5`), la recta se acerca pero no acierta exacto en ningún caso — eso es normal y esperable.

## R²: un puntaje de qué tan buena es la recta

`R²` es un número entre `0` y `1` (a veces se muestra como porcentaje, de `0%` a `100%`) que dice qué tan bien la recta explica los datos:

- `R² = 0` (o `0%`): la recta no ayuda nada a adivinar mejor que simplemente decir siempre el promedio.
- `R² = 1` (o `100%`): la recta adivina perfecto, pasando exactamente por todos los puntos.
- Cuanto más cerca de `1`, mejor explica la recta la relación entre `x` e `y`.

Para el ejemplo de las notas, `R² = 0.6` (`60%`): la cantidad de horas estudiadas explica el `60%` de por qué varían las notas entre los estudiantes; el `40%` restante depende de otras cosas que la recta no tiene en cuenta (por ejemplo, cuánto entendió cada uno en clase).

### Cómo se calcula (para quien tenga curiosidad)

```
variación total de las notas = suma de (cada nota real − promedio de las notas) al cuadrado
variación que explica la recta = suma de (cada nota adivinada − promedio de las notas) al cuadrado

R² = variación que explica la recta / variación total de las notas
```

Con los números del ejemplo: variación total = `6`, variación que explica la recta = `3.6`, entonces `R² = 3.6 / 6 = 0.6`.

## El mismo ejemplo, hecho por la computadora con `statsmodels`

Todo lo anterior es exactamente lo que calcula `statsmodels` por dentro. El siguiente código llega al mismo resultado (`número base = 2.2`, `cuánto sube por hora = 0.6`, `R² = 0.6`) sin necesidad de hacer las cuentas a mano:

```python
import pandas as pd
import statsmodels.api as sm

datos = pd.DataFrame({
    'horas_estudio': [1, 2, 3, 4, 5],
    'nota': [2, 4, 5, 4, 5],
})

y = datos['nota']
x = sm.add_constant(datos['horas_estudio'])  # agrega la columna del "número base"

modelo = sm.OLS(y, x).fit()

print(modelo.params)
# const             2.2   -> el número base (β0)
# horas_estudio     0.6   -> cuánto sube por hora (β1)

print(modelo.rsquared)
# 0.6   -> R²
```

## Visualización con matplotlib y seaborn

### Paso a paso: puntos + recta

El enfoque documentado en [Gráficos de dispersión y línea](../../matplotbit/01-Graficos/graficos_de_dispersion_y_linea.md) dibuja los puntos reales con `sns.scatterplot()` y, encima, la recta adivinada con `sns.lineplot()`:

```python
import seaborn as sns
import matplotlib.pyplot as plt

x_horas = datos['horas_estudio']
y_nota = datos['nota']
y_pred = modelo.predict(x)   # las notas que adivina la recta

plt.figure(figsize=(6, 4), tight_layout=True)

sns.scatterplot(x=x_horas, y=y_nota)       # los puntos reales
sns.lineplot(x=x_horas, y=y_pred, color='red')  # la recta adivinada

plt.xlabel('Horas de estudio')
plt.ylabel('Nota del examen')
plt.savefig('regresion_horas_nota')
plt.show()
```

### Atajo: `sns.regplot()`

`seaborn` tiene una función que dibuja los puntos y calcula la recta ella sola, sin necesidad de armar el modelo con `statsmodels` primero.

#### Sintaxis

```python
sns.regplot(x=x, y=y, data=None, ci=95, scatter_kws=None, line_kws=None)
```

#### Parámetros

- `x`, `y`: los datos a graficar (pueden ser columnas de un `DataFrame`, o directamente el nombre de la columna si se usa `data`).
- `data` (opcional): el `DataFrame` del que se toman `x` e `y` cuando se pasan como nombres de columna (texto).
- `ci` (opcional): una banda sombreada alrededor de la recta que muestra el margen de confianza; se puede desactivar con `ci=None`.
- `scatter_kws` / `line_kws` (opcional): para cambiar el color u otros detalles de los puntos y de la línea por separado.

#### Ejemplo

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4), tight_layout=True)

sns.regplot(x='horas_estudio', y='nota', data=datos, ci=95,
            scatter_kws={'color': 'steelblue'},
            line_kws={'color': 'red'})

plt.xlabel('Horas de estudio')
plt.ylabel('Nota del examen')
plt.show()
```

#### Consideraciones

- `sns.regplot()` calcula su propia recta por dentro; no usa el modelo ya ajustado con `statsmodels`. Para ver el resumen completo (`R²`, si el resultado es confiable estadísticamente, etc.) sigue haciendo falta `statsmodels`; `regplot()` sirve para un vistazo rápido.
- `sns.lmplot()` hace algo parecido a `regplot()`, pero permite separar el gráfico en varios subgráficos según una tercera columna (por ejemplo, un gráfico por curso).

## Glosario rápido (para volver a consultar)

| Símbolo | Se lee | Significa |
|---|---|---|
| `y` | y | Lo que se quiere adivinar |
| `x` | equis | El dato conocido, usado para adivinar |
| `ŷ` | y con sombrerito | Lo que adivina la recta |
| `β0` | beta cero | Número base (nota con 0 horas de estudio) |
| `β1` | beta uno | Cuánto sube por cada hora |
| `ε` | épsilon | El error (real menos adivinado) |
| `Σ` | sigma | "Sumá todos estos números" |
| `x̄`, `ȳ` | equis/y testada | El promedio de `x` o de `y` |
| `R²` | erre cuadrado | Puntaje de `0` a `1` de qué tan buena es la recta |

## Conceptos relacionados

- [Regresión lineal sobre datos de Pandas](./regresion_lineal.md)
- [Gráficos de dispersión y línea](../../matplotbit/01-Graficos/graficos_de_dispersion_y_linea.md)
- [Visualización de DataFrames](../06-Visualizacion/visualizacion_de_dataframes.md)
