

##EXCEPCIONES

# def devolver_rec():

#     try:
#         value = int(input('Ingresa un número natural: '))
#         print('El recíproco de', value, 'es', 1/value)        
#     except ValueError:
#         print(value," no es un tipo valido")
#     except ZeroDivisionError:
#         print("La division entre 0 no esta permitida")
#     except:
#         print("Ha sucedido un error inesperado¡¡¡")

# devolver_rec()

# def get_number():
#      while True:
#         try:
#             number=int(input("Ingrese un numero entero:\n"))
#             return print("El cociente de ",number," entre 2 es: ",number/2)
#         except:
#             print("El valor debe ser un entero")




##(5)Definir una función llamada "divide_numbers" que reciba dos números como parámetros.

# opcion=" "
# def divide_numbers():
#     global opcion
#     while opcion:
#         try:
#             num1=int(input("Ingrese un numero\n"))
#             num2=int(input("Ingrese otro numero\n"))
#             result=num1/num2
#             print("El cociente de los numeros es :", result)
            
#             opcion=input("Desea ingresar mas numeros?\n")
#             opcion=opcion

#         except:
        
#             print("El segundo numero debe de ser diferente de cero")

# divide_numbers()




# def calcular_raiz(numero):
#         try:
#             if(numero<0):
#                 raise ValueError
#             print(numero**2)
            
#         except ValueError:
#             print("El numero debe de ser positivo")


# calcular_raiz(-3)