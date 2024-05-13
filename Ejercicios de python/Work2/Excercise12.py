numeros_pares = 0
numeros_impares = 0
multiplos_de_tres = 0

while True:
    numero = int(input("Ingrese un número entero positivo (-1 para salir): "))

    if numero == -1:
        break

    digitos_pares = 0
    digitos_impares = 0

    while numero > 0:
        digito = numero % 10

        if digito % 2 == 0:
            digitos_pares += 1
        else:
            digitos_impares += 1

        numero //= 10

    numeros_pares += digitos_pares
    numeros_impares += digitos_impares

    if numero % 3 == 0:
        multiplos_de_tres += 1

print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
print("Cantidad de números múltiplos de 3:", multiplos_de_tres)