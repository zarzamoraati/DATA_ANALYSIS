def validation_limite():
    try:
        entrada=int(input("Ingrese un numeor enetero, \n"))
        limit_inf=int(input("Ingrese un limite inf \n"))
        limit_sup=int(input("ingrese un limite superior"))
        if limit_inf > entrada or limit_sup < entrada:
            raise IndexError
        print(entrada)
    except ValueError:
        print("Entrada incorrecta")
    except IndexError:
        print("Error: el valor no está dentro del rango permitido (min..max)") 
        

validation_limite()




print(float("1, 3"))