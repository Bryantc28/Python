numero = int(input("Ingrese el número:"))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"El número{numero} no es primo")
            break
    else:
        print(f"El número {numero} es primo")
else:
        print(f"El número {numero} no es primo")