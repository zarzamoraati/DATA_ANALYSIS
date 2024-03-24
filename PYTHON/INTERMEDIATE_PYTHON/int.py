import time
##(1)
# numbers=[]

# for i in range(5):
#     number=input("Ingrese un numero")
#     if "." in number:
#         number=float(number)
#     else:
#         number=int(number)
#     numbers.append(number)

# print("Lista de Numeros:",numbers)

# product=1
# suma=sum(numbers)
# for number in numbers:
#     product*=number 


# print("Suma:\n",suma)
# print("Producto:\n",product)
# print("Media:\n",round((suma/len(numbers)),1))


##(2)
# person={"nombre":[],"edad":[]}
# opcion=" "
# while opcion:
#     name=input("Ingrese su nombre ")
#     age=int(input("Ingrese su edad"))
#     person["nombre"].append(name)
#     person["edad"].append(age)
#     opcion=input("Desea ingresar otra persona?\n")


# for i in range(len(person["nombre"])):
#     edad=int(person["edad"][i])
#     if edad>=18 and len(list(person["nombre"][i])) >= 5:
#         print(len(list(person["nombre"][i])))
#         print(person["nombre"][i]," es mayor de edad")
#         print(person["El nombre ", "nombre"][i]," tiene 5 letras o mas: ",len(lsist(person["nombre"][i])))
#     else:
#         print(person["nombre"][i]," es menor de edad")
#         print(person["El nombre ","nombre"][i], "tiene una longitud menor a 5 letras:", len(list(person["nombre"][i])))
    

   ###(3) 
# opcion=" "
# words=input("ingrese una frase \n").split(" ")
# print(words)
# string=" ".join(words)
# print(string)
# newString=string.replace("a","*").replace("e","*").replace("i","*").replace("i","*").replace("o","*").replace("u","*")
# print(newString)

###(4)

# def divide_numbers(num1,num2):
#         try:
#             if num2==0:
#                 raise ZeroDivisionError
#             cociente=num1/num2
#             print("Division de ",num1," y ",num2," es: ",cociente)
    
#         except:
#             print(ZeroDivisionError,"Division por cero o segundo numero igual a  0")


# divide_numbers(12,0)
# divide_numbers(24,2)

##(5)

# fruits=["apple","mango","orange","banana"]

# fruits.append("strawberrys")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# print(fruits.index("orange"))
# print(fruits.index("banana"))
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)



####(6)///PENDIENTE MEJORAR EL EJERCICIO

# student={}
# student["name"]=input("Ingrese el nombre del estudiante:\n")


# opcion=" "
# while opcion:
#     asignatura=input("Ingrese una asignatura")
#     nota=float(input("Ingrese la calificacion de {}:".format(asignatura)))
#     student[asignatura]=nota
#     opcion=input("Desea agregar mas asignaturas?")



# asignaturas= ",".join(student.keys())
# notas=", ".join(str(nota) for nota in student.values())
# asignaturas.remove("name")

# print("Asignatura dele studiante: ",asignaturas)
# print("Calificaciones del estudiante: ",notas)

# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)

###FUNCIONES LAMBDA -NIVEL BASICO

# suma=lambda num1,num2:num1+num2
# print(suma(9,10))

# es_par=lambda numero: numero%2==0 
# print(es_par(5))
# print(es_par(10))
# print(es_par(11))

###INTERMEDIO LABMDA FUNCTIONS

##DELVOLVER EL CUADRADO DE UNa lista de NUmeros

# numbers=[11,4,100,50,8]

# pow_numbers=list(map(lambda x:x**2,numbers))
# print(pow_numbers)



##DECORADORES NIVEL BASICO 

# def decorador(callback):
#       def wrapper():
#          print("Hola¡")
#          callback()
#       return wrapper

# def callback():
#    print("some boring stuff here")

# my_decorator=decorador(callback)

# my_decorator()         

#Medir tiempo

# def medir_tiempo(callback,n):
#    def wrapper():
#       inicio=time.time()
#       resultado=callback(n)
#       fin=time.time()
#       interval=fin-inicio
      
#       print("Tiempo de ejecucion:" + str(interval))
#    return wrapper


# def calculate_factorial(n):
#    if n<2:
#       return 1
#    return n * calculate_factorial(n-1)
   

# my_timeout=medir_tiempo(calculate_factorial,5)

# my_timeout()


##DECORADORES -ALMACENAMIENTO EN CACHE

# def cache_decorator(callback):
#    resultados_cache={}
   
#    def wrapper(*args):
#       if args in resultados_cache:
#          print("Obteniendo resultados desde la cache:")
#          return resultados_cache[args]
#       else:
#          resultado=callback(*args)
#          resultados_cache[args]=resultado
#          return resultado
#    return wrapper
# ##USAND PALABRA RESERVADA @<name_decorator>
# @cache_decorator
# def suma(a,b):
#    ##mensaje para saber si el resultado no proviene de la cache
#    print("Calculando la suma...")
#    return a + b 

# suma(22,40)
# suma(22,40)

# my_cache=cache_decorator(suma)
# print(my_cache(12,99))
# print(my_cache(20,100))
# print(my_cache(12,99))

##

### MI IMPLEMENTACION , NOTA:DEJA PASAR VALORES BOOLEANOS
# def validar_decorator(callback):
#    def wrapper(*args):
#       try:
#          for arg in args:
#             if isinstance(arg, int) or isinstance(arg, float):
#                result = callback(*args)
#                return print(result)
#             else:
#                raise TypeError
#       except TypeError:
#          print(f"El tipo: '{type(arg).__name__}' no es un tipo válido")
#    return wrapper

# @validar_decorator
# def multiplicar(a, b):
#    return a * b

# multiplicar(22, 2)
# multiplicar(True, "hola")
# multiplicar("70", 10)
# multiplicar(10, 90.9)


##Implmentacio correcta
# def validar(func):
#     def wrapper(*args, **kwargs):
#         if all(isinstance(arg, int) or isinstance(arg,float) for arg in args):
#             return func(*args, **kwargs)
#         else:
#             print(f"Error, no  valido")
#     return wrapper

# @validar
# def multiplicar(a, b):
#     print(a * b)

# multiplicar(22,2)
# multiplicar(True,"hola")
# multiplicar("70",10)
# multiplicar(10,90.9)





































###Almacenamiento en cache 
##paraa cada entrada dada a una funcion almacenar la entrada y el res
##La salida o solucion es que si se llama a la funcio con los mismo arg
##se devuelva el resultado alamacenado en la "cache" , en lugar de volver a llamar a la func

##funcion decoradora
##funcion wrapper
##funcion a la que se le aplicara el decorador

##interfaz decorator (metodos wrapper)
##interfaz wrapper(metodos 0 )
##interfaz funcion cociente(metodos 0)


# def cache_decorator():
#     cache={}
#     def wrapper(*args,**kwargs):
#         if args in cache:
#             print("mostrando resultado desde la cache:")
#             return print(cache[args])
#         else:
#             resultado=suma(*args)
#             cache[args]=resultado
#             print(resultado)
#     return wrapper       

# def suma(a,b):
#     print("desde la funcion")
#     return a + b

# my_suma=cache_decorator()
# my_suma(89,10)
# my_suma(100,20)
# my_suma(89,10)
#Validar Tipos 

# def validator():
#     def wrapper(*args):
#         try:
#             if args[1] == 0:
#                 raise ZeroDivisionError
#             if all(isinstance(arg, int) or isinstance(arg, float) or not isinstance(arg, bool) for arg in args):
#                 print("Los tipos son validos y diferentes de 0. Llamando a la funcion:")
#                 get_cociente(*args)
#             else:
#                 raise TypeError
#         except TypeError:
#             print("El valor dado no es un tipo valido.Intentelo nuevamente")
#         except ZeroDivisionError:
#             print("El valor del denominador no puedo ser 0. Itentelo nuevamente")
#     return wrapper

# def get_cociente(a,b):
#     return print(a/b)


# my_div=validator()
# my_div(20,2)
# my_div(12,0)
# my_div(True,99)








# my_cuenta=CuentaBancaria("noemi",1999)
# my_cuenta.consultarSaldo()
# my_cuenta.depositar(2000)
# my_cuenta.consultarSaldo()
# my_cuenta.retirar(999)
# my_cuenta.consultarSaldo()
# my_cuenta.retirar(3001)









##decoradores
# def cache():
#    diccionario_cache={}
#    def wrapper(*args,**kwargs):
#       if(args in diccionario_cache):
#          print("devolviendo resultados desde la cache:")
#          return diccionario_cache[args]
#       else:
#          print("llamando a la funcion...")
#          result=suma(*args)
#          diccionario_cache[args]=result
#          return result
#    return wrapper

# def suma(a,b):
#    return a+b

# my_cache=cache()
# print(my_cache(12,90))
# print(my_cache(12,90))
# print(my_cache(1,100))

# def valid_types():
#    def wrapper(*args,**kwargs):
#       try:
#          if args[1]==0:
#             raise ZeroDivisionError
#          if all(isinstance(arg,int) or isinstance(arg, float) for arg in args):
#             result=division(*args)
#             return print(result)
#          else:
#             raise TypeError
#       except ZeroDivisionError:
#          return print("La division entre 0 no esta definida.Intentelo de nuevo")
#       except TypeError:
#          print("El tipo dado es diferentes de int o float.Intento de nuevo")
#    return wrapper

# def division(a,b):
#    return a/b

# my_division=valid_types()
# my_division(890,10)
# my_division("a",10)
# my_division(890,0)


##lambdac



# ##cudrados
# numeros=[2,13,4,5,17,10,23]
# cuadrados=list(map(lambda numero:numero**2,numeros))
# print(cuadrados)

# ##par 
# pares=list(filter(lambda numero:numero%2==0,numeros))
# print(pares)
# ##impar
# impar=list(filter(lambda numero:not numero%2==0,numeros))
# print(impar)

# ##empizar por 
# cadena="la angelical deldrima abre su ano fresco en el atardecer del mes de abril"
# starts=list(filter(lambda word:word.startswith("a") ,cadena.split(" ")))
# print(starts)

# #classes

# numeros1=[122,155]
# print(numeros1.index(155))
