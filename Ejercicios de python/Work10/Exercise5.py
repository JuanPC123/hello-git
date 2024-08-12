import random
import string

class PasswordManager:
    def __init__(self, password):
        self.password = password

    def esFuerte(self):
        upper_count = sum(1 for char in self.password if char.isupper())
        lower_count = sum(1 for char in self.password if char.islower())
        digit_count = sum(1 for char in self.password if char.isdigit())

        return upper_count > 2 and lower_count > 1 and digit_count > 5

    def generarPassword(self, longitud):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(longitud))

    def seguridadPassword(self):
        longitud = len(self.password)

        if 1 <= longitud <= 6:
            return "Débil"
        elif 7 <= longitud <= 10:
            return "Media"
        elif 11 <= longitud <= 20:
            return "Fuerte"
        else:
            return "Muy Fuerte"

#  >:3
if __name__ == "__main__":

    password = input("Ingrese una contraseña: ")
    manager = PasswordManager(password)

    if manager.esFuerte():
        print("La contraseña es fuerte.")
    else:
        print("La contraseña no es lo suficientemente fuerte.")

    longitud_password = int(input("Ingrese la longitud para generar una nueva contraseña: "))
    nueva_password = manager.generarPassword(longitud_password)
    print("Nueva contraseña generada:", nueva_password)

    print("Nivel de seguridad de la contraseña actual:", manager.seguridadPassword())
