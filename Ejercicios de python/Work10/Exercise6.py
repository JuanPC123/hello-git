class Contador:
    def __init__(self):
        self._valor = 0
    
    def reset(self):
        self._valor = 0
    
    def inc(self):
        self._valor += 1
    
    def dec(self):
        self._valor -= 1
    
    def valor_actual(self, nuevo_valor=None):
        if nuevo_valor is not None:
            self._valor = nuevo_valor
        return self._valor

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
print(contador_uno.valor_actual())  

# Prueba con el contador_dos
contador_dos.valor_actual(17)
contador_dos.dec()
contador_dos.dec()
contador_dos.dec()
contador_dos.inc()
print(contador_dos.valor_actual())

# Prueba con el contador_tres
contador_tres.valor_actual(1)
contador_tres.inc()
contador_tres.dec()
contador_tres.dec()
contador_tres.inc()
print(contador_tres.valor_actual()) 
