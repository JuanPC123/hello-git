#Clase Persona
class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Cédula:", self.cedula)

    def es_mayor_de_edad(self):
        return self.edad >= 18

#Esto se utiliza cuando queremos utilizar el programa directamente, no cuando sea importado como un módulo en otro script
if __name__ == "__main__":
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    cedula = input("Ingrese la cédula de la persona: ")

    persona = Persona(nombre, edad, cedula)
    print("\nDatos de la persona:")
    persona.mostrar()

    if persona.es_mayor_de_edad():
        print("La persona es mayor de edad.")
    else:
        print("La persona no es mayor de edad.")
