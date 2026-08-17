# Creando Excepciones personalizadas

class MiError(Exception):
#* Esta clase es para representar mi error

    def __init__ (self,mensaje,codigo):
        self.mensaje = mensaje
        self.codigo = codigo
            
    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"

    try:
        n1 = int(input("Escribe el primer numero: "))
        n1 = int(input("Escribe el segundo numero: "))

#* TIPOS DE EXCEPCIONES
    except ValueError as e: 
        print("Ingresa una valor que corresponda") # PODEMOS PRINTEAR LA EXCEPCION EN ESPECIFICO PARA OBTENER EL VALOR CONCRETO Y DESPUES LE PASAMOS ESA EXCEPCION ESPECIFICA
    finally:
        print('se ejecuta siempre') # Lo vamos a usar independientemente si vamos a tener exito en un bloque de try/catch
     
#* Lanzando excepciones 

def division(n=0):
    if n == 0:
        raise MiError('No se puede dividir por 0' , 777)
    return 5/n

try:
    division()
except MiError as e:
    print(e)

