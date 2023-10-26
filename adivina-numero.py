import random

numero = random.randint(1, 100)
# print(numero)

print("ADIVINA EL NÚMERO")

while True:
    x = int(input("Ingrese un número: "))

    if x < numero:
        print("¡Más alto!")

    elif x > numero:
        print("¡Más bajo!")

    else:
        print("¡Acertaste!")
        break