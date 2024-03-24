def Calculadora():
    def suma(num1,num2):
        return num1+num2
    def dividir(num1,num2):
        return num1/num2
    def producto(num1,num2):
        return num1*num2
    utils={
        "suma":suma,
        "division":dividir,
        "producto":producto
    }     
    return utils   



my_calc=Calculadora()

for key in my_calc.keys():
    print(my_calc[key](12,10))


class Auto:
    def __init__(self,model,brand):
        self.__model=model
        self.__brand=brand
    def get_auto(self):
        print(f"Auto de la marca {self.__brand} y modelo {self.__model} esta listo")

class Moto:
    def __init__(self,model,brand):
        self.__model=model
        self.__brand=brand
    def get_moto(self):
        print(f"Auto de la marca {self.__brand} y modelo {self.__model} esta listo")

def crear_vehiculo(tipo,model,brand):
    if tipo=="auto":
        return Auto(model,brand)
    elif tipo=="moto":
        return Moto(model,brand)
    else:
        print(f"El tipo {tipo} no existe en la fabrica")
    

mi_vehicle1=crear_vehiculo("auto","x-100","ford")
mi_vehicle2=crear_vehiculo("moto","99-cobra","susuki")
mi_vehicle1.get_auto()
mi_vehicle2.get_moto()












# def crear_calculadora():
#     def suma(a, b):
#         return a + b

#     def resta(a, b):
#         return a - b

#     def multiplicacion(a, b):
#         return a * b

#     def division(a, b):
#         return a / b

#     calculadora = {
#         'suma': suma,
#         'resta': resta,
#         'multiplicacion': multiplicacion,
#         'division': division
#     }

#     return calculadora

# mi_calculadora = crear_calculadora()

# resultado_suma = mi_calculadora['suma'](5, 3)
# resultado_resta = mi_calculadora['resta'](5, 3)
# resultado_multiplicacion = mi_calculadora['multiplicacion'](5, 3)
# resultado_division = mi_calculadora['division'](5, 3)

# print(resultado_suma)              # Resultado: 8
# print(resultado_resta)             # Resultado: 2
# print(resultado_multiplicacion)    # Resultado: 15
# print(resultado_division)          # Resultado: 1.6666666666666667



# Ejercicio 1: Función fábrica para crear objetos de diferentes tipos

# python
# Copy code
# class Auto:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     def mostrar_info(self):
#         print(f"Auto: {self.marca} {self.modelo}")

# class Moto:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     def mostrar_info(self):
#         print(f"Moto: {self.marca} {self.modelo}")

# def crear_vehiculo(tipo, marca, modelo):
#     if tipo == "auto":
#         return Auto(marca, modelo)
#     elif tipo == "moto":
#         return Moto(marca, modelo)
#     else:
#         raise ValueError("Tipo de vehículo no válido")

# vehiculo1 = crear_vehiculo("auto", "Toyota", "Corolla")
# vehiculo2 = crear_vehiculo("moto", "Honda", "CBR")

# vehiculo1.mostrar_info()
# vehiculo2.mostrar_info()
# En este ejemplo, la función crear_vehiculo() es una función fábrica que crea objetos de diferentes tipos de vehículos (en este caso, Auto y Moto) según el parámetro "tipo" especificado. Dependiendo del tipo proporcionado, la función crea y devuelve una instancia del objeto correspondiente.