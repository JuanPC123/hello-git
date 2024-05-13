def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    return palabra == palabra[::-1]  # Comprobar si la palabra es igual a su reverso

contador_palindromos = 0

while True:
    palabra = input("Ingrese una palabra (o 'fin' para terminar): ")
    if palabra == "fin":
        break
    if es_palindromo(palabra):
        contador_palindromos += 1

print("Cantidad de palíndromos ingresados:", contador_palindromos)