# programa que calcula los número pares de un rango solicitado


x = int(input("Ingrese el número inicial: "))
y = int(input("Ingrese el número final: "))

for i in range(x, y + 1):
    if (i % 2) == 0:
        print(i)