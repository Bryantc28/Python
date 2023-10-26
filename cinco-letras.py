#Escribe un programa que tome una lista de palabras
# y devuelva una lista que contenga solo las palabras que tienen más de cinco letras.

lista = []

while True:
    palabra = input("Ingrese una palabra: ")
    c = len(palabra)

    if c > 5:
        lista.append(palabra)
    else:
        insertar = input("¿Desea ingresar otra palabra? (s/n): ").lower()
        if insertar != 's':
            break

print("Palabras con más de cinco letras: ")
for i in lista:
    print(i)