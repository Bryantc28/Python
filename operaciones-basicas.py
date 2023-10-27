# Escribe un programa que funcione como una calculadora básica.
# Debe solicitar al usuario dos números y una operación (suma, resta, multiplicación o división)
# y mostrar el resultado de la operación.
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir por cero."

operaciones = {
    '1': suma,
    'suma': suma,
    '2': resta,
    'resta': resta,
    '3': multiplicacion,
    'multiplicacion': multiplicacion,
    '4': division,
    'division': division
}

try:
    numero_1 = float(input("Ingrese un número: "))
    numero_2 = float(input("Ingrese otro número: "))
    opcion = input("Opciones\n"
                   "1 - Suma\n"
                   "2 - Resta\n"
                   "3 - Multiplicación\n"
                   "4 - División\n"
                   "¿Qué operación desea realizar?: ").lower()

    resultado = operaciones.get(opcion, "Opción inválida.")(numero_1, numero_2)
    print("Resultado:", resultado)

except ValueError:
    print("Error: Por favor, ingrese números válidos.")
