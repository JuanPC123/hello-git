def EsPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

suma_pares = 0
suma_impares = 0

for i in range(10):
    numero = int(input("Ingrese un número: "))
    if EsPar(numero):
        suma_pares += numero
    else:
        suma_impares += numero

print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)