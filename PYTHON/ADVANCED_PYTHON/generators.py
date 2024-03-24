# Paso 1: Define una función que actúe como generador. Por ejemplo, crearemos un generador que genere los cuadrados de los números del 1 al 5.
# Paso 2: Llama a la función generadora y asigna el resultado a una variable.
# Paso 3: Utiliza el generador para obtener los valores generados. Puedes hacer esto mediante un bucle for o llamando al método next() del generador.

def generator():
    for x in range(10):
        yield x**2

obj_gen=generator()

for numero in obj_gen:
    print(numero)


# def generator():
#     for numero in range(6):
#         yield numero


# iter_obj=generator()

# for numero in iter_obj:
#     print(numero)

# def generator_squares():
#     for numero in range(6):
#         yield numero **2


# obj=generator_squares()
# for number in obj:
#     print(number)



# def generator():
#     for i in range(1,6):
#         yield i


# obj_generator=generator()
# # print(next(obj_generator))
# # print(next(obj_generator))
# # print(next(obj_generator))
# # print(next(obj_generator))
# # print(next(obj_generator
# for number in obj_generator:
#     print(number)


# cuadrados=(numero**2 for numero in range(1, 6) )
# print(cuadrados)
# for cuadrado in cuadrados:
#     print(cuadrado)


# Ejercicio 2: Generador usando comprensiones de listas

# Paso 1: Define una comprensión de lista que genere los números pares del 1 al 10. Utilizaremos una condición en la comprensión para filtrar solo los números pares.Devuelve la compresionc omo un generador
# Paso 2: Utiliza el generador para obtener los valores generados. Puedes hacer esto mediante un bucle for o llamando al método next() del generador.


# pares=(numero for numero in range(11) if numero % 2==0)
# print(pares)
# for par in pares:
#     print(par)


# def generador_cuadrados():
#     for i in range(1, 6):
#         yield i**2

# generador = generador_cuadrados()


# for numero in generador:
#     print(numero)



# Ejercicio 2: Generador usando comprensiones de listas

# Paso 1: Define una comprensión de lista que genere los números pares del 1 al 10. Utilizaremos una condición en la comprensión para filtrar solo los números pares.
# Paso 2: Utiliza el generador para obtener los valores generados. Puedes hacer esto mediante un bucle for o llamando al método next() del generador.

# obj_pares=(pares for pares in range(1,11) if pares%2==0)
# for par in obj_pares:print(par)

# pares=(n for n in range(1,11 ) if n % 2 == 0  )
# print(pares)
# for m in pares:
#     print(m)
# print(list(pares))



# generador_pares = (num for num in range(1, 11) if num % 2 == 0)


# for numero in generador_pares:
#     print(numero)