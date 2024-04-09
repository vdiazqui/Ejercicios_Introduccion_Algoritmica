def calcular_interes_inversion(inversion_inicial, interes_anual, duracion_meses):
# Calcula los intereses generados por una inversión dada una tasa de interés anual y una duración en meses.
    """
    Args:
        inversion_inicial (float): El monto inicial invertido.
        interes_anual (float): La tasa de interés anual en porcentaje.
        duracion_meses (int): El tiempo de la inversión en meses.

    Returns:
        float: El monto de intereses generados, redondeado a dos decimales.
    """
    interes_generado = (inversion_inicial * interes_anual / 100) * (duracion_meses / 12)
    return round(interes_generado, 2)

def solicitar_valor_numerico(mensaje, tipo_dato=float):
#Solicita al usuario un valor numérico y verifica que sea un número válido.

    while True:
        try:
            valor = tipo_dato(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un valor mayor a cero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

# Solicitar al usuario los datos necesarios para el cálculo
inversion_inicial = solicitar_valor_numerico("Ingrese el capital invertido: ")
interes_anual = solicitar_valor_numerico("Ingrese la tasa de interés anual (%): ")
duracion_meses = solicitar_valor_numerico("Ingrese el tiempo de la inversión en meses: ", int)

# Calcular el importe de los intereses generados por la inversión
interes_generado = calcular_interes_inversion(inversion_inicial, interes_anual, duracion_meses)

# Mostrar el resultado
print(f"El importe de los intereses generados por la inversión es: {interes_generado}")
