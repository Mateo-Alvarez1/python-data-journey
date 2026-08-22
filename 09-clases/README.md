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

La ``Herencia``a es el proceso mediante el cual se puede crear una clase ``hija`` que hereda de una clase ``padre``, compartiendo sus metodos y atributos. Ademas de ello una clase `hija` puede sobreescribir los metodos o atributos, o incluso definir unos nuevos

Se puede crear una clase hija con tan solo pasar como parametro la clase de la que queremos heredar.

```python
#Clase Padre
class Animal:
    pass
#Clase Hija que hereda de la padre 
class Perro(Animal):
    pass
```

Con el siguiente metodo podemos ver que clases en concreto descienden de ``Animal``

```python
print(Animal.__subclasses__())
# [<class '__main__.Perro'>]
```

> ¿Para que queremos la Herencia?

Dado que una clase hija hereda los atributos y metodos de la clase padre, nos puede ser muy util cuando tengamos clases que se parecen entre si pero tienen ciertas particularidades. En este caso en vez de definir un monton de clases para cada animal, podemos tomar los elementos comunes y crear una clase `Animal` de la que heredan el resto, respetando la filosofia **DRY**

## Extendiendo Y Modificando Metodos
Continuemos con nuestro ejemplo de perros y animales. Vamos a definir una clase padre `Animal` que tendra todos los atributos y metodos genericos.

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
```

Ahora creamos la clase `Perro` que va a heredar de `Animal`

```python
# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro
```

## Uso del Super

La funcion `Super` lo que nos permite es acceder a los metodos de la clase padre desde una de sus hijas. Volvamos al ejemplo de `Animal` y `Perro` 

```python
   class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad        
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__) 
```

> Tal vez queramos que nuestro perro tenga un parametro extra en el contructor, como podria ser el Dueño. Tenemos dos alternativas para hacer esto

- Podemos crear un nuevos `__init__` y guardar todas las varibales una a una
- O podemos usar `super()` para llamar a `__init__` de la clase padre que ya acepta la `especie` y `edad` y solo asignar la variable nueva manualmente

```python
class Ave():
    def __init__(self):
        self.volador = "volador"
    
    def vuela(self):
        print("Vuela ave")
        
class Pato(Ave):
    
    def __init__(self):
        super().__init__() # llama al constructor de la clase padre para poder acceder a los atributos de la clase padre
        self.nada = "nadando"
    
    def vuela(self):
        super().vuela() # llama al metodo de la clase padre para poder acceder a los metodos de la clase padre
        print("vuela pato")
        

pato = Pato()
pato.vuela()
print(pato.nada, pato.volador)
```

Podemos ver en este caso como se llama a ``super()`` en el constructor y se lo llama en el metodo `vuela` para sobreescribirlo

## Herencia Mutliple

En Python es posible realizar **Herencia Multiple**, la misma significa que una clase **hereda de varias clases** padre en vez de una sola

Ejemplo

```python
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass
```

Otra forma de hacerlo es la siguiente

```python
class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass
```

Llegados a este punto nos podemos plantear lo siguiente. Vale, como sabemos de otros posts las clases hijas heredan los métodos de las clases padre, pero también pueden reimplementarlos de manera distinta. Entonces, si llamo a un método que todas las clases tienen en común ¿a cuál se llama?. Pues bien, existe una forma de saberlo.

La forma de saber a que método se llama es consultar el **MRO** o **Method Order Resolution**. Esta función nos devuelve una tupla con el orden de búsqueda de los métodos. Como era de esperar se empieza en la propia clase y se va subiendo hasta la clase padre, de izquierda a derecha.

```python
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass

print(Clase3.__mro__)
# (<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class 'object'>)
```

Una curiosidad es que al final del todo vemos la clase ``object``. Aunque pueda parecer raro, es correcto ya que en realidad todas las clases en Python heredan de una clase genérica ``object``, aunque no lo especifiquemos explícitamente.`

> OJO! POR QUE LA HERENCIA MULTIPLE NO SIEMPRE ES BUENO USARLA Y ACA VAN ALGUNOS MOTIVOS

- **Problema del diamante (diamond problem)**. Si dos clases padre heredan de una misma clase base y ambas sobreescriben un método, la clase hija queda con ambigüedad sobre cuál versión usar. Python lo resuelve con el MRO (Method Resolution Order, algoritmo C3), pero el resultado no siempre es intuitivo a simple vista.

- Cuando una clase hereda de 3-4 clases padre, saber de dónde viene un método o atributo específico deja de ser evidente con solo mirar el código — hay que revisar el MRO completo ``(D.__mro__)``

- **Acoplamiento fuerte (fragile base class problem)**. Un cambio en una clase padre puede romper el comportamiento de la clase hija de forma inesperada, y ese efecto es más difícil de prever cuantas más clases padre hay involucradas

- **Colisión de nombres**. Si dos clases padre definen atributos o métodos con el mismo nombre pero distinto propósito, se puede generar comportamiento inconsistente sin que salte ningún error.

- **Mantenibilidad a largo plazo**. Jerarquías de herencia múltiple complejas son más difíciles de testear, refactorizar y entender para alguien que se suma al proyecto después.

## Clases Abstractas -> Volver a ver clase

## Polimorfismo

El Polimorfismo es uno de los pilares basicos de la POO. El mismo tiene origen en *poly* (muchos) *morfo* (formas) y aplicado a la programacion hace referencia a que los objetos pueden tomar diferentes formas.

¿Que quiere decir esto?
Que muchos objetos pueden ser accedidos utilizando la misma interfaz, pero cada uno se va a comportar de acuerto a su propia naturaleza.

Al ser un lenguaje con tipado dinámico y permitir duck typing, en Python no es necesario que los objetos compartan un interfaz, simplemente basta con que tengan los métodos que se quieren llamar.

Explicado en criollo, el polimorfismo es:

> La capacidad que tienen los objetos de comportarse de a cuerdo a su propia naturaleza cuando son accedidos mediante una misma interfaz.

```python
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass
        
class Usuario(Model):
    def guardar(self):
        print("Guardar en la db")
    
 
    
class Sesion(Model):
    def guardar(self):
        print("Guardar en el disco")
        
        
        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
    
    
usuario = Usuario()
sesion = Sesion()

guardar([usuario, sesion])
```
