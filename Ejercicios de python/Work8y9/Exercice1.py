class Alumno:
    def _init_(self, nombre, edad, grado, promedio, comportamiento):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.promedio = promedio
        self.comportamiento = comportamiento
    
    def estudiar(self, horas):
        print(f"{self.nombre} está estudiando durante {horas} horas.")
    
    def tomar_examen(self):
        print(f"{self.nombre} está tomando un examen.")
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Grado: {self.grado}")
        print(f"Promedio: {self.promedio}")
        print(f"Comportamiento: {self.comportamiento}")

class Profesor:
    def _init_(self, nombre, edad, especialidad, experiencia, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.experiencia = experiencia
        self.calificacion = calificacion
    
    def dar_clase(self):
        print(f"El profesor {self.nombre} está dando clase.")
    
    def corregir_examen(self):
        print(f"El profesor {self.nombre} está corrigiendo un examen.")
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Experiencia: {self.experiencia} años")
        print(f"Calificación: {self.calificacion}")

class Silla:
    def _init_(self, material, color, numero_patas, estado, confort):
        self.material = material
        self.color = color
        self.numero_patas = numero_patas
        self.estado = estado
        self.confort = confort
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"La silla ahora está {nuevo_estado}.")
    
    def mostrar_caracteristicas(self):
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Número de patas: {self.numero_patas}")
        print(f"Estado: {self.estado}")
        print(f"Nivel de confort: {self.confort}")

class Computadora:
    def _init_(self, marca, modelo, ram, almacenamiento, estado):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.estado = estado
    
    def encender(self):
        self.estado = "Encendida"
        print("La computadora ha sido encendida.")
    
    def apagar(self):
        self.estado = "Apagada"
        print("La computadora ha sido apagada.")
    
    def mostrar_especificaciones(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Estado: {self.estado}")

class Asignatura:
    def _init_(self, nombre, codigo, horario, profesor, estudiantes):
        self.nombre = nombre
        self.codigo = codigo
        self.horario = horario
        self.profesor = profesor
        self.estudiantes = estudiantes
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado a la asignatura {self.nombre}.")
    
    def mostrar_informacion(self):
        print(f"Asignatura: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Horario: {self.horario}")
        print(f"Profesor: {self.profesor.nombre}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante.nombre)

class Horario:
    def _init_(self, dia_semana, hora_inicio, hora_fin, asignaturas):
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.asignaturas = asignaturas
    
    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f"Asignatura {asignatura.nombre} agregada al horario del {self.dia_semana}.")
    
    def mostrar_horario(self):
        print(f"Día: {self.dia_semana}")
        print(f"Hora de inicio: {self.hora_inicio}")
        print(f"Hora de fin: {self.hora_fin}")
        print("Asignaturas:")
        for asignatura in self.asignaturas:
            print(asignatura.nombre)

class Libro:
    def _init_(self, titulo, autor, tema, cantidad_paginas, estado):
        self.titulo = titulo
        self.autor = autor
        self.tema = tema
        self.cantidad_paginas = cantidad_paginas
        self.estado = estado
    
    def abrir(self):
        print(f"El libro '{self.titulo}' está siendo abierto.")
    
    def cerrar(self):
        print(f"El libro '{self.titulo}' está siendo cerrado.")
    
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Tema: {self.tema}")
        print(f"Cantidad de páginas: {self.cantidad_paginas}")
        print(f"Estado: {self.estado}")

class Pizarra:
    def _init_(self, material, color, estado, limpieza):
        self.material = material
        self.color = color
        self.estado = estado
        self.limpieza = limpieza
    
    def escribir(self, contenido):
        print(f"Escribiendo en la pizarra: '{contenido}'.")
    
    def limpiar(self):
        print("Limpiando la pizarra.")
        self.limpieza = "Limpia"
    
    def mostrar_estado(self):
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Estado: {self.estado}")
        print(f"Nivel de limpieza: {self.limpieza}")

class Proyector:
    def _init_(self, marca, modelo, resolucion, estado):
        self.marca = marca
        self.modelo = modelo
        self.resolucion = resolucion
        self.estado = estado
    
    def encender(self):
        print("Encendiendo el proyector...")
        self.estado = "Encendido"
    
    def apagar(self):
        print("Apagando el proyector...")
        self.estado = "Apagado"
    
    def mostrar_especificaciones(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Resolución: {self.resolucion}")
        print(f"Estado: {self.estado}")

class Mesa:
    def _init_(self, material, color, numero_patas, capacidad, estado):
        self.material = material
        self.color = color
        self.numero_patas = numero_patas
        self.capacidad = capacidad
        self.estado = estado
    
    def ocupar(self):
        print("Ocupando la mesa...")
        self.estado = "Ocupada"
    
    def desocupar(self):
        print("Desocupando la mesa...")
        self.estado = "Desocupada"
    
    def mostrar_caracteristicas(self):
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Número de patas: {self.numero_patas}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Estado: {self.estado}")



# Instanciando 5 objetos de cada clase
alumno1 = Alumno("Juan", 15, 10, 8.5, "Bueno")
alumno2 = Alumno("María", 14, 9, 9.2, "Excelente")
alumno3 = Alumno("Pedro", 16, 11, 7.8, "Regular")
alumno4 = Alumno("Ana", 15, 10, 8.9, "Bueno")
alumno5 = Alumno("Luis", 14, 9, 9.5, "Excelente")

profesor1 = Profesor("Carlos", 40, "Matemáticas", 15, "Excelente")
profesor2 = Profesor("Ana", 35, "Historia", 10, "Bueno")
profesor3 = Profesor("Laura", 45, "Ciencias", 20, "Muy Bueno")
profesor4 = Profesor("Diego", 38, "Literatura", 12, "Regular")
profesor5 = Profesor("Sara", 42, "Inglés", 18, "Bueno")

silla1 = Silla("Madera", "Marrón", 4, "En uso", "Alto")
silla2 = Silla("Plástico", "Blanco", 3, "En uso", "Medio")
silla3 = Silla("Metal", "Negro", 4, "En uso", "Alto")
silla4 = Silla("Madera", "Azul", 3, "En uso", "Bajo")
silla5 = Silla("Plástico", "Rojo", 4, "En uso", "Medio")

computadora1 = Computadora("HP", "Pavilion", 8, 512, "Apagada")
computadora2 = Computadora("Dell", "Inspiron", 16, 1024, "Encendida")
computadora3 = Computadora("Lenovo", "ThinkPad", 16, 512, "Apagada")
computadora4 = Computadora("Asus", "ROG", 32, 1024, "Encendida")
computadora5 = Computadora("Apple", "MacBook", 16, 512, "Apagada")

asignatura1 = Asignatura("Matemáticas", "MAT101", "Lunes 08:00 - 10:00", profesor1, [alumno1, alumno2])
asignatura2 = Asignatura("Historia", "HIS101", "Martes 10:00 - 12:00", profesor2, [alumno3, alumno4])
asignatura3 = Asignatura("Ciencias", "CIE101", "Miércoles 08:00 - 10:00", profesor3, [alumno1, alumno5])
asignatura4 = Asignatura("Literatura", "LIT101", "Jueves 10:00 - 12:00", profesor4, [alumno2, alumno3])
asignatura5 = Asignatura("Inglés", "ING101", "Viernes 08:00 - 10:00", profesor5, [alumno4, alumno5])

horario_lunes = Horario("Lunes", "08:00", "12:00", [asignatura1, asignatura3])
horario_martes = Horario("Martes", "08:00", "12:00", [asignatura2, asignatura4])
horario_miercoles = Horario("Miércoles", "08:00", "12:00", [asignatura3, asignatura5])
horario_jueves = Horario("Jueves", "08:00", "12:00", [asignatura4, asignatura1])
horario_viernes = Horario("Viernes", "08:00", "12:00", [asignatura5, asignatura2])

libro1 = Libro("Matemáticas Avanzadas", "Carlos Ruiz", "Matemáticas", 300, "Nuevo")
libro2 = Libro("Historia del Mundo", "Ana Martínez", "Historia", 250, "Usado")
libro3 = Libro("Biología Celular", "Laura Gómez", "Biología", 200, "Nuevo")
libro4 = Libro("Literatura Clásica", "Diego Pérez", "Literatura", 350, "Usado")
libro5 = Libro("Inglés Intermedio", "Sara López", "Inglés", 280, "Nuevo")

pizarra1 = Pizarra("PVC", "Verde", "En uso", "Sucia")
pizarra2 = Pizarra("Acrílico", "Blanco", "En uso", "Limpia")
pizarra3 = Pizarra("Pizarra Digital", "Negro", "En uso", "Limpia")
pizarra4 = Pizarra("Madera", "Negro", "En uso", "Sucia")
pizarra5 = Pizarra("PVC", "Blanco", "En uso", "Limpia")

proyector1 = Proyector("Epson", "PowerLite", "1080p", "Apagado")
proyector2 = Proyector("BenQ", "W1070", "1080p", "Apagado")
proyector3 = Proyector("Sony", "VPL-HW45ES", "1080p", "Apagado")
proyector4 = Proyector("Optoma", "HD143X", "1080p", "Apagado")
proyector5 = Proyector("LG", "PF50KA", "1080p", "Apagado")

mesa1 = Mesa("Madera", "Marrón", 4, 4, "Libre")
mesa2 = Mesa("Plástico", "Blanco", 4, 4, "Libre")
mesa3 = Mesa("Metal", "Negro", 4, 4, "Libre")
mesa4 = Mesa("Madera", "Azul", 4, 4, "Libre")
mesa5 = Mesa("Plástico", "Rojo", 4, 4, "Libre")

# Mostrar información de un alumno en particular

print("\nInformación de un alumno:")
alumno2.mostrar_informacion()

# Mostrar información de un profesor en particular
print("\nInformación de un profesor:")
profesor3.mostrar_informacion()

# Mostrar información de una silla en particular
print("\nInformación de una silla:")
silla4.mostrar_caracteristicas()

# Mostrar información de una computadora en particular
print("\nInformación de una computadora:")
computadora5.mostrar_especificaciones()

# Mostrar información de una asignatura en particular
print("\nInformación de una asignatura:")
asignatura1.mostrar_informacion()

# Mostrar información de un horario en particular
print("\nInformación de un horario:")
horario_viernes.mostrar_horario()

# Mostrar información de un libro en particular
print("\nInformación de un libro:")
libro1.mostrar_informacion()

# Mostrar el estado de una pizarra en particular
print("\nEstado de una pizarra:")
pizarra2.mostrar_estado()

# Mostrar las especificaciones de un proyector en particular
print("\nEspecificaciones de un proyector:")
proyector3.mostrar_especificaciones()

# Mostrar las características de una mesa en particular
print("\nCaracterísticas de una mesa:")
mesa4.mostrar_caracteristicas()    