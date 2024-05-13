numero = int(input("Ingrese un número positivo (0 para finalizar): "))
mayor = 0

while numero != 0:
    if numero > mayor:
        mayor = numero
    numero = int(input("Ingrese otro número positivo (0 para finalizar): "))

print("El mayor número ingresado fue:", mayor)