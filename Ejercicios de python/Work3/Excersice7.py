# Solicitar la cantidad objetivo
objetivo = float(input("Ingrese la cantidad que desea ahorrar: "))

# Inicializar el total ahorrado en 0
total_ahorrado = 0

# Solicitar las cantidades a ahorrar hasta alcanzar el objetivo
while total_ahorrado < objetivo:
    cantidad = float(input("Ingrese la cantidad a ahorrar: "))
    total_ahorrado += cantidad

# Imprimir el resultado
print("¡Objetivo alcanzado! Total ahorrado:", total_ahorrado)