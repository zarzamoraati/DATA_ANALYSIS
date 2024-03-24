# Ejercicio de creación de excepciones personalizadas:

# Crea una excepción personalizada llamada SaldoInsuficienteError que se levante cuando se intente retirar más dinero de una cuenta bancaria de lo que hay disponible.
# Crea una función llamada retirar_dinero que reciba como argumentos el saldo actual y la cantidad a retirar.
# Dentro de la función, utiliza un condicional para verificar si la cantidad a retirar es mayor que el saldo actual. Si es así, levanta la excepción SaldoInsuficienteError.
# Prueba la función llamando a retirar_dinero con diferentes saldos y cantidades a retirar.












class SaldoInsuficienteError(Exception):
    pass

def retirar_saldo(saldo,monto):
    try:
        if monto>saldo:
            raise SaldoInsuficienteError("El saldo es insuficiente")
        else:
            return print(f"Saldo restante: {saldo-monto}") 
    except SaldoInsuficienteError as e:
        print(str(e))
    finally:
        print("La transaccion se ha cerrado")


retirar_saldo(122,22)
retirar_saldo(100,120)

# class SaldoInsuficienteError(Exception):
#     pass

# def retirar_dinero(saldo, cantidad):
#     if cantidad > saldo:
#         raise SaldoInsuficienteError("Saldo insuficiente. No se puede retirar esa cantidad.")
#     else:
#         saldo -= cantidad
#         print("Retiro exitoso. Saldo restante:", saldo)

# saldo_actual = 1000
# cantidad_retiro = 1500
# try:
#     retirar_dinero(saldo_actual, cantidad_retiro)
# except SaldoInsuficienteError as e:
#     print(e)

# En este ejercicio, se crea una excepción personalizada SaldoInsuficienteError que se levanta cuando se intenta retirar más dinero del saldo disponible. Al llamar a la función retirar_dinero, se verifica si la cantidad a retirar es mayor que el saldo actual y se levanta la excepción en caso de que sea así.


# Ejercicio de utilización del bloque finally:

# Crea una función llamada abrir_archivo que reciba el nombre de un archivo como argumento.
# Dentro de la función, utiliza un bloque try-except-finally para abrir el archivo en modo lectura, leer su contenido y cerrarlo.
# En el bloque finally, imprime un mensaje indicando que el archivo se ha cerrado correctamente, independientemente de si ocurrió una excepción o no.
# Prueba la función llamando a abrir_archivo con diferentes nombres de archivo, incluyendo uno que no exista.


# def abrir_archivo(file_name):
#     try:
#         if os.path.exists(file_name):
#             obj_file=open(file_name,"r")
#             print(obj_file.read())
#             obj_file.close()
#         else:
#             raise Exception
#     except:
#         print("El archivo no existe")
#     finally:
#         print("El archivo se ha cerrado correctamente")
    
# abrir_archivo("something")


# def abrir_archivo(nombre_archivo):
#     try:
#         archivo = open(nombre_archivo, 'r')
#         contenido = archivo.read()
#         print("Contenido del archivo:", contenido)
#     except FileNotFoundError:
#         print("El archivo no existe.")
#     finally:
#         if 'archivo' in locals():
#             archivo.close()
#             print("Archivo cerrado correctamente.")

# nombre_archivo = "archivo.txt"
# abrir_archivo(nombre_archivo)
# En este ejercicio, la función abrir_archivo intenta abrir y leer un archivo. Si el archivo no existe, se captura la excepción FileNotFoundError. El bloque finally se ejecuta siempre, sin importar si se produce una excepción o no, y se encarga de cerrar el archivo.
