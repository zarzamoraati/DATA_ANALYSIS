from os import strerror

diccionario={chr(char):0 for char in range(ord("a"),ord("z") + 1)}
name_file=input("Ingresa el nombre del archivo\n")
try:
    obj_file=open(name_file,"rt")
    for line in obj_file:
        for char in line:
            if char.isalpha():
                diccionario[char.lower()]+=1
    obj_file.close()
    new_file=input("Ingrese el nombre del archivo a editar\n")
    obj_write=open(new_file + ".hist","wt")
    for char in sorted(diccionario.keys(), key=lambda x:diccionario[x], reverse=True):
        if diccionario[char] > 0 :
            obj_write.write(f"{char}==>{diccionario[char]}\n")
    obj_write.close()
    
except IOError as e:
    print("Hubo un error al abrir/leer el archivo", strerror(e.errno))


