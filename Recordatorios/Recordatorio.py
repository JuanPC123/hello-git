#Ejercicios de repaso 11 (7 ejercicios) Solución de problemas con clases Tiempo estimado 20 Horas✍ realizar los siguientes ejercicios: 14. Clase Motor(Motor), 8. Objecto Chimuela1(Chimuela) y 10. Objecto Calculadora(Calculadora)

""" 14. Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos
piden hacer un metodo constructor concentrado en las características del motor. El prototipo
de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 RPM.
La velocidad del auto se calcula así: (rpm / 100) * (0.5 + (cambio / 2)). P.ej. en
tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40.
También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por
kilómetro. A este valor se le aplican los siguientes ajustes:
Si el motor está a más de 3000 rpm, entonces se multiplica por
(rpm - 2500) / 500.
P.ej., a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
Si el motor está en primera, entonces se multiplica por 3.
Si el motor está en segunda, entonces se multiplica por 2.
Los efectos por revoluciones y por cambio se acumulan. P.ej. si el motor está en
primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.
El metodo constructor debe entender estos mensajes:
arrancar(), se pone en primera con 500 rpm.
subirCambio()
bajarCambio()
subirRPM(cuantos)
bajarRPM(cuantos)
velocidad()
consumoActualPorKm() """

class Motor:
    def __init__(self):
        self.cambio = 1
        self.rpm = 5000

    def arrancar(self):
        self.cambio = 3
        self.rpm = 2000

    def subirCambio(self):
        if self.cambio < 5:
            self.cambio += 1

    def bajarCambio(self):
        if self.cambio > 1:
            self.cambio -= 1

    def subirRPM(self, cuantos):
        self.rpm += cuantos

    def bajarRPM(self, cuantos):
        if self.rpm - cuantos >= 0:
            self.rpm -= cuantos

    def velocidad(self):
        return (self.rpm / 100) * (0.5 + (self.cambio / 2))

    def consumoActualPorKm(self):
        base_consumo = 0.05
        ajuste_rpm = (self.rpm - 2500) / 500 if self.rpm > 3000 else 0
        ajuste_cambio = 3 if self.cambio == 1 else 2 if self.cambio == 2 else 1
        return base_consumo * self.cambio * ajuste_rpm * ajuste_cambio
motor = Motor()
motor.arrancar()
motor.subirCambio()
motor.subirRPM(1000)
velocidad_actual = motor.velocidad()
consumo_actual = motor.consumoActualPorKm()
print(f"Velocidad actual: {velocidad_actual}")
print(f"Consumo actual por km: {consumo_actual}")