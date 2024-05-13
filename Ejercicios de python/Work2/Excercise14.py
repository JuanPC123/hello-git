def es_multiplo_de_10(numero):
    return numero % 10 == 0

def contiene_cero(numero):
    return '0' in str(numero)

def concatenar_numeros():
    multiplo_de_3 = ''
    contiene_cero = ''
    numero = ''

    while True:
        numero_ingresado = input("Ingrese un número: ")

        if not numero_ingresado.isdigit():
            print("Debe ingresar un número válido.")
            continue

        numero = numero_ingresado

        if int(numero) % 10 == 0 or int(numero) < 0:
            break

        if len(numero) % 3 == 0:
            multiplo_de_3 += numero + '-'

        if '0' in numero:
            contiene_cero += numero + '-'

    print("Números múltiplos de 3: " + multiplo_de_3)
    print("Números que contienen el dígito 0: " + contiene_cero)
