# Inicializar una variable para almacenar la suma de números pares
suma = 0

# Iterar a través de los números del 1 al 100
for numero in range(1, 101):
    # Verificar si el número actual es par
    if numero % 2 == 0:
        # Si es par, agregarlo a la suma
        suma += numero

# Imprimir la suma de números pares del 1 al 100
print("La suma de los números pares del 1 al 100 es:", suma)
