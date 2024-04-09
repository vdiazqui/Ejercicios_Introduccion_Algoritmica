class CuentaConDescubierto:
# Definición de la clase CuentaConDescubierto (asegúrate de tener esta clase definida en tu script)
    def __init__(self, titular, saldo_inicial=0.0, limite_descubierto=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_descubierto = limite_descubierto

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self.saldo:.2f} EUR.")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser mayor que cero.")
            return

        if self.saldo - cantidad >= -self.limite_descubierto:
            self.saldo -= cantidad
            print(f"Retiro realizado. Nuevo saldo: {self.saldo:.2f} EUR.")
            if self.saldo < 0:
                print(f"Advertencia: La cuenta está en descubierto por {-self.saldo:.2f} EUR.")
        else:
            print("Error: La operación excede el límite de descubierto permitido.")

# Crear una instancia de la clase y realizar algunas operaciones
mi_cuenta = CuentaConDescubierto("Juan Pérez", 100.0, 50.0)  # Inicializa la cuenta con 100 EUR y un límite de descubierto de 50 EUR

# Realizar operaciones
mi_cuenta.depositar(200)  # Intenta depositar 200 EUR
mi_cuenta.retirar(50)     # Intenta retirar 50 EUR
mi_cuenta.retirar(300)    # Intenta retirar 300 EUR, excediendo el límite de descubierto

# Observa los mensajes impresos para ver el resultado de estas operaciones
