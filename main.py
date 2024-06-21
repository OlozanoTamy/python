import os
# Calculo del minimo comun multiplo de 3 numeros


def menu():
    os.system("clear")
    print("Bienvenido a tu calculadora de  MCM y MCD")
    print("Menu de opciones")
    print("Seleccione su opcion")
    print("\t 1 - Calcular el Minimo Comun Multiplo")
    print("\t 2 - Calcular el Maximo Comun Divisor")
    print("\t S - Salir")


def MCM_metodo1(num1, num2, num3):
    print("Metodo 1")


def MCD_metodo1(num1, num2, num3):
    print("Dale ROOOOO")


def MCD_metodo2():
    print("Lo dejo todo")


def MCM_metodo2():
    print("Sos de la B")

# Programa Principal


seleccion = "0"
while (seleccion != "S"):
    menu()
    seleccion = input("Ingrese un numero o presione S para salir")
# num1 = int(input("Digite el primer numero: "))
# num2 = int(input("Digite el segundo numero: "))
# num3 = int(input("Digite el tercer numero: "))
# print(f'Los numeros que digito son, {type(num1)} , {num2} , {num3}')
