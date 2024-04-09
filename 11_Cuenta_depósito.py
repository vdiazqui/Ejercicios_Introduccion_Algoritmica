def obtener_salario_por_hora(salario_bruto_mensual):
# Calcula el salario por hora basado en el salario bruto mensual.
    """
    El cálculo se basa en un año laboral de 52 semanas, repartidas en 12 meses,
    con una jornada laboral de 35 horas semanales.
    
    Args:
        salario_bruto_mensual (float): El salario bruto mensual del empleado.
    
    Returns:
        float: El salario por hora del empleado.
    """
    salario_anual = salario_bruto_mensual * 12
    salario_semanal = salario_anual / 52
    return salario_semanal / 35

def calcular_pago_por_horas_extra(salario_bruto_mensual, horas_extras):
    """
    Calcula el pago por horas extra trabajadas en el mes.
    
    Las primeras 8 horas extra (36ª a 43ª hora) se pagan con un incremento del 125% sobre la tarifa normal.
    Las horas extra a partir de la 44ª se pagan con un incremento del 150% sobre la tarifa normal.
    """
    
    salario_hora = obtener_salario_por_hora(salario_bruto_mensual)
    incremento_36_43 = min(horas_extras, 8)
    incremento_44_en_adelante = max(horas_extras - 8, 0)

    pago_36_43 = incremento_36_43 * salario_hora * 1.25
    pago_44_en_adelante = incremento_44_en_adelante * salario_hora * 1.5

    return pago_36_43 + pago_44_en_adelante

# Solicitar información al usuario
salario_bruto_mensual = float(input("Ingrese su salario bruto mensual: "))
horas_extras = int(input("Ingrese el total de horas extra trabajadas: "))

# Calcular el importe de las horas extra
total_horas_extra = calcular_pago_por_horas_extra(salario_bruto_mensual, horas_extras)

# Mostrar el resultado
print(f"El total a pagar por las horas extra es: {total_horas_extra}")
