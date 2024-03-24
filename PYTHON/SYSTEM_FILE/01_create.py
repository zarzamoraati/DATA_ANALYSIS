##Objetivo Crea uan funcion con las opciones 
##de crear un archivo o un directorio
import os 

def create():
    opcion=input("Eliga una opcion:\n1) Crear archivo\n2)Crear directorio")
    if(opcion == "1"):
        create_file()
    elif(opcion=="2"):
        create_dir()
    else:
        print("Opcion invalida")


def create_file():
    path_file=create_path()
    try:
        with open(path_file,"w") as file:
            content=input("Ingrese el contenido de su archivo")
            file.write(content)
            file.close()
            print("Archivo creado con exito")
    except Exception as e:
        print(f"Error", str(e))
    
    
def create_path():
    name_path=input("Ingrese la ruta y nombre del archivo")
    ext=input("Ingrese la extension")
    path=os.path.join(f"{name_path}.{ext}")
    return path

    
def create_dir():
    path=input("Ingrese la ruta y nombre del directorio")
    try:
        if(os.path.exists(path)):
            raise FileExistsError
        else:
            try:
                os.mkdir(path)
                print("Directorio creado con exito")
            except:
                raise Exception
    except FileExistsError:
        print("El direcotorio con la ruta especiifcada ya existe")
    except Exception as e:
        print(f"Error:{str(e)}")
        

create()


















# import os

# def create():
#     opcion=input("Desea crear un 1)file  o un 2)Directorio?")
#     if opcion=="1":
#         create_file()
#     elif opcion=="2":
#         create_dir()
#     else:
#         print("Opcion Invalida")
#         create()

# def create_file():
#     path_file=create_path_file()
#     try:
#         with open(path_file, "w") as archivo:##Obligatorio usar "w" o "a" para crear un new file
#              print(f"Archivo {path_file} creado con exito")
#              archivo.close()
#     except Exception as e:
#              print("Hubo un error al crear archivo",str(e))
            

# def create_path_file():
#     name=input("Escriba el nombre del archivo")
#     path=input("escriba la ruta del arcchivo")
#     ext=input("Ingrese la extensiond el arcivo")
#     path_file=os.path.join(f"{path}/{name}.{ext}")    
#     return 

# def create_dir():
#     path_dir=input("Escriba la ruta y nombre del directorio")
#     try:
#         os.mkdir(path_dir)
#         print(f"Directorio {path_dir} creado con exito")
#     except Exception as e:
#         print("Hubo un error al crear el directorio",str(e))


# create()



# import os
# def create_dir(path):
#     try:
#         os.mkdir(path)
#         print("Directorio creado con exito¡¡¡")
#     except FileExistsError:
#         print(f"El archivo {path} ya existe" )
#     except Exception as e:
#         print("Error al crear el archivo",str(e))
        

# def nombrar_directorio():
#     path=input("Ingrese la ruta y el nombre del directorio:") 
#     create_dir(path)


# def crear_archivo(path_file,contenido):
#     with open(path_file,"w") as archivo:
#         archivo.write(contenido)
#         print("Archivo creado con exito")

# def nombrar_archivo():
#     nombre_archivo=input("Ingrese la ruta y nombre del archivo")
#     extension=input("Ingrese la extension")
#     contenido=input("Defina el contenido del archivo")
#     path_file=os.path.join(f"{nombre_archivo}.{extension}")
#     crear_archivo(path_file,contenido)


# def creator():
#     eleccion=input("Desea crear un archivo (1) o un directorio (2)?")
#     if eleccion == "1":
#         nombrar_archivo()
#     elif eleccion == "2":
#         nombrar_directorio()
#     else:
#         print("La opcion ingresada no es valida, Intentelo nuevamente")
#         return creator()



# creator()
