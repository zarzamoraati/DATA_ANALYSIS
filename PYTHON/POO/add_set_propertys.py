class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
    

# Así es como funciona:

# La línea 1: define una clase muy simple...
# Las líneas 3 a la 10: ... la llenan con algunos atributos.
# La línea 12: ¡esta es nuestra función!
# La línea 13: escanea el atributo __dict__, buscando todos los nombres de atributos.
# La línea 14: si un nombre comienza con i...
# La línea 15: ... utiliza la función getattr() para obtener su valor actual; nota: getattr() toma dos argumentos: un objeto y su nombre de propiedad (como una cadena) y devuelve el valor del atributo actual.
# La línea 16: comprueba si el valor es de tipo entero, emplea la función isinstance() para este propósito (discutiremos esto más adelante).
# La línea 17: si la comprobación sale bien, incrementa el valor de la propiedad haciendo uso de la función setattr(); la función toma tres argumentos: un objeto, el nombre de la propiedad (como una cadena) y el nuevo valor de la propiedad.