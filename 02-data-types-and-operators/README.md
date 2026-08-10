
# Tipos de datos

Los tipos de datos en Python son categorías de valores que determinan qué tipo de operaciones se pueden realizar con ellos.Podemos ver que tipo de dato estamos utilizando con la función type().

```python
print(type(5))        # <class 'int'>
```

## Números

Tipos de datos numéricos en Python:

- Numeros **Enteros** (int): números sin parte decimal, como 1, 100, -5.
- Números **Flotantes** (float): números con parte decimal, como 3.14
- Numeros **Complejos** (complex): números con parte real e imaginaria, como 2 + 3j.

```python
# Ejemplos de números
int_num = 10        # Entero
float_num = 3.14    # Flotante
complex_num = 2 + 3j # Complejo
```


## Strings

Los strings (o cadenas de texto) en Python son secuencias de caracteres encerradas en comillas simples o dobles.

```python
# Ejemplos de strings
single_quote_string = 'Hola, mundo!'
double_quote_string = "Hola, mundo!"
multi_line_string = '''Este es un string
de varias líneas.'''
format_string = f'Hola, {single_quote_string}' #Esto permite insertar variables dentro de un string usando f-strings.
```

## Logicos (Booleanos)

Los valores booleanos en Python son `True` y `False`. Se utilizan para representar la verdad o falsedad de una condición.

```python
# Ejemplos de booleanos
is_true = True
is_false = False
```

## Operadores

Los operadores en Python son símbolos que realizan operaciones sobre valores y variables. Algunos de los operadores más comunes incluyen:

- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Operadores de comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Operadores lógicos**: `and`, `or`, `not`

```python
# Ejemplos de operaciones aritméticas
# Definimos dos variables

a = 3 # a es una variable y 3 es un tipo de dato entero
b = 2 # b es una variable y 2 es un tipo de dato entero

sum = a + b
resta = a - b
producto = a * b
division = a / b
resto = a % b 
cociente = a // b
potencia = a ** b 


print(sum) 
print('a + b = ', sum)
print('a - b = ', resta)
print('a * b = ', producto)
print('a / b = ', division)
print('a % b = ', resto)
print('a // b = ', cociente)
print('a ** b = ', potencia)
```

```python
# Ejemplos de operadores de comparación
x = 5
y = 3

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```

```python
# Ejemplos de operadores lógicos
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)     # False
```

```Python
# Ejemplos con Strings
string1 = "Hola"
string2 = "Mundo"

# Concatenación de strings
concatenacion = string1 + " " + string2
print(concatenacion)  # Hola Mundo

# Repetición de strings
repeticion = string1 * 3
print(repeticion)  # HolaHolaHola

# Comparación de strings
print(string1 == string2)  # False

# Comparación de strings (case-sensitive)
print(string1.lower() == string2.lower())  # False
```

## Casteo de tipos

El casteo de tipos (type casting) es el proceso de convertir un valor de un tipo de dato a otro. En Python, podemos realizar el casteo utilizando las funciones `int()`, `float()`, `str()`, entre otras.

```python
# Ejemplos de casteo de tipos
# Convertir un entero a flotante
a = 5
b = float(a)
print(b)  # 5.0

# Convertir un flotante a entero
c = 3.14
d = int(c)
print(d)  # 3

# Convertir un número a string
e = 10
f = str(e)
print(f)  # "10"
```
