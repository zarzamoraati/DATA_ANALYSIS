#  Días de la semana
# Tu tarea es implementar una clase llamada Weeker. Sí, tus ojos no te engañan, este nombre proviene del hecho de que los objetos de esta clase podrán almacenar y manipular los días de la semana.

# El constructor de la clase acepta un argumento: una cadena. La cadena representa el nombre del día de la semana y los únicos valores aceptables deben provenir del siguiente conjunto:

# Lun Mar Mie Jue Vie Sab Dom

# Invocar al constructor con un argumento desde fuera de este conjunto debería generar la excepción WeekDayError (defínela tu mismo; no te preocupes, pronto hablaremos sobre la naturaleza objetiva de las excepciones). La clase debe proporcionar las siguientes facilidades:

# Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la misma forma que los argumentos del constructor.
# La clase debe estar equipada con métodos de un parámetro llamados add_days(n) y subtract_days(n), siendo n un número entero que actualiza el día de la semana almacenado dentro del objeto mediante el número de días indicado, hacia adelante o hacia atrás.
# Todas las propiedades del objeto deben ser privadas.

class WeekDayError(Exception):
    pass
class Weeker: 
    days=["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
    def __init__(self,day):
        try:
            self.__current_day=self.days.index(day)
        except ValueError:
            raise WeekDayError
            
    def get_day(self):
        print(self.days[self.__current_day])
    def subtract_days(self,value):
        self.__current_day=(value-self.__current_day) % 7
    def add_days(self,value):
        self.__current_day=(value+self.__current_day) % 7
    def get_current(self):
        return self.__current_day

try:
    my_week=Weeker("Lun")
    my_week.get_day()
    my_week.add_days(122)
    my_week.get_day()
    my_week.subtract_days(88)
    my_week.get_day()
    print(my_week.get_current())

    
except WeekDayError:
    print("Dia no valido")
    

            
        
    










# class WeekDayError(Exception):
#     pass


# class Weeker:
#     __names = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

#     def __init__(self, day):
#         try:
#             self.__current = Weeker.__names.index(day)
#         except ValueError:
#             raise WeekDayError

#     def __str__(self):
#         return Weeker.__names[self.__current]

#     def add_days(self, n):
#         self.__current = (self.__current + n) % 7

#     def subtract_days(self, n):
#         self.__current = (self.__current - n) % 7


# try:
#     weekday = Weeker('Lun')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Lunes')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.")




# Puntos en un plano
# Visitemos un lugar muy especial: un plano con el sistema de coordenadas cartesianas (puedes obtener más información sobre este concepto aquí: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

# Cada punto ubicado en el plano puede describirse como un par de coordenadas habitualmente llamadas x y y. Queremos que escribas una clase en Python que almacene ambas coordenadas como números flotantes. Además, queremos que los objetos de esta clase evalúen las distancias entre cualquiera de los dos puntos situados en el plano.

# La tarea es bastante fácil si empleas la función denominada hypot() (disponible a través del módulo math) que evalúa la longitud de la hipotenusa de un triángulo rectángulo (más detalles aquí: https://en.wikipedia.org/wiki/Hypotenuse) y aquí: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

# Así es como imaginamos la clase:

# Se llama Point.
# Su constructor acepta dos argumentos (x y y respectivamente), ambos por defecto se igualan a cero.
# Todas las propiedades deben ser privadas.
# La clase contiene dos métodos sin parámetros llamados getx() y gety(), que devuelven cada una de las dos coordenadas (las coordenadas se almacenan de forma privada, por lo que no se puede acceder a ellas directamente desde el objeto).
# La clase proporciona un método llamado distance_from_xy(x,y), que calcula y devuelve la distancia entre el punto almacenado dentro del objeto y el otro punto dado en un par de números flotantes.
# La clase proporciona un método llamado distance_from_point(point), que calcula la distancia (como el método anterior), pero la ubicación del otro punto se da como otro objeto de clase Point.


# import math


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         #
#         # Escribir código aquí
#         #

#     def getx(self):
#         #
#         # Escribir código aquí
#         #

#     def gety(self):
#         #
#         # Escribir código aquí
#         #

#     def distance_from_xy(self, x, y):
#         #
#         # Escribir código aquí
#         #

#     def distance_from_point(self, point):
#         #
#         # Escribir código aquí
#         #


# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))
    




# Tríangulo
# Ahora vamos a colocar la clase Point (ver Lab anterior) dentro de otra clase. Además, vamos a poner tres puntos en una clase, lo que nos permitirá definir un triángulo. ¿Cómo podemos hacerlo?

# La nueva clase se llamará Triangle y esto es lo que queremos:

# El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.
# Los puntos se almacenan dentro del objeto como una lista privada.
# La clase proporciona un método sin parámetros llamado perimeter(), que calcula el perímetro del triángulo descrito por los tres puntos; el perímetro es la suma de todas las longitudes de los lados (lo mencionamos para que conste, aunque estamos seguros de que tú mismo lo conoces perfectamente).
# Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra.




#     import math


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         per = 0
#         for i in range(3):
#             per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
#         return per


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())