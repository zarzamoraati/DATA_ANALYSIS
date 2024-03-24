# #RSTRICCIONES 
# Un código de país de dos letras tomado del estándar ISO 3166-1 (por ejemplo, FR para Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).
# Dos dígitos de verificación utilizados para realizar las verificaciones de validez: pruebas rápidas y simples, pero no totalmente confiables, que muestran si un número es inválido (distorsionado por un error tipográfico) o válido.
# El número de cuenta real (hasta 30 caracteres alfanuméricos; la longitud de esa parte depende del paí


#El método isalnum() devuelve True si todos los caracteres de la cadena son alfanuméricos (ya sean letras o números) 


# (Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena (es decir, el código del país y los dígitos de verificación).
# (Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así la cadena, donde A = 10, B = 11 ... Z = 35.
# (Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de ese número dividiéndolo entre 97. Si el residuo es 1, pasa la prueba de verificación de dígitos y el IBAN puede ser válido.


def validador_IBAN():
    iban=input("Ingrese su numero de cuenta IBAN\n")
    iban_normalizado=iban.replace(" ","")
    if not iban_normalizado.isalnum():
        print("Se detectaron caracteres no validos.Solo se aceptan acracteres alfanumericos")
        return validador_IBAN()
    if len(iban_normalizado) > 30:
        return print("Validacion fallida. Cadena demasiado larga (max 30)")
    if len(iban_normalizado)<20:
        return print("Validacion fallida. Cadena demasiado corta min(20)")
    validator=iban_normalizado[4:]+iban_normalizado[0:4]
    iban2=""
    for iban in validator:
         if iban.isdigit():
            iban2+=iban
         else:
            iban2+=str(10 + ord(iban) - ord("A"))
    if int(iban2) % 97 == 1:
        print("IBN valido")
    else:
        print("IBN invalido")
validador_IBAN()


# cadena="deldrima12pure"
# new=[ch.replace(ch, str(ord(ch))) for ch in cadena if ch.isalnum()]
# print(new)
# if float("".join(new)) % 92 == 1:
#     print("IBN VALIDO")
# else:
#     print("IBN INVALIDO")