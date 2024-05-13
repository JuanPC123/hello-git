#Rango que el usuario quiera
""" n1 = int(input("Coloca un numero de cuantas veces quieras repetir: "))


for i in range (0,n1+1): 
    print(f"vamos en la letra: {i}")
    i += 1
     """
#contador 
""" contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    if contador > 8:
        break
    print(f"voy en numero {contador}") """
#-------------------------------------------------------------------------------------------
#arreglo letras
#.append sirve para agregar un nuevo objeto al final de la lista
#len para ver la cantidad de caracteres que tiene la variable
#.pop es para eliminar la posicion 
#.remove es para eliminar algo en especifico 
""" Arreglo_Letras = [12, 13, 14, 15, True, False, (1, 2 ,3 ,4,['Jack', 'lola'])]
Arreglo_Letras.append("final")

print(f"total de elementos en el arreglo: {len(Arreglo_Letras)}")
print(f"Ultima posicion del arreglo es: {len(Arreglo_Letras)-1}")
i = 0
while i <  len(Arreglo_Letras):
    print(f"Voy en la posicion {i} y tiene el valor: {Arreglo_Letras[i]}")
    i = i + 1
 """
""" numero_uno = [1,2,3,4, "hola","hola"]
numero_dos = [10,20,5,30,40]
numero_uno.pop(3)
numero_uno.remove("hola")
print(numero_uno) """

#--------------------------------------------------------------------------------------------
#Tuplas
#Parecidas a los arreglos(listas), pero las tuplas no se pueden modificar, o agregar de otra manera  si no es directa
""" thistuple = ("Apple", "Banana","Orange")
print(thistuple[1]) """
#--------------------------------------------------------------------------------------------
