# Escribe un programa que tome una lista de números y devuelva una nueva lista
# que contenga solo los números pares de la lista original.

lista_str = input("Ingrese una lista de números: ")

lista = [int(n) for n in lista_str]

pares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)

print(f"Los siguientes números son pares: {pares}")