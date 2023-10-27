# Escribe un programa que solicite un número al usuario y realice una
# cuenta regresiva desde ese número hasta 1, mostrando cada número en pantalla.

x = int(input("Ingrese un número: "))

for i in range(x, 0, -1):
    print(i)