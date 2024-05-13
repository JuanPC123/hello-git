letra = input("Ingrese una letra: ")

if len(letra) > 1:
    print("No se puede ingresar más de una letra.")
else:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Es una vocal.")
    else:
        print("No es una vocal.")