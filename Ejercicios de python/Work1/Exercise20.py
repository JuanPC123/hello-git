n1 = int(input("Coloca un numero: "))
n2 = int(input("Coloca otro numero: "))
n3 = int(input("Coloca otro numero: "))

if n1 < n2 and n1 < n3:
    print("El numero menor es:",n1)
elif n2 < n1 and n2 < n3:
    print("El numero menor es:",n2)
else:
    print("El numero menor es:",n3)


