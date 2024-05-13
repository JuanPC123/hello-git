class Persona:
    def __init__(self, nombre, edad, dni, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo.upper()  # Convertir a mayúsculas para evitar problemas de entrada
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 20:
            return -1
        elif 20 <= imc <= 25:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        return self.edad >= 18

    def comprobarSexo(self, sexo):
        if sexo.upper() in ['H', 'M']:
            self.sexo = sexo.upper()
        else:
            self.sexo = 'H'  # Por defecto, si el sexo introducido no es correcto, se establece como 'H'

# Ejemplo de uso
if __name__ == "__main__":
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    dni = input("Ingrese el DNI de la persona: ")
    sexo = input("Ingrese el sexo de la persona (H para hombre, M para mujer): ")
    peso = float(input("Ingrese el peso de la persona (en kg): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))

    persona = Persona(nombre, edad, dni, sexo, peso, altura)

    print("\nResultado del cálculo del IMC:")
    resultado_imc = persona.calcularIMC()
    if resultado_imc == -1:
        print("La persona está por debajo de su peso ideal.")
    elif resultado_imc == 0:
        print("La persona está en su peso ideal.")
    else:
        print("La persona tiene sobrepeso.")

    if persona.esMayorDeEdad():
        print("La persona es mayor de edad.")
    else:
        print("La persona es menor de edad.")

    print("Sexo de la persona:", persona.sexo)
