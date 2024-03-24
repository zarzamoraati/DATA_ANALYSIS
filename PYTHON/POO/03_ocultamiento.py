# Ejercicio 1: Ocultamiento de atributos
# En este ejemplo, la clase Persona tiene dos atributos privados, __nombre y __edad, que están ocultos. Estos atributos solo pueden ser accedidos indirectamente a través de los métodos obtener_nombre() y obtener_edad(). Además, la clase Persona tiene un método privado __saludar() que no puede ser accedido desde fuera de la clase.

# La clase Estudiante hereda de Persona y agrega su propio atributo privado __grado. También tiene un método presentarse() que llama al método privado __saludar() de la clase base


# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age

#     def __saludar(self):
#         print(f"Hello im {self.__name} ")  

#     def saludo(self):
#         self.__saludar()
    


# class Estudent(Person):
#         def __init__(self,grade,name,age):
#             super().__init__(name,age)
#             self.__grade=grade
#         def get_grade(self):
#             print(f"Soy un/a {self.__grade}")
#         def presentation(self):
#             self.saludo()
#             self.get_grade()
            
            

# person1=Estudent("bachiller","noemi",22)
# person1.presentation()

###Ocultamiento de metodos
# En este ejemplo, la clase Vehiculo tiene un método privado __revisar_motor() que no puede ser accedido desde fuera de la clase. Las clases derivadas, como Motocicleta, pueden utilizar este método privado en sus propios métodos, como acelerar() y frenar(). Los métodos ocultos se llaman dentro de la clase derivada, pero no se pueden acceder directamente desde fuera de la clase.







# class Persona:
#     def __init__(self, nombre, edad):
#         self.__nombre = nombre
#         self.__edad = edad

#     def obtener_nombre(self):
#         return self.__nombre

#     def obtener_edad(self):
#         return self.__edad

#     def __saludar(self):
#         print(f"Hola, mi nombre es {self.__nombre}.")

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.__grado = grado

#     def obtener_grado(self):
#         return self.__grado

#     def presentarse(self):
#         self.__saludar()
#         print(f"Soy un estudiante de {self.__grado}.")

# estudiante = Estudiante("Juan", 18, "11vo grado")
# print(estudiante.obtener_nombre())  # Acceso permitido mediante método
# print(estudiante.obtener_edad())    # Acceso permitido mediante método
# print(estudiante.obtener_grado())   # Acceso permitido mediante método
# estudiante.presentarse()            # Acceso permitido desde el método derivado



# En este ejemplo, la clase Persona tiene dos atributos privados, __nombre y __edad, que están ocultos. Estos atributos solo pueden ser accedidos indirectamente a través de los métodos obtener_nombre() y obtener_edad(). Además, la clase Persona tiene un método privado __saludar() que no puede ser accedido desde fuera de la clase.

# La clase Estudiante hereda de Persona y agrega su propio atributo privado __grado. También tiene un método presentarse() que llama al método privado __saludar() de la clase base.

# Ejercicio 2: Ocultamiento de métodos


# class Vehiculo:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     def acelerar(self):
#         print("Acelerando...")

#     def frenar(self):
#         print("Frenando...")

#     def __revisar_motor(self):
#         print("Revisando motor...")

# class Motocicleta(Vehiculo):
#     def __init__(self, marca, modelo):
#         super().__init__(marca, modelo)

#     def acelerar(self):
#         self.__revisar_motor()
#         print("Acelerando la motocicleta...")

#     def frenar(self):
#         self.__revisar_motor()
#         print("Frenando la motocicleta...")

# moto = Motocicleta("Honda", "CBR")
# moto.acelerar()  # Acceso permitido desde el método derivado
# moto.frenar()    # Acceso permitido desde el método derivado

# En este ejemplo, la clase Vehiculo tiene un método privado __revisar_motor() que no puede ser accedido desde fuera de la clase. Las clases derivadas, como Motocicleta, pueden utilizar este método privado en sus propios métodos, como acelerar() y frenar(). Los métodos ocultos se llaman dentro de la clase derivada, pero no se pueden acceder directamente desde fuera de la clase.