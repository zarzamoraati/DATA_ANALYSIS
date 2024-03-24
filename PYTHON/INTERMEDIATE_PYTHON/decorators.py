def validation():
    diccionario={}
    def wrapper(*args):
        try:
            if args[1] == 0:
                raise ZeroDivisionError
            elif not all(isinstance(value , int) or isinstance(value,float) for value in args ):
                raise ValueError
            else:
                if  args in diccionario:
                    print("Dvolviendo resultados desde la cache")
                    result=diccionario[args]
                    print(f"Resultado {round(result,2)}")  
                else:
                    print("Lllamando a la funcion 'dividir'")
                    result=division_num(*args)
                    diccionario[args]=result
                    return print(f"Resultado: {round(result,2)}")
              
        except ZeroDivisionError:
            print("Division entre 0 no definida")
        except ValueError:
            print("Solo se permiten numeros")
        except Exception as e:
            print(str(e))
            
    return wrapper
            
        
def division_num(x,y):
    return x/y


validador=validation()
validador(2,9)
validador(1,0)
validador("a",2)
validador(2,9)
validador(10,2)

    



















# ##Decoradores
##cache
# def cache():
#     diccionario={}
#     def wrapper(*args):
#         if args in diccionario:
#             print("Delvolviendo resultados desde la cache")
#             return print(diccionario[args])
#         else:
#             print("Devolviendo resultados desde la funcion suma")
#             result=suma(*args)
#             diccionario[args]=result
#             return print(result)
#     return wrapper
# def suma(a,b):
#     return a+b

# my_cache=cache()
# my_cache(20,10)
# my_cache(20,10)
# my_cache(70,30)
##validator
# def validator():
#     def wrapper(*args):
#         try:
#             if args[1] == 0:
#                 raise ZeroDivisionError
#             if not all(isinstance(item, int) or isinstance(item,float) for item in args):
#                 raise ValueError
#             else:
#                 result=division(*args)
#                 return print(result)
#         except ZeroDivisionError:
#             print("La division por 0 no esta definida")
#         except ValueError:
#             print("Solo enteros o flotantes son valores validos")
#         except Exception as e:
#             print(f"Se produjo un error", str(e))
#     return wrapper


# def division(x,y):
#     return x/y

# my_validator=validator()
# my_validator(12,2)
# my_validator(10,0)
# my_validator(40,"a")














# #decorador cache
# def cache():
#     almac_cache={}
#     def wrapper(*args):
#         if args in almac_cache:
#             print("Devoliendo resultados desde la cache")
#             return print(almac_cache[args])
#         else:
#             result=suma(*args)
#             almac_cache[args]=result
#             return print(result)
#     return wrapper

# def suma(a,b):
#     print("Devolviendo resultados desde la funcion ")
#     return a+b


# my_cache=cache()
# my_cache(12,8)
# my_cache(12,8)

# decorador valida- tipos
# def tipos():
#     def wrapper(*args):
#         try:   
#             if args[1] ==0:
#                 raise ZeroDivisionError
#             if(all(isinstance(arg, int) or isinstance(arg, float) for arg in args)):
#                 print("Los tipso osn validos, llamando al funcion 'dividir'")
#                 result=dividir(*args)
#                 return print(result)
#             else:
#                 raise TypeError
#         except ZeroDivisionError:
#             print("la division entre 0 no esta definida, ingrese un valor valido ")
#         except TypeError:
#             print("Los tipos dados no son validos,solo numeros")        
#     return wrapper

# def dividir(x,y):
#     return x/y


# my_type=tipos()
# my_type(8,2)
# my_type(19,0)
# my_type("a",100)