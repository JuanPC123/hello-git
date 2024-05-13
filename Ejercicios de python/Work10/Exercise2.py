#Clase Cuenta(Banco)
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

#Esto se utiliza cuando queremos utilizar el programa directamente, no cuando sea importado como un módulo en otro script
if __name__ == "__main__":
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    cantidad_inicial = float(input("Ingrese la cantidad inicial en la cuenta (opcional): ") or 0)

    cuenta = Cuenta(titular, cantidad_inicial)

    cuenta.mostrar()
    
    cantidad_a_ingresar = float(input("Ingrese la cantidad a ingresar en la cuenta: "))
    cuenta.ingresar(cantidad_a_ingresar)
    print("Después de ingresar:")
    cuenta.mostrar()

    cantidad_a_retirar = float(input("Ingrese la cantidad a retirar de la cuenta: "))
    cuenta.retirar(cantidad_a_retirar)
    print("Después de retirar:")
    cuenta.mostrar()
