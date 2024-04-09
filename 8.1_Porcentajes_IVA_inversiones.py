def calcular_total_con_iva(importe_base, tasa_iva):
# Calcula el total después de agregar el IVA a un importe base.
    """
    Args:
        importe_base (float): El precio del producto sin IVA.
        tasa_iva (float): El porcentaje de IVA aplicable.

    Returns:
        float: El precio total con el IVA incluido, redondeado a dos decimales.
    """
    total_iva_incluido = importe_base * (1 + tasa_iva / 100)
    return round(total_iva_incluido, 2)

def solicitar_valor(mensaje):
# Solicita al usuario un valor numérico y verifica que sea un número válido.

    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

# Pedir al usuario que introduzca los datos necesarios
base_sin_iva = solicitar_valor("Introduzca el importe sin IVA: ")
iva = solicitar_valor("Introduzca el porcentaje de IVA: ")

# Usar la función para calcular el importe total con IVA
total = calcular_total_con_iva(base_sin_iva, iva)

# Imprimir el resultado
print(f"El importe total con el IVA incluido es: {total}")

