while True:
    password1 = input("Ingrese una contraseña: ")
    password2 = input("Ingrese la contraseña nuevamente: ")

    if password1 == password2:
        print("Contraseña correcta. ¡Acceso concedido!")
        break
    else:
        print("Las contraseñas no coinciden. Inténtelo nuevamente.")