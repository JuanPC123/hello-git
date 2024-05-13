Age = int(input("Ingresa tu edad: "))
Buy = int(input("Productos comprados: "))

if Age >= 18 and Buy >= 1:
    print("Eres mayor de edad, Tienes descuento")
elif Age >= 18 and Buy == 0:
    print("Eres mayor de edad, Compra un producto")
else:
    print("Eres menor de edad, No tienes descuento")