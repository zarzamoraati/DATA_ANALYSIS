# ##Objetivo crear una funcion que permita abrir y leer un archivo
import os
# os.mkdir("./test")

# with open("./test/test_file1.txt","wt") as file1,open("./test/test_file2.txt","wt") as file2:
#     file1.write("some text \n some another text")
#     file2.write("sojwojwdodjojo \n kwqhdqhqdi\n kqwdlkqbkbbbxbibi1ashoax\n dwbqaxdpodop")
    

def open_and_read():
    path_file=get_name_file()
    if os.path.exists:
        try:
            obj_file=open(path_file,"rt")
            print(obj_file.read())
            obj_file.seek(0)
            print(obj_file.readlines())
            obj_file.close()
            print("El archivo se  cerro con exito")
        except Exception as e:
            print("Hubo un error al intentar abrir el archivo",str(e))


def get_name_file():
    path=input("Ingrese la ruta absoluta o relativa \n")
    name=input("Ingrese el nombre del archivo y extension \n")
    path_name=os.path.join(f"{path}/{name}")
    return path_name

open_and_read()







# def open_file(path_file):
#     obj_file=open(path_file,"r")
#     print(obj_file.read())
#     ##seek()-PUNTERO QUE SE ENCARGA DE LEER EL CONT DEL ARCHIVO
#     obj_file.seek(0)##restablecemos el puntero a 0 para el metodo readlines()
#     print(obj_file.readlines())
#     obj_file.close() 

# def input_file():
#     name_file=input("Ingrese la ruta y nombre del archivo")
#     extension=input("Ingrese la extension del archivo")
#     path_file=os.path.join(f"{name_file}.{extension}")
#     open_file(path_file)

