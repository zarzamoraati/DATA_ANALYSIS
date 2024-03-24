## CLASES

# class Rectangulo:
#     def __init__(self, ancho,alto):
#         self.ancho=ancho
#         self.alto=alto

#     def calcular_area(self):
#         return print(self.ancho*self.alto/2)
#     def calcular_perimetro(self):
#         return print(2*(self.ancho*self.alto))


# my_rectangle=Rectangulo(12,9)
# my_rectangle.calcular_area()
# my_rectangle.calcular_perimetro()


class Figure:
    def __init__(self,tipo):
        self.type:tipo


class Rectangulo(Figure):
    def __init__(self,base,altura,tipo):
        super().__init__(tipo)
        self.__base=base
        self.__altura=altura
    def get_area(self):
        return self.__base*self.__altura

class Triangulo(Figure):
    def __init__(self,base,altura,tipo):
        super().__init__(tipo)
        self.__base=base
        self.__altura=altura
    def get_area(self):
        return (self.__base*self.__altura)/2

rectangulo=Rectangulo(12,10,"rectangulo")
triangulo=Triangulo(10,9,"triangulo")
print(rectangulo.get_area())
print(triangulo.get_area())     
# class CuentaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular=titular
#         self.saldo=saldo

#     def depositar(self,monto):
#         self.saldo+=monto
#     def retirar(self,monto):
#         if(self.saldo==0):
#             print("No cuenta con saldo en su cuenta")
#         if(self.saldo>=monto):
#             self.saldo-=monto
#         else:
#             print("Saldo insuficiente")
#     def consultarSaldo(self):
#         return print("Su saldo actual es de: $" ,self.saldo)
    
###
try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")
 