# Clases

Python es un lenguaje **Orientado a Objetos**. Todo en Python es un **objeto**, con sus *propiedades* y *metodos*.
Un Numero, una Cadena, lista, diccionario, tupla, etc. Utilizado en un programa es un **objeto de una clase incorporada** correspondiente.

> Creamos Clases para crear Objetos

Una **Clase** es como un constructor de Objetos, o un *"Molde"* como me gusta llamarle a mi para crear objetos.Donde la clase define **atributos** y el **comportamiento** del objeto, mientras que el objeto, representa la clase.

Cada Elemento de un programa Python es un objeto de una clase. Hagamos una comprobacion:

```python

>>> num = 10
>>> type(num)
<class 'int'>

>>> string = 'string'
>>> type(string)
<class 'str'>

>>> boolean = True
>>> type(boolean)
<class 'bool'>

>>> lst = []
>>> type(lst)
<class 'list'>

>>> tpl = ()
>>> type(tpl)
<class 'tuple'>

>>> set1 = set()
>>> type(set1)
<class 'set'>

>>> dct = {}
>>> type(dct)
<class 'dict'>
```

## Crear Una Clase

Para crear una clase necesitamos la palabra clave `class` seguido del nombre que le queremos asignar. El mismo debe estar en `CamelCase`.

```python
#Sintaxis
class ClassName:
    code goes here
```

Ejemplo

```python
class Person:
    pass
```

## Crear un Objeto

Podemos crear un **Objeto** a partir de esta clase definida

```python
p = Person()
print(p)
```

## Constructor

Una clase sin `constructor` no es realmente util debido a que el mismo lo que hace es permitir **inicializar los atributos y el estado inicial del objeto**

Python tiene incorporado el **metodo magico** `__init__` que tiene un *autoparametro* `self` que hace referencia a la instancia actual de la clase.

```python
class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name = name

p = Person('Asabeneh')
print(p.name)
print(p)
```

## Metodos de Objetos

Los objetos ademas de tener atributos tambien pueden tener Metodos, que hace referencia a las funcionalidades que va a tener ese objeto.

```python
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

## Decorador Property

El decorador `@property` es usado para modificar un metodo para que sea un atributo o propiedad. Se usa sobre un **metodo** y hara que funciones como **atributo**

El objetivo de este decorador esta relacionado con el concepto de **encapsulación** Este concepto indica que en determinadas ocasiones es importante **ocultar** el estado interno de los objetos al **exterior** para evitar que sean modificados de manera incorrecta

```python
class Perro:
    def __init__(self, nombre):
        self.__nombre = nombre


    @property #* Se usa para modificar una metodo para que se comporte como un atributo o propiedad
    def nombre(self):
        return self.__nombre
    
    
    @nombre.setter
    def nombre(self,nombre):
        if nombre.strip():
            self.__nombre = nombre
        return

perro = Perro("helo")
print(perro.nombre)
```

Lo que podemos ver aca es el uso de `__` en el atributo `nombre` esto se hace para decirle a python que vamos a trabajarlo como un atributo `privado` y que no pueda ser accedido como el resto de los atributos

Al definir la propiedad con ``@property`` el acceso a ese atributo se va a hacer a traves de una funcion.

```python
 @property
    def nombre(self):
        return self.__nombre
    
    
    @nombre.setter
    def nombre(self,nombre):
        if nombre.strip():
            self.__nombre = nombre
        return
```

## Metodos Magicos

Los **Metodos Magicos** son funciones especiale con *doble guion bajo al inicio y al final* ``(como __init__)``. No se llaman de forma directa, sino que python los ejecuta de manera automatica cuando ocurre una accion especifica.

Entre los distintos metodos magicos que existen tenemos

```python
    
    def __del__(self):
        print(f"chau perro {self.nombre}")    
        
    def __str__(self):  # Este te permite mostrar la clase de una forma mas amigable, en vez de mostrar la direccion de memoria
        return f"Clase de Perro: {self.nombre}"

perro = Perro("Chanchito", 7)
print(perro)
del perr
```

Tambien tenemos algunos metodos magicos de **comparacion**

```python
class Coordenadas:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon
        
    def __eq__(self, otro): # COMPARAR CLASES, TAMBIEN INTERPRETA O INFIERE EN EL __ne__ o (not equal)
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __lt__(self, otro): # MENOR QUE
        return self.lat + self.lon < otro.lat + otro.lon
        
    def __le__(self ,otro): # MENOR IGUAL
        return self.lat + self.lon <= otro.lat + otro.lon
    
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
print(coords <= coords2)
```

Podes ver todos los metodos magicos existente aca [Metodos Magicos](https://rszalski.github.io/magicmethods/#representations)

## Contenedores

Un contenedor es una clase que **almacena y organiza** instancias de otra clase, ofreciendo métodos para gestionarlas como grupo (agregar, eliminar, listar, filtrar) en vez de manejarlas una por una manualmente.

Ejemplo

```python
class Producto:
    def __init__ (self, nombre, precio):
        self.nombre = nombre
        self.precio = precio    
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio} "
    
    
    
class ``Categoria``:
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
        
    def addProducto(self, producto):
        self.productos.append(producto)
    
    def imprimir(self):
        for producto in self.productos:
            print(producto)
            
            
kayak = Producto("Kayak", 200)
Bici = Producto("Bici", 400)
deportes = Categoria("Deportes", [ kayak , Bici])
deportes.imprimir()
```

Acá, ``Categoria`` es el contenedor de ``Producto``. Cada ``Categoria`` tiene su propia lista interna ``(self.productos)``y expone métodos (``addProducto``, ``imprimir``) para interactuar con esa colección sin que el resto del código tenga que manipular la lista directamente.`

¿Por qué usar este patrón?

- Encapsula la lógica de la colección dentro de una sola clase.
- Si mañana cambiás cómo se almacenan los productos (lista → diccionario → base de datos), solo tocás ``Categoria``, no el resto del sistema.
- Da una interfaz clara: quien usa ``Categoria`` no necesita saber cómo está implementada la lista por dentro.

## Herencia
## Herencia Mutliple
## Clases Abstractas
## Polimorfismo 
