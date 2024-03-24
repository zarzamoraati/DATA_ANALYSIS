
# diccionario={}
# ##Add
# diccionario["Deldrima"]={"age":22,"nature":"arcane"}
# diccionario.update({"Noemi":{"age":45,"nature":"magic"}})
# print(diccionario["Deldrima"])
# print(diccionario["Noemi"])


# ##Update
# diccionario["Deldrima"]={"age":20,"nature":"pacific"}
# diccionario2={"Noemi":{"age":12,"nature":"warrior"}}
# diccionario.update(diccionario2)
# print(diccionario["Noemi"])

# ##get 
# print(diccionario.get("Deldrima"))
# print(diccionario.get("Noemi"))
# ##Remove
# diccionario4=diccionario.copy()
# print(diccionario4)
# diccionario.pop("Deldrima")
# print(diccionario.get("Deldrima"))
# diccionario.popitem()
# print(diccionario)
# del diccionario4["Deldrima"]
# print(diccionario4)
# ##Metodos
# diccionario4["polo"]={"age":22,"nature":"shy"}
# print(diccionario4.keys())
# print(diccionario4.values())
# print(diccionario4.items())
# diccionario4.clear()
# print(diccionario4)







###Add
diccionario={}
diccionario["noemi"]={"nature":"arcane","hair":"curly"}
diccionario.update({"chio":{"nature":"warrior","hair":"straight"}})
print(diccionario["noemi"])
print(diccionario["chio"])

###Get
print(diccionario.get("noemi"))
print(diccionario.get("chio"))

###Update
diccionario.update({"noemi":{"nature":"mistic","hair":"tick"}})
diccionario["chio"]={"armor":"12"}
print(diccionario.get("noemi"))
print(diccionario.get("chio"))
##delete

print("depues de eliminar")
del diccionario["noemi"]
diccionario.pop("chio")

print(diccionario)

##methods
diccionario["noemi"]={"nature":"shy","hair":"curly"}
diccionario.update({"chio":{"nature":"warrior","hair":"straight"}})
new=diccionario.copy()
print(new.keys())
print(new.values())
print(new.items())

new.clear()
print(new)
















##(3)Crear un diccionario llamado "person" con las claves "name" y "age".

# person={"name":[],"age":[]}


# bandera=" "

# while bandera:
#     name=input("Ingrese su nombre")
#     age=input("Ingrese su edad")
#     person["name"].append(name)
#     person["age"].append(age)
#     bandera=input("Desea agregar mas valores\n?")


# for i in range(len(person["name"])):
#     nombre=person["name"][i]
#     edad=person["age"][i]
#     if int(edad)<18:
#         print("Persona", nombre, " es menor de edad" )
#     else:
#         print("Persona", nombre, " es adulta")
    
        
