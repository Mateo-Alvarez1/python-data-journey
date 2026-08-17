# Funciones

Las funciones son bloques de codigo reutilizables que se usan para hacer una tarea especifica.Se crean a partir de la palabra reservada `def` 

```python
    def nombre_funcion(argumentos):
    código
    return retorno
```

Cualquier funcion tendra un **nombre**, unos **argumentos de entrada**, un **codigo** a ejecutar y unos **parametros de salida*.

```python
def f(x):
    return 2*x
y = f(3)
print(y) # 6
```

## Principios

- **Reusabilidad**, la mejor solucion para evitar codigo repetido es utilizarlas.Ya que nos evita codigo repetido y seria ademas mas facil de modificar
- **Modularidad**, en vez de escribir largas piezas de codigo, es mejor crear modulos o funciones que agrupen ciertos fragmentos de codigos en funcionalidades especificas, haciendo que el codigo resulte mas facil de leer

## Argumentos Por Posicion
Los argumentos por **posición** o posicionales son la forma más básica e intuitiva de pasar parámetros. Si tenemos una función ``resta()`` que acepta dos parámetros, se puede llamar como se muestra a continuación.

```python
def resta(a, b):
    return a-b
resta(5, 3) # 2
```

## Argumentos Por Nombre

Otra forma de llamar a una función, es usando el nombre del argumento con = y su valor. El siguiente código hace lo mismo que el código anterior, con la diferencia de que los argumentos no son posicionales.

```python
resta(a=3, b=5) # -2
```

## Argumentos por defecto

Tal vez queramos tener una función con algún parámetro opcional, que pueda ser usado o no dependiendo de diferentes circunstancias. Para ello, lo que podemos hacer es asignar un valor **por defecto** a la función. En el siguiente caso c valdría cero salvo que se indique lo contrario.

```python
def suma(a, b, c=0):
    return a+b+c
suma(5,5,3) # 13
```

## Argumentos de longitud variable (*xargs y **keyargs)

- *xargs -> Te permite agrupar argumentos posicionales adicionales de forma de **tuplas**

```python
def suma(*numeros):
    resultado=0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,3,5)
```

- **kwargs -> Agrupa los argumentos con nombre (clave-valor) adicionales en forma de un diccionario

```python
def get_product(**datos):
    
    return datos["id"]
    
print(get_product(id="1",name="iphone"))  
```

## Sentencia Return

El uso de la sentencia ``return`` permite realizar dos cosas:

- Salir de la función y transferir la ejecución de vuelta a donde se realizó la llamada.
- Devolver uno o varios parámetros, fruto de la ejecución de la función.

En lo relativo a lo primero, una vez se llama a ``return`` se para la ejecución de la función y se vuelve o retorna al punto donde fue llamada. Es por ello por lo que el código que va después del ``return`` no es ejecutado en el siguiente ejemplo.

```python
def mi_funcion():
    print("Entra en mi_funcion")
    return
    print("No llega")
mi_funcion() # Entra en mi_funcion
```

## Anotaciones en funciones
Existe una funcionalidad relativamente reciente en Python llamada **function annotation** o anotaciones en funciones. Dicha funcionalidad nos permite añadir metadatos a las funciones, indicando los tipos esperados tanto de entrada como de salida.

```python
def multiplica_por_3(numero: int) -> int:
    return numero*3

multiplica_por_3(6) # 18
```

> Son muy utiles de cara a la documentacion del codigo