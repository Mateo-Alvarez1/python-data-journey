# ============================================================
# 🐍 PYTHON - TIPOS DE DATOS Y OPERADORES
# ============================================================
#
# Ejercicios prácticos con:
# - Tipos de datos
# - type()
# - Números
# - Strings
# - Booleanos
# - Operadores aritméticos
# - Operadores de comparación
# - Operadores lógicos
# - F-strings
#
# ============================================================


# ============================================================
# 🟢 NIVEL 1 - TIPOS DE DATOS
# ============================================================

# EJERCICIO 1
# Utilizá la función type() para mostrar el tipo de dato
# de los siguientes valores:
#
# 10
# 3.14
# "Python"
# True


print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))


# ------------------------------------------------------------
# EJERCICIO 2
# ------------------------------------------------------------
# Creá cuatro variables utilizando diferentes tipos de datos:
#
# nombre → string
# edad → int
# altura → float
# es_estudiante → bool
#
# Después mostrá el valor y el tipo de dato de cada variable.


nombre = "Olivia"
edad = 25
altura = 1.75
es_estudiante = True

print(nombre, type(nombre))
print(edad, type(edad))
print(altura, type(altura))
print(es_estudiante, type(es_estudiante))


# ------------------------------------------------------------
# EJERCICIO 3
# ------------------------------------------------------------
# Creá una variable llamada numero_complejo con el valor
# 2 + 3j.
#
# Mostrá su valor y su tipo de dato.


numero_complejo = 2 + 3j

print(numero_complejo)
print(type(numero_complejo))


# ============================================================
# 🟢 NIVEL 2 - OPERADORES ARITMÉTICOS
# ============================================================

# EJERCICIO 4
# Creá dos variables:
#
# a = 20
# b = 6
#
# Calculá:
#
# - Suma
# - Resta
# - Multiplicación
# - División
#
# Mostrá todos los resultados.


a = 20
b = 6

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


# ------------------------------------------------------------
# EJERCICIO 5
# ------------------------------------------------------------
# Utilizando las variables del ejercicio anterior, calculá:
#
# - El resto de la división.
# - El cociente entero.
# - La potencia de a elevado a b.


resto = a % b
cociente = a // b
potencia = a ** b

print("Resto:", resto)
print("Cociente:", cociente)
print("Potencia:", potencia)


# ------------------------------------------------------------
# EJERCICIO 6
# ------------------------------------------------------------
# Una persona compra 5 productos que cuestan $2500 cada uno.
#
# Creá las variables necesarias y calculá el precio total.


precio = 2500
cantidad = 5

total = precio * cantidad

print("Precio total:", total)


# ------------------------------------------------------------
# EJERCICIO 7
# ------------------------------------------------------------
# Una persona tiene $100.000 y realiza los siguientes gastos:
#
# Comida: $25.000
# Transporte: $10.000
# Entretenimiento: $15.000
#
# Calculá cuánto dinero le queda.


dinero = 100000

comida = 25000
transporte = 10000
entretenimiento = 15000

gastos_totales = comida + transporte + entretenimiento
dinero_restante = dinero - gastos_totales

print("Gastos totales:", gastos_totales)
print("Dinero restante:", dinero_restante)


# ============================================================
# 🟡 NIVEL 3 - OPERADORES DE COMPARACIÓN
# ============================================================

# EJERCICIO 8
# Creá una variable llamada edad con el valor 20.
#
# Comprobá:
#
# - Si la edad es exactamente 20.
# - Si es mayor a 18.
# - Si es menor a 18.
# - Si es mayor o igual a 18.


edad = 20

print("¿Tiene 20 años?", edad == 20)
print("¿Es mayor a 18?", edad > 18)
print("¿Es menor a 18?", edad < 18)
print("¿Es mayor o igual a 18?", edad >= 18)


# ------------------------------------------------------------
# EJERCICIO 9
# ------------------------------------------------------------
# Creá dos variables:
#
# precio_1 = 5000
# precio_2 = 7500
#
# Comprobá:
#
# - Si tienen el mismo precio.
# - Si son diferentes.
# - Si precio_1 es mayor que precio_2.
# - Si precio_1 es menor que precio_2.


precio_1 = 5000
precio_2 = 7500

print("¿Son iguales?", precio_1 == precio_2)
print("¿Son diferentes?", precio_1 != precio_2)
print("¿Precio 1 es mayor?", precio_1 > precio_2)
print("¿Precio 1 es menor?", precio_1 < precio_2)


# ------------------------------------------------------------
# EJERCICIO 10
# ------------------------------------------------------------
# Una tienda tiene 15 productos en stock.
#
# Comprobá:
#
# - Si hay productos disponibles.
# - Si hay al menos 10 productos.
# - Si el stock está agotado.


stock = 15

print("¿Hay productos?", stock > 0)
print("¿Hay al menos 10?", stock >= 10)
print("¿Está agotado?", stock == 0)


# ============================================================
# 🟡 NIVEL 4 - OPERADORES LÓGICOS
# ============================================================

# EJERCICIO 11
# Una persona puede conducir si:
#
# - Es mayor de 18 años.
# - Tiene licencia.
#
# Creá:
#
# edad = 25
# tiene_licencia = True
#
# Utilizá el operador AND para comprobar si puede conducir.


edad = 25
tiene_licencia = True

puede_conducir = edad >= 18 and tiene_licencia

print("¿Puede conducir?", puede_conducir)


# ------------------------------------------------------------
# EJERCICIO 12
# ------------------------------------------------------------
# Una persona puede realizar una compra si:
#
# - Tiene dinero.
# O
# - Tiene tarjeta.
#
# Creá:
#
# tiene_dinero = False
# tiene_tarjeta = True
#
# Utilizá OR para comprobar si puede comprar.


tiene_dinero = False
tiene_tarjeta = True

puede_comprar = tiene_dinero or tiene_tarjeta

print("¿Puede comprar?", puede_comprar)


# ------------------------------------------------------------
# EJERCICIO 13
# ------------------------------------------------------------
# Creá una variable:
#
# usuario_bloqueado = False
#
# Utilizá NOT para obtener el valor contrario.


usuario_bloqueado = False

usuario_activo = not usuario_bloqueado

print("¿Usuario activo?", usuario_activo)


# ============================================================
# 🟠 NIVEL 5 - STRINGS
# ============================================================

# EJERCICIO 14
# Creá dos variables:
#
# palabra_1 = "Hola"
# palabra_2 = "Mundo"
#
# Concatená ambas variables para obtener:
#
# Hola Mundo


palabra_1 = "Hola"
palabra_2 = "Mundo"

resultado = palabra_1 + " " + palabra_2

print(resultado)


# ------------------------------------------------------------
# EJERCICIO 15
# ------------------------------------------------------------
# Creá una variable llamada palabra con el valor "Python".
#
# Repetí la palabra 3 veces utilizando el operador *.


palabra = "Python"

resultado = palabra * 3

print(resultado)


# ------------------------------------------------------------
# EJERCICIO 16
# ------------------------------------------------------------
# Creá dos variables:
#
# palabra_1 = "Python"
# palabra_2 = "Python"
#
# Comprobá si ambas variables contienen el mismo texto.


palabra_1 = "Python"
palabra_2 = "Python"

print(palabra_1 == palabra_2)


# ------------------------------------------------------------
# EJERCICIO 17
# ------------------------------------------------------------
# Creá:
#
# lenguaje = "Python"
#
# Comprobá si:
#
# lenguaje == "python"
#
# Después utilizá .lower() para realizar una comparación
# que no dependa de mayúsculas y minúsculas.


lenguaje = "Python"

print(lenguaje == "python")

print(lenguaje.lower() == "python")


# ============================================================
# 🟠 NIVEL 6 - F-STRINGS
# ============================================================

# EJERCICIO 18
# Creá las siguientes variables:
#
# nombre = "Mateo"
# edad = 23
# ciudad = "San Juan"
#
# Utilizá un f-string para mostrar:
#
# Hola, soy Mateo, tengo 23 años y vivo en San Juan.


nombre = "Mateo"
edad = 23
ciudad = "San Juan"

print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}.")


# ------------------------------------------------------------
# EJERCICIO 19
# ------------------------------------------------------------
# Una tienda vende:
#
# producto = "Notebook"
# precio = 750000
# cantidad = 2
#
# Calculá el precio total.
#
# Mostrá:
#
# Compraste 2 Notebook por un total de $1500000.


producto = "Notebook"
precio = 750000
cantidad = 2

total = precio * cantidad

print(f"Compraste {cantidad} {producto} por un total de ${total}.")


# ============================================================
# 🔴 NIVEL 7 - DESAFÍOS
# ============================================================

# EJERCICIO 20
# Una persona tiene:
#
# salario = 800000
# gastos = 650000
#
# Calculá cuánto dinero le queda.
#
# Después comprobá si le quedan más de $100000.


salario = 800000
gastos = 650000

dinero_restante = salario - gastos

print("Dinero restante:", dinero_restante)
print("¿Le quedan más de $100000?", dinero_restante > 100000)


# ------------------------------------------------------------
# EJERCICIO 21
# ------------------------------------------------------------
# Una empresa tiene:
#
# 25 empleados.
# Cada empleado gana $500000.
#
# Calculá cuánto dinero necesita la empresa para pagar
# todos los salarios.


empleados = 25
salario_promedio = 500000

costo_total = empleados * salario_promedio

print("Costo total de salarios:", costo_total)


# ------------------------------------------------------------
# EJERCICIO 22
# ------------------------------------------------------------
# Una tienda vende un producto a $50000.
#
# Tiene un descuento del 15%.
#
# Calculá:
#
# 1. El monto del descuento.
# 2. El precio final.


precio = 50000
descuento = 15

monto_descuento = precio * descuento / 100
precio_final = precio - monto_descuento

print("Descuento:", monto_descuento)
print("Precio final:", precio_final)


# ------------------------------------------------------------
# EJERCICIO 23
# ------------------------------------------------------------
# Una persona compra:
#
# 2 pizzas de $12000.
# 3 empanadas de $1500.
# 2 bebidas de $2500.
#
# Calculá el total de la compra.
#
# Después comprobá si el total supera los $40000.


precio_pizza = 12000
cantidad_pizzas = 2

precio_empanada = 1500
cantidad_empanadas = 3

precio_bebida = 2500
cantidad_bebidas = 2

total_pizzas = precio_pizza * cantidad_pizzas
total_empanadas = precio_empanada * cantidad_empanadas
total_bebidas = precio_bebida * cantidad_bebidas

total = total_pizzas + total_empanadas + total_bebidas

print("Total:", total)
print("¿Supera los $40000?", total > 40000)


# ============================================================
# 🏆 DESAFÍO FINAL
# ============================================================

# EJERCICIO 24
# Creá un pequeño perfil utilizando diferentes tipos de datos.
#
# El perfil debe contener:
#
# - Nombre
# - Edad
# - Altura
# - Ciudad
# - Salario
# - Tiene trabajo
#
# Después:
#
# 1. Mostrá todos los datos.
# 2. Mostrá el tipo de dato de cada variable.
# 3. Calculá cuánto gana por día suponiendo 30 días.
# 4. Comprobá si gana más de $500000.
# 5. Mostrá la información utilizando f-strings.


nombre = "Mateo"
edad = 23
altura = 1.83
ciudad = "San Juan"
salario = 800000
tiene_trabajo = True

salario_diario = salario // 30
gana_mas_de_500000 = salario > 500000

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"Ciudad: {ciudad}")
print(f"Salario: ${salario}")
print(f"Tiene trabajo: {tiene_trabajo}")
print(f"Salario diario: ${salario_diario}")
print(f"¿Gana más de $500000?: {gana_mas_de_500000}")

print("\nTipos de datos:")

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(ciudad))
print(type(salario))
print(type(tiene_trabajo))