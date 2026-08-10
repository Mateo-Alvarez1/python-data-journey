
# Variables

Las variables son contenedores que almacenan datos en un espacio en memoria del ordenador. Permiten guardar y manipular información de manera dinámica durante la ejecución de un programa.

Reglas para nombrar variables en Python:

1. Los nombres de las variables deben comenzar con una letra (a-z, A-Z)
2. Pueden contener letras, números y guiones bajos (_)
3. No pueden comenzar con un número
4. Son sensibles a mayúsculas y minúsculas (por ejemplo, `miVariable` y `mivariable` son diferentes)

Ejemplos de declaración de variables en Python:

```python
# Declaración de variables
nombre = "Juan"  # Variable de tipo cadena (string)
edad = 25        # Variable de tipo entero (int)
altura = 1.75    # Variable de tipo flotante (float)
```

Formas NO válidas de declarar variables:

```python
# Nombres de variables no válidos
first-name
first@name
first$name
num-1
```

En Python generalmente se usa la convencion Snake Case para nombrar variables, es decir, se utilizan letras minúsculas y se separan las palabras con guiones bajos (_). Por ejemplo: `mi_variable`, `edad_usuario`, `altura_promedio`.

Ejemplos de uso de variables:

```python
# Variables en Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

Declaración de múltiples variables en una línea

```python
# Declaración de múltiples variables en una línea
name, age, country = 'Asabeneh', 250, 'Finland'
```

Podemos usar input() para obtener datos del usuario y almacenarlos en variables:

```python
# Obtener datos del usuario
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Your first name is', first_name)
print('Your last name is', last_name)
```
