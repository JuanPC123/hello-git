total = 0

while True:
    monto = float(input("Ingrese el monto de la compra (ingrese 0 para terminar): "))
    
    if monto < 0:
        print("Monto no valido")
    if monto == 0:
        break
    total += monto
if total > 1000:
    descuento = total * 0.1
    total -= descuento
print("El total a pagar es:", total)