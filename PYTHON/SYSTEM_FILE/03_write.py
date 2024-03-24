##Objetivo Crear una funcion que permita escrbir un archivo
## y definir su modo de escritura
import os
def write():
    try:
        path=input("Escriba la ruta y nombre del archivo")
        if(os.path.exists(path)):
            modo=input("Defina el modo de apertura\n'a' or 'w'?\n")
            with open(path,modo) as file:
                content=input("Escriba el contenido del archivo")
                file.write("\n"+content)
                file.close()
        else:
            raise FileExistsError
    except Exception as e:
            print(f"Error",str(e))
        
            
write()
        



















# import os

# def open_and_create():
#     path_file=path_name=get_path_file()
#     if os.path.exists(path_file):
#         mode=input("Selecione el modo de escritura\n")
#         content=input("Agregue el contenido")
#         try:
#             obj_file=open(path_file,mode)
#             if mode == "a":
#                 content="\n"+content
#             obj_file.write(content)
#             obj_file.close()        
#         except Exception as e:
#             print("GHubo un problem al abrir/editar el archivo",str(e))

# def get_path_file():
#     path=input("Ingrese la ruta relativa o absoluta")
#     name=input("Ingrese el nombre del archivo")
#     path_file=os.path.join(f"{path}/{name}")
#     return path_file
    
# open_and_create()

























# def write_file(seleccion,path,contenido):
#     try:
#         obj_file=open(path,seleccion)
#         obj_file.write(contenido)
#         print("Archivo editado con exito")
#     except Exception as e:
#         print("Hubo un error el editar el archivo",str(e))

# def mode_write():
#     path=name_file()
#     seleccion=input("Ingrese el modo de apertura de su archivo:\n1)'a'\n2)'w'")
#     contenido=input("Ingrese el contenido que desea escribir")
#     if seleccion == "a" or seleccion == "w":
#          write_file(seleccion,path,contenido)
#     else:
#         print("El tipo de apertura noe s valido, intentlo nuevamente")
    


# def name_file():
#     name=input("Ingrese el nombre del archivo")
#     path_file=input("Ingrese la ruta del archivo")
#     extension=input("Ingrese la extension del archivo")
#     path=os.path.join(f"{path_file}/{name}.{extension}")
#     return path



# mode_write()








# def how_to_write(contenido):
#     eleccion_mode=input("Seleccione el modo de apertura \n1) 'w'\n2) 'a'\n")
#     if eleccion_mode == "1":
#         write_file("w",contenido)
#     elif eleccion_mode == "2":
#         write_file("a",contenido)
#     else:
#         print("La eleccion no es valida.Intenetlo nuevamente")
#         how_to_write()

# def write_file(modo,contenido):
#     name_file=input("Ingrese el nombre del archivo")
#     try: 
#         obj_file=open(name_file,modo)
#         obj_file.write(contenido)
#         obj_file.close()
#     except Exception as e:
#         print(f"Hubo un problema intentando abrir el archivo",str(e))


# def start_write():
#     contenido=input("Escriba el contenido a escribir ene l archivo")
#     if contenido:
#         how_to_write(contenido)
#     else:
#         mas_info="\nSi abre su archivo en modo 'w' el contenido de lo que escriba remplazara al contenido actual\n. Si abre su archivo en modo 'a' todo lo escriba se agregara debajo del conetnido actual" 
#         how_to_write(mas_info)

# start_write()

    