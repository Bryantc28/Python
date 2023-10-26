texto = input("Texto a verificar: ")

texto = texto.replace(" ", "").lower()
print("Texto sin espacios y en minúsculas:", texto)

texto_invertido = texto[::-1]
print("Texto invertido:", texto_invertido)
    print("Es un palíndromo")

else:
    print("No es un palíndromo")
