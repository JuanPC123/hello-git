# Solicitar la cantidad objetivo
objetivo = float(input("Ingrese la cantidad que desea ahorrar: "))

# Inicializar el total ahorrado en 0
total_ahorrado = 0

# Ciclo para solicitar las cantidades a ahorrar
while total_ahorrado < objetivo:
    cantidad = float(input("Ingrese la cantidad a ahorrar: "))
    
    # Verificar que la cantidad sea positiva
    if cantidad < 0:
        print("La cantidad debe ser positiva. Inténtelo de nuevo.")
        continue
    
    # Actualizar el total ahorrado
    total_ahorrado += cantidad

# Mostrar el resultado
print("¡Objetivo alcanzado! Total ahorrado:", total_ahorrado)