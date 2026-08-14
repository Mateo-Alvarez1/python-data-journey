# Condicionales

De no ser por las estructuras de control, el codigo en cualquier lenguaje de programacion seria ejecutado secuencialmente hasta terminar. Un codigo, no deja de ser un conjunto de instrucciones que son ejecutadas unas tras otras. Gracias a las estructuras de control nosotros podemos cambiar el flujo de ejecucion de un programa, haciendo que ciertos bloques de codigo se ejecuten si y solo si se dan unas condicioens

## Uso del If

Un ejemplo seria si tenemos dos valores `a` y `b` que queremos dividir. Antes de entrar en el bloque de codigo que divide `a/b`. Seria importante verificar que `b` es distinto de cero, ya que la division por cero no esta definida.Es aque donde entran los `if`.

```python
a = 4
b = 2
if b != 0:
    print(a/b)
```

En este ejemplo podemos ver como se puede usar un `if` en Python. Con el operador `!=` se comprueba que el número `b` sea distinto de cero, y si lo es, se ejecuta el código que está indentado. Por lo tanto un `if` tiene dos partes:

- La condicion que se tiene que cumplir para que el bloque de codigo se ejecute, es nuestro caso `b!=0`
- El bloque de codigo que se ejecutara si se cumple la condicion anterios

Es muy importante tener en cuenta que la sentencia if debe ir terminada por : y el bloque de código a ejecutar debe estar indentado.

```python
if b != 0:
    c = a/b
    d = c + 1
    print(d)
```

Se puede también combinar varias condiciones entre el if y los :. Por ejemplo, se puede requerir que un número sea mayor que 5 y además menor que 15. Tenemos en realidad tres operadores usados conjuntamente, que serán evaluados por separado hasta devolver el resultado final, que será True si la condición se cumple o False de lo contrario.

```python
a = 10
if a > 5 and a < 15:
    print("Mayor que 5 y menos que 15")
```

Si tenemos un `if` sin contenido, tal vez porque sea una tarea pendiente que estamos dejando para implementar en un futuro, es necesario hacer uso de `pass` para evitar el error. Realmente `pass` no hace nada, simplemente es para tener contento al interprete de código.

```python
if a > 5:
    pass
```

## Uso de Else y Elif

Es posible que no solo queramos hacer algo si una determinada condición se cumple, sino que además queramos hacer algo de lo contrario. Es aquí donde entra la cláusula `else`

```python
x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")
```

En muchos casos, podemos tener varias condiciones diferentes y para cada una queremos un código distinto. Es aquí donde entra en juego el ``elif``.

```python
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
```

Con la cláusula ``elif`` podemos ejecutar tantos bloques de código distintos como queramos según la condición.

## Operador Ternario

El operador ternario o ``ternary operator`` es una herramienta muy potente que muchos lenguajes de programación tienen. En Python es un poco distinto a lo que sería en C, pero el concepto es el mismo. Se trata de una cláusula ``if``,``else`` que se define en una sola línea y puede ser usado por ejemplo, dentro de un `print()`.

### Sintaxis

> [código si se cumple] if [condición] else [código si no se cumple]

```python
a = 10
b = 5
c = a/b if b!=0 else -1
print(c)
#2
```
