
###Implementa una clase Gato y Perrro que hereden del la clase animal 


class Animal:
    def __init__(self,especie,nombre):
        self.especie=especie
        self.nombre=nombre
    
    def animal_info(self):
        print(f"El animal {self.nombre} de la especie {self.especie}")
    def sonido(self):
        print("El animal esta emitieno un sonido...")

class Perro(Animal):
    def __init__(self,especie,nombre,raza,color):
        super().__init__(especie,nombre)
        self.raza=raza
        self.color=color
    def sonido(self):
        super().sonido()
        print("Guau Guau")
    def animal_info(self):
        super().animal_info()
        print(f"es de color {self.color} y pertenece al raza {self.raza}")

class Gato(Animal):
    def __init__(self,especie,nombre,raza,color):
        super().__init__(especie,nombre)
        self.raza=raza
        self.color=color

    def sonido(self):
        super().sonido()
        print("Miau Miau")
    def animal_info(self):
        super().animal_info()
        print(f"es de color {self.color} y pertenece a la raza {self.raza}")
        
perro=Perro("Canino","Firulais","Labrador","Oro")
gato=Gato("Felino","Garfield","Angora","Marron")


perro.sonido()
perro.animal_info()
















# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def comer(self):
#         print(f"{self.nombre} está comiendo.")

# class Perro(Animal):
#     def __init__(self, nombre, raza):
#         super().__init__(nombre)
#         self.raza = raza

#     def ladrar(self):
#         print("¡Guau! ¡Guau!")

# class Gato(Animal):
#     def __init__(self, nombre, color):
#         super().__init__(nombre)
#         self.color = color

#     def maullar(self):
#         print("¡Miau! ¡Miau!")

# # Crear instancias de las clases derivadas
# mi_perro = Perro("Firulais", "Labrador")
# mi_gato = Gato("Garfield", "Naranja")

# # Acceder a métodos de las clases base y derivadas
# mi_perro.comer()
# mi_perro.ladrar()

# mi_gato.comer()
# mi_gato.maullar()


# Ejemplo 2: Herencia múltiple

class Volador:
    def volar(self):
        print("Volando alto¡¡¡")     

class Nadador:
    def nadar(self):
        print("Nadando en el agua")

class Pato(Volador,Nadador):
    def hacer_sonido(self):
        print("Cuak Cuack¡¡¡")
    def pista(self):
        print("Adivina lo que soy...")
pato=Pato()
pato.volar()
pato.nadar()
pato.pista()
pato.hacer_sonido()


# class Volador:
#     def volar(self):
#         print("Volando alto.")

# class Nadador:
#     def nadar(self):
#         print("Nadando en el agua.")

# class Pato(Volador, Nadador):
#     def graznar(self):
#         print("¡Cuack! ¡Cuack!")

# mi_pato = Pato()
# mi_pato.volar()
# mi_pato.nadar()
# mi_pato.graznar()
# En este ejemplo, la clase Pato hereda de las clases Volador y Nadador, lo que se conoce como herencia múltiple. Esto significa que Pato puede acceder a los métodos volar de la clase Volador y nadar de la clase Nadador. Además, Pato también tiene su propio método graznar.