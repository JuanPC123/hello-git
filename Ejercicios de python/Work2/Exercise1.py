frase = input("Ingresa una frase: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print("La frase contiene", contador, "vocales.")