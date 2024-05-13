cadena = input("Ingrese una cadena de caracteres: ")

letras = 0
simbolos = 0
digitos = 0
multiplos_de_4 = 0

for caracter in cadena:
    if caracter.isalpha():
        letras += 1
    elif caracter.isdigit():
        digitos += 1
        if int(caracter) % 4 == 0:
            multiplos_de_4 += 1
    else:
        simbolos += 1

print("Cantidad de letras:", letras)
print("Cantidad de símbolos:", simbolos)
print("Cantidad de dígitos:", digitos)
print("Cantidad de dígitos múltiplos de 4:", multiplos_de_4)