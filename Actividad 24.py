#Actividad 24

def menu():
    print("---MENÚ---")
    print("1.Factorial de un numero")
    print("2.Suma hasta n numero")
    print("3.Calcular el numero Fibonacci")
    print("4.Contar apariciones de letra")
    print("5.Invertir cadena de texto.")
    print("6.Calcular potencia de numero.")
    print("7.Salir.")

def factorial(numero):
    if numero == 0 or numero==1:
        return 1
    else:
        return numero * factorial(numero-1)

def suma(numero):
    if numero ==0 or numero ==1:
        return 1
    else:
        numero= numero
        return numero + suma(numero-1)



def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero ==1:
        return 1
    else:
        return fibonacci(numero -1) + fibonacci(numero -2)

def contar_letra(palabra,letra):
    if palabra =="":
        return 0
    else:
        if palabra[0] == letra:
            return 1 + contar_letra(palabra[1:],letra)
        else:
            return contar_letra(palabra[1:],letra)


def invertir_cadena(cadena_texto, contador=0):
    if contador == len(cadena_texto):
        return ""
    else:
        return invertir_cadena(cadena_texto, contador +1) + cadena_texto[contador]

def potencia(base,exponente):
    if exponente ==0:
        return 1
    else:
        return potencia(base,exponente -1)


#programa principal
while True:
    menu()
    opcion= input("Ingrese una opcion:")
    match opcion:
        case "1":
            print("Factorial de numero")
            numero=int(input("Ingrese un numero:"))
            print(factorial(numero))
        case "2":
            print("Suma hasta n numero")
            numero= int(input("Ingrese un numero:"))
            print(suma(numero))
        case "3":
            print("Calculo Número Fibonacci")
            numero= int(input("Ingrese numero a calcular:"))
            print(fibonacci(numero))
        case "4":
            print("Contador de apariciones de letra en palabra")
            palabra= input("Ingrese palabra:")
            letra : input("Ingrese letr a buscar:")
            print(contar_letra(palabra,letra))
        case "5":
            print("Invertir cadena de texto")
            texto= input("Ingrese cadena de texto:")
            print(invertir_cadena(texto))
        case "6":
            print("Calular potencia de numero")
            numero= int(input("Ingrese numero:"))
            potencia: int(input("Ingrese potencia de numero:"))
            potencia(numero,potencia())
        case "7":
            print("Saliendo....")
        case _:
            print("Opcion no valida...")
            break

