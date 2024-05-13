attempts = 0
password = input("Ingrese una contraseña: ")
confirm_password = input("Confirme la contraseña: ")

while password != confirm_password:
    attempts += 1
    if attempts >= 3:
        print("Ha excedido el número máximo de intentos.")
        break
    print("Las contraseñas no coinciden. Inténtelo de nuevo.")
    confirm_password = input("Confirme la contraseña: ")

if password == confirm_password:
    print("Contraseña confirmada correctamente.")