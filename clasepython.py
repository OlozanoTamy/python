# Cicol while
# Ciclo for
# Un bucle for es un buvle  que se repite un numero determinado de veces
import random
# print("Inicio del programa")

# for variable in [0, 1, 2, 3, 4]:
#     print(f'El valor de la variable es {variable}')
# print("Fin del programa")

# for i in range(100):
#     print("Hola")
# print("Solo santa fe loka")


# El rango puede ser negativo

# Dado
print("Comienzo")
# Variable Testigo
sacaste_cinco = False
for i in range(3):
    dado = random.randrange(1, 7)
    print(f"Tirada {i+1}: {dado}")
    if dado == 5:
        sacaste_cinco = True
if sacaste_cinco:
    print("Ha salido al menos un 5")
else:
    print("No ha salido ningun 5")
print("Final")


# Contador
print("Comienzo")
contador = 0
for i in range(3):
    dado = random.randrange(1, 7)
    print(f"Tirada {i+1}: {dado}")
    if dado == 5:
        contador += 1
if contador > 0:
    print(f"Ha salido {contador} cincos")
else:
    print("No ha salido ningun 5")
print("Final")

# Acumuladores
# Se usan para acumular datos
