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
        return numero + suma(numero)

def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero ==1:
        return 1
    else:
        return fibonacci(numero -1) + fibonacci(numero -2)

numero= int(input("INgrese un numero:"))
print(fibonacci(numero))

"""""
#programa principal
menu()
opcion= input("Ingrese una opcion:")
match opcion:
    case "1":
        print("Factorial de numero")
        numero=int(input("Ingrese un numero:"))
        factorial(numero)
    case "2":
        print("Suma hasta n numero")
        numero= int(input("Ingrese un numero:"))
        suma(numero)
        
        """""