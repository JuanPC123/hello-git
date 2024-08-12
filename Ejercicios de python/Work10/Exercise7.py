class Contador:
    def __init__(self):
        self._valor = 0
        self._ultimo_comando = None
    
    def reset(self):
        self._valor = 0
        self._ultimo_comando = "reset"
    
    def inc(self):
        self._valor += 1
        self._ultimo_comando = "incremento"
    
    def dec(self):
        self._valor -= 1
        self._ultimo_comando = "decremento"
    
    def valor_actual(self, nuevo_valor=None):
        if nuevo_valor is not None:
            self._valor = nuevo_valor
            self._ultimo_comando = "actualizacion"
        return self._valor
    
    def ultimo_comando(self):
        return self._ultimo_comando

# Crear tres instancias de la clase Contador
contador_uno = Contador()
contador_dos = Contador()
contador_tres = Contador()

# Prueba con el contador_uno
contador_uno.valor_actual(10)
contador_uno.inc()
contador_uno.inc()
contador_uno.dec()
contador_uno.inc()
print(contador_uno.valor_actual())  # Debe imprimir 12
print(contador_uno.ultimo_comando())  # Debe imprimir "incremento"

# Prueba con el contador_dos
contador_dos.valor_actual(17)
contador_dos.dec()
contador_dos.dec()
contador_dos.dec()
contador_dos.inc()
print(contador_dos.valor_actual())  # Debe imprimir 15
print(contador_dos.ultimo_comando())  # Debe imprimir "incremento"

# Prueba con el contador_tres
contador_tres.valor_actual(1)
contador_tres.inc()
contador_tres.dec()
contador_tres.dec()
contador_tres.inc()
print(contador_tres.valor_actual())  # Debe imprimir 1
print(contador_tres.ultimo_comando())  # Debe imprimir "incremento"
