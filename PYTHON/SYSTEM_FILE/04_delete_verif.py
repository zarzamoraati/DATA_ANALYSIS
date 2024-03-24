import os
##Objetivo  Crear una funcion que permita eliminar un directorio u archivo
def delete():
    opcion=input("Elija una opcion: 1) Delete File\n2)Delete Dir")
    if opcion == "1":
        delete_file()
    elif opcion == "2":
        delete_dir()
    else:
        print("Opcion invalida")
        

def delete_file():
    path=input("Ingrese la ruta y el nombre del archivo\n")
    try:
        if(os.path.exists(path)):
            os.remove(path)
            print("Archivo eliminado con exito")
        else:
            raise FileExistsError
    except FileExistsError:
            print("El archivo no existe")
    except Exception as e:
            print(f"Error:",str(e))
        
def delete_dir():
    path=input("Ingre al ruta del directorio")
    try:
        if os.path.exists(path):
            aux(path)
            print("Directorio eliminado con exito")
        else:
            raise Exception("EL DIRECTORIO NO EXISTE")
    except Exception as e :
        print(str(e))

def aux(path):
    if len(os.listdir(path))>0:
         for element in os.listdir(path):
                path_ext= os.path.join(f"{path}/{element}")
                if os.path.isfile(path_ext):
                    os.remove(path_ext)
                else:
                    aux(path_ext)
    try:
        os.rmdir(path)
    except:
        print("Error rmdir")     
                    


delete()












# ##NOTA : IMPORTAR MODULO shutil para eliminar directorios no vacios
# def check_and_delete():
#     tipo=input("Ingrese elemento a eliminar 1) Archivo 2)Directorio")
#     if tipo=="1":
#         delete_file()
#     elif tipo=="2":
#         delete_dir()
#     else:
#         print("El tipo del elemento no es valido")

# def delete_file():
#     path=input("Ingrese la ruta del archivo")
#     name=input("Ingrese el nombr del archivo")
#     file_path=os.path.join(f"{path}/{name}")
#     if os.path.exists(file_path):
#         try:
#             os.remove(file_path)
#         except Exception as e:
#             print("Hubo un error al remover el archivo",str(e))

# def delete_dir():
#     path=input("Inrese la ruta del directorio")
#     if os.path.exists(path):
#         try:
#             aux_vaciar(path)
#             print("Todos los directorios en la ruta fueron eliminados con exito")
#         except Exception as e:
#             print("Hubo un problema al eliminar el directorio",str(e))
#     else:
#         print("Ruta no valida")


# def aux_vaciar(path):

#     if len(os.listdir(path))>0:
#         for element in os.listdir(path):
#             path_extend=os.path.join(f"{path}/{element}")
#             if os.path.isfile(path_extend):
#                 os.remove(path_extend)
#             else:
#                 aux_vaciar(path_extend)
    
#         try:
#             os.rmdir(path)
#             print(f"Directorio {path} eliminado")
#         except:
#             print("Problema al eliminar el directroio")
    

    


# check_and_delete()























# def delete_file():
#     path=get_path_file()
#     if os.path.exists(path):
#         try:
#             os.remove(path)
#             print("Archivo eliminado con exito")
#         except Exception as e:
#             print("Hubo un error al eliminar el archivo")

# def get_path_file():
#     name=input("Ingrese el nombre del archivo ")
#     path_file=input("Inregese la ruta del archivo ")
#     extension=input("Ingrese la extension del archivo")
#     return os.path.join(f"{path_file}/{name}.{extension}")

# def delete_dir():
#     path=input("Ingrese la ruta del directorio ")
#     if os.path.exists(path):
#         vaciar_dir(path)
#     else:
#         print("La ruta especificada no existe")

# def vaciar_dir(path):
#     if os.path.isfile(path):
#         os.remove(path)
#         print(f"Archivo {path} eliminado con exito")
#     else:
#         if len(os.listdir(path)) > 0:
#              for element in os.listdir(path):
#                 vaciar_dir(os.path.join(f"{path}/{element}"))
#         try:
#             os.rmdir(path)
#             print(f"Directorio {path} eliminado con exito")
#         except Exception as e:
#             print("Hubo un error al eliminar el direcotio")
            

    

# def delete():
#     seleccion=input("Desea eliminar un archivo o un directorio \n1)Archivo\2)Directorio")
#     if seleccion == "1":
#         delete_file()
#     elif seleccion == "2":
#         delete_dir()
#     else:
#         print("Opcion no valida")
#         delete()
    

# delete()













# ##Eliminar un archivo
# def delete_file():
#     path_file=input("Ingrese el nombre y la extension del archivo")
#     if os.path.exists(path_file):
#         try:
#             os.remove(path_file)
#             print(f"El archivo {path_file} fue eliminado con exito")
#         except Exception as e:
#             print("Hubo un error al eliminar el archivo especificado")
#     else:
#         print("El archivo con al ruta especificada no existe")

# ##Eliminar directorio
# def delete_dir(): 
#     path_dir=input("Ingrese la rura y nombre del directorio")
#     ## VERIFICAR SI EL DIR EXISTE ##Devuelve un booelan
#     if os.path.exists(path_dir):
#         vaciar_directorio(path_dir)
#     else:
#         print("El directorio con la ruta especificada no existe")  


# def vaciar_directorio(path):
#     ##Es un archivo
#     if os.path.isfile(path):
#         os.remove(path)
#         print(f"Archivo aliminado con exito:{path}")
#     ##Es un directorio
#     elif os.path.isdir(path):
#         contenido=os.listdir(path)
#         ##El directorio no esta vacio
#         if len(contenido) >= 0:
#             for element in contenido:
#                 path_element=os.path.join(path,element)
#                 vaciar_directorio(path_element)
#             ##El directorio esta vacio
#             try:
#                 os.rmdir(path)
#                 print(f"Directorio ${path} eliminado con exito")
#             except Exception as e:
#                 print("Hubo un error al eliminar el directorio")    


# def start_delete():
#     eleccion=input("Que desea eliminar? \n1)Directorio\nArchivo")
#     if eleccion=="1":
#         delete_dir()
#     elif eleccion == "2":
#         delete_file()
#     else:
#         print("Opcion no valida. Intentelo nuevamente")
#         start_delete()

# start_delete()