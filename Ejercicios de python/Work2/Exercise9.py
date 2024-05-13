aprobados = 0
total_calificaciones = 0
suma_aprobados = 0

while True:
    respuesta = input("¿Desea analizar calificaciones de alumnos? (S/N): ")
    if respuesta != "S":
        break

    calificacion = float(input("Ingrese la calificación del alumno: "))
    total_calificaciones += 1

    if calificacion > 4:
        aprobados += 1
        suma_aprobados += calificacion

porcentaje_aprobados = (aprobados / total_calificaciones) * 100 if total_calificaciones > 0 else 0
promedio_aprobados = suma_aprobados / aprobados if aprobados > 0 else 0

print(f"Porcentaje de alumnos aprobados: {porcentaje_aprobados}%")
print(f"Promedio de los aprobados: {promedio_aprobados}")