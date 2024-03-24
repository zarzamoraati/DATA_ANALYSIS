# ##cuadrados
# numeros=[x for x in range(11)]
# cudrados=list(map(lambda x:x**2,numeros))
# print(cudrados)
#  ##pares
# pares=list(filter(lambda x:x%2==0,cudrados))
# print(pares)
# ##impares
# impares=list(filter(lambda x:not x%2==0,cudrados))
# print(impares)

# ##startswith
# cadena="la estrella en el atardecer se esfumaba "

# starts=list(filter(lambda word: word.startswith("e"), cadena.split(" ")))

# print(starts)
















##  Lamba functions

## devolver el cuadrado de un arreglo de numeros

numeros=list(range(10))
print(list(map(lambda x:x**2,numeros)))

##Pares
print(list(filter(lambda x: x%2==0,numeros)))
##impares
print(list(filter(lambda x: x%3==0,numeros)))

##startsWith
cadena="la estrella en el atardecer se esfumaba "
print(list(filter(lambda x: x.startswith("e"),cadena.split(" "))))
# suma=lambda x,y:x+y

# print(suma(10,2))
# ##

# numeros=[2,3,4,5,6]

# cuadrados = list(map(lambda numero: numero**2, numeros))

# print(cuadrados)
# ##
# lista=[2,13,9,5,-19,122]

# evaluate_par=list(filter(lambda x:x%2 == 0, lista))
# print(evaluate_par)

# evaluate_impar=list(filter(lambda x: not x%2==0, lista))
# print(evaluate_impar)
# ##
# cadena="Hello friend , australia is a country in the aside of the world "

# empieza_con = list(filter(lambda x:x.startswith("a"),cadena.split(" ")))
# print(",".join(empieza_con))


##devolver palabras que comiencen con "letra"

# cadena="el amor en el estudio era armonico"

# cadena_list=cadena.split(" ")
# print(cadena_list)
# list_starts=list(filter(lambda string:string.startswith("a"), cadena_list))
# print(list_starts)