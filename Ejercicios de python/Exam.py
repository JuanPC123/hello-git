nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana"]
apellidos = ["Gómez", "López", "Pérez", "Rodríguez", "Fernández", "Martínez"]
edades = [20, 22, 21, 19, 23, 20]
altura_cm = [170, 165, 180, 175, 160, 170]
semestre = [3, 4, 2, 1, 5, 3]
materias_cursando = ["Matemáticas,Física", "Matemáticas,Física","Matemáticas,Física","Matemáticas,Física","Matemáticas,Física","Matemáticas,Física" ]

def descripcion_alumno(posicion):
    nombre = nombres[posicion]
    apellido = apellidos[posicion]
    edad = edades[posicion]
    altura = altura_cm[posicion]
    sem = semestre[posicion]
    materias = materias_cursando[posicion]

    return f"{nombre} {apellido} con edad {edad} y una altura de {altura} centimetros, semestre {sem} y esta cursando estas {materias}  materias"

#---------------------------------------------------------------------------------------------------------

def crear_alumno():
    nombre = str(input("Ingrese el nombre del alumno: "))
    apellido = str(input("Ingrese el apellido del alumno: "))
    edad = int(input("Ingrese la edad del alumno: "))
    altura = int(input("Ingrese la altura del alumno en centímetros: "))
    sem = str(input("Ingrese el semestre del alumno: "))
    materias = str(input("Ingrese las materias que está cursando el alumno: "))

    nombres.append(nombre)
    apellidos.append(apellido)
    edades.append(edad)
    altura_cm.append(altura)
    semestre.append(sem)
    
    materias_cursando.append(materias.split(","))

    return f"El alumno agregado es: {descripcion_alumno(len(nombres)-1)}"

print(crear_alumno())

#------------------------------------------------------------------------------------------------------------

def construir_salon(total_alumnos):
    print("Alumno a ingresar: ")
    for _ in range(total_alumnos):
        print(crear_alumno())
construir_salon(1)

#-----------------------------------------------------------------------------------------------------------

def traer_altura_mayor_que(altura):
    nombres_altos = []
    for i in range(len(nombres)):
        if altura_cm[i] >= altura:
            nombres_altos.append(nombres[i])
    return nombres_altos

altura_ingresada = int(input("Ingrese la altura en centímetros: "))
nombres_altos = traer_altura_mayor_que(altura_ingresada)
print("Los nombres de las personas con altura mayor o igual a", altura_ingresada, "son:", nombres_altos)
