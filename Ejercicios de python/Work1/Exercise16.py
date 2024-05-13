nom = input("Coloca un nombre: ")
nom2 = input("Coloca otro nombre: ")
diferencia_1=nom[0]
diferencia_2=nom[-1]
diferencia_3=nom2[0]
diferencia_4=nom2[-1]
print("la letra es:",diferencia_1)

if diferencia_1==diferencia_3:
    print("las primeras letras son iguales")
elif diferencia_2 == diferencia_4:
    print("Las ultimas letras son iguales ")
else: 
    print("ninguna letra es igual ")