class Cuenta:
# Representa una cuenta de depósito bancario básica.

    def __init__(self, titular, saldo_inicial=0.0):
    # Inicializa una nueva cuenta con un titular y un saldo inicial.
    
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
    # Incrementa el saldo de la cuenta en la cantidad especificada.
    
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self.saldo:.2f} EUR.")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
    # Disminuye el saldo de la cuenta en la cantidad especificada, si hay saldo suficiente.
    
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser mayor que cero.")
            return
        
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retiro realizado. Nuevo saldo: {self.saldo:.2f} EUR.")
        else:
            print("Error: Saldo insuficiente para realizar el retiro.")

# Crear una instancia de la clase Cuenta
mi_cuenta = Cuenta("Ana López", 500.0)  # Inicializa la cuenta con 500 EUR

# Realizar operaciones
mi_cuenta.depositar(250)  # Intenta depositar 250 EUR
mi_cuenta.retirar(100)    # Intenta retirar 100 EUR
mi_cuenta.retirar(700)    # Intenta retirar 700 EUR, lo cual no es posible debido a saldo insuficiente

# Observa los mensajes impresos para ver el resultado de estas operaciones
