def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

numeros_impares = 0

while True:
    numero = int(input("Ingrese un número entero: "))
    if suma_digitos(numero) > 1000 or numero % 5 == 0:
        break
    if numero % 2 != 0:
        numeros_impares += 1

print("Cantidad de números impares ingresados:", numeros_impares)