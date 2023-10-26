# Escribe un programa que tome una lista de nombres y devuelva
# una nueva lista que contenga solo los nombres que contengan la letra 'A'

lista_nombres = []

while True:
    nombre = input("Ingrese un nombre: ")

    if 'a' in nombre or 'A' in nombre:
        lista_nombres.append(nombre)
    else:
        insertar = input("Desea ingresar otro nombre? (s/n): ").lower()
        if insertar != 's':
            break

print("Lista de nombres con 'a': ")
for i in lista_nombres:
    print(i)