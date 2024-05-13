def sumatoriaDigitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

numero = 0
while numero != 100:
    numero = int(input("Ingrese un número (ingrese 100 para terminar): "))
    if numero != 100:
        suma_digitos = sumatoriaDigitos(numero)
        print("La suma de los dígitos es:", suma_digitos)