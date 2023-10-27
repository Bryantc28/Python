# Escribe un programa que solicite una palabra o una oración al usuario
# y cuente la cantidad de vocales (a, e, i, o, u) en esa entrada.
texto = input("Ingrese el texto: ").lower()

vocales = "aeiou"
conteo_vocales = {vocal: texto.count(vocal) for vocal in vocales}
# print(conteo_vocales)

total_vocales = sum(conteo_vocales.values())

for vocal, cantidad in conteo_vocales.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")

print(f"El total de vocales es: {total_vocales}")
