
## convertir cada caracter de una cadena en su siguiente en punto codigo
##Restricciones Solo se aceptan letras en mayusculas
##la cadena no debe contener espeacios

##**El método isalpha() es más especializado, se interesa en letras solamente.

# **Al contrario, el método isdigit() busca solo dígitos, cualquier otra cosa produce False (falso) como resultado.

# **Si deseas saber el valor del punto de código ASCII/UNICODE de un carácter específico, puedes usar la función ord() (proveniente de ordinal).si deseas saver el el caracter a partir de un valo puedes usar chr

def to_cifrado_cesar(string):
    filter_letters=string
    ##solo letras
    if not string.isalpha():
        filter_letters="".join([item for item in cadena if item.isalpha()])
    #contiene minusculas?
    if filter_letters.islower():
        filter_letters=filter_letters.upper()
    ##no espacios
    filter_letters=filter_letters.strip()
    ##cifrado  ord() , chr()
    # filter_letters=chr(ord()+1)
    cifrado_result=""
    for ch in filter_letters:
        cifrado_result+=(chr(ord(ch)+1))
    return cifrado_result



##Tu tarea es escribir un programa el cual:

# Le pida al usuario una línea de texto para encriptar.
# Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
# Imprime el texto codificado.

##MEJORAR FUNCION AGREGANDO LOS SIGUIENTES ELEMTOS (TEXTOA CODIFICAR ) (CANTIDAD DE SDESPLAZAMIENTOS) (TIPO DE CIFRADO, CIFRAR O DESCIFRAR)


cadena = "holas1 delrima"
print(to_cifrado_cesar(cadena))
    