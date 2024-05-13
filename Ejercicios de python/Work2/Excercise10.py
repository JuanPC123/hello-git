string_completo = ""
contador_a = 0

while True:
    caracter = input("Ingrese un caracter: ")

    if len(caracter) != 1 or caracter == "0":
        break

    string_completo += caracter

    if caracter == "a":
        contador_a += 1

porcentaje_a = (contador_a / len(string_completo)) * 100

print("String completo:", string_completo)
print("Porcentaje de caracteres 'a':", porcentaje_a)