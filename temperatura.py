while True:
    opcion = input("1 para convertir de Celsius a Fahrenheit\n"
                   "2 para convertir de Fahrenheit a Celsius\n"
                   "Ingrese su opción: ")

    if opcion == '1':
        # Convertir de Celsius a Fahrenheit
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(f"{celsius}° Celsius es igual a {fahrenheit:.2f}° Fahrenheit")
    elif opcion == '2':
        # Convertir de Fahrenheit a Celsius
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print(f"{fahrenheit}° Fahrenheit es igual a {celsius:.2f}° Celsius")
    else:
        print("Opción inválida. Por favor, ingrese 1 o 2 para seleccionar una opción válida.")
        continue

    otra_conversion = input("¿Desea hacer otra conversión? (s/n): ").lower()

    # Si la respuesta no es 's', salir del bucle y finalizar el programa
    if otra_conversion != 's':
        break