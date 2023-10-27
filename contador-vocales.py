# Escribe un programa que solicite una palabra o una oración al usuario
# y cuente la cantidad de vocales (a, e, i, o, u) en esa entrada.
texto = input("Ingrese el texto: ")

a = texto.count('a')
e = texto.count('e')
i = texto.count('i')
o = texto.count('o')
u = texto.count('u')

total = (a + e + i + o + u)

print(f"La vocal 'a' aparece {a} veces.")
print(f"La vocal 'e' aparece {e} veces.")
print(f"La vocal 'i' aparece {i} veces.")
print(f"La vocal 'o' aparece {o} veces.")
print(f"La vocal 'u' aparece {u} veces.")
print(f"El total de vocales es: {total}")