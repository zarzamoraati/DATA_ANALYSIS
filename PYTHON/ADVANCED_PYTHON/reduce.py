from functools import reduce 

numeros=[num for num in range(101)]

print(reduce(lambda x,y:x+y,numeros))





















# numeros=[1,10,20,100]
# # # Calcular la suma de una lista de números
# suma=reduce(lambda x,y:x+y,numeros)
# print(suma)








# SINTAXIS reduce(función, secuencia):

# La función reduce() aplica la función dada a los elementos de la secuencia de forma acumulativa y devuelve un solo valor resultante.
# Para utilizar reduce(), debes importarla del módulo functools.
# Ejemplo de uso:

# from functools import reduce
# # Calcular la suma de una lista de números



# numeros = [1, 2, 3, 4, 5]
# suma = reduce(lambda x, y: x + y, numeros)
# print(suma)
# # Resultado: 15
# Recuerda que map(), filter() y r