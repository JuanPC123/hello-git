""" """ """ #Clase formula
class Formula:
    def sumar(self, entero1, entero2):
        return entero1 + entero2

    def fibonacci(self, cantidad):
        fibonacci_series = [0, 1]
        while len(fibonacci_series) < cantidad:
            next_fib = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_fib)
        return fibonacci_series

    def operacion_modulo(self, cantidad):
        numeros_con_residuo_cero = []
        for num in range(1, cantidad):
            if cantidad % num == 0:
                numeros_con_residuo_cero.append(num)
        return numeros_con_residuo_cero

    def es_primo(self, numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def primos(self, cantidad):
        numeros_primos = []
        current_number = 2
        while len(numeros_primos) < cantidad:
            if self.es_primo(current_number):
                numeros_primos.append(current_number)
            current_number += 1
        return numeros_primos

# >:3
if __name__ == "__main__":
    formula = Formula()

    print("Suma de 5 y 7:", formula.sumar(5, 7))

    cantidad_fibonacci = int(input("Ingrese la cantidad de números Fibonacci a generar: "))
    print("Números Fibonacci:", formula.fibonacci(cantidad_fibonacci))

    cantidad_modulo = int(input("Ingrese un número para calcular los números con residuo 0: "))
    print("Números con residuo 0:", formula.operacion_modulo(cantidad_modulo))

    cantidad_primos = int(input("Ingrese la cantidad de números primos a mostrar: "))
    print("Números primos:", formula.primos(cantidad_primos))
 """