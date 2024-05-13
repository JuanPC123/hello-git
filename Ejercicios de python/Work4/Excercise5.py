def contar_divisores(numero):
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    return divisores

numeros = []
while True:
    numero = int(input("Ingrese un número entero (ingrese un número que comience con 9 para terminar): "))
    if str(numero).startswith("9"):
        break
    numeros.append(numero)

contador = 0
for numero in numeros:
    if contar_divisores(numero) == 2:
        contador += 1

print(f"La cantidad de números con solo dos divisores es: {contador}")