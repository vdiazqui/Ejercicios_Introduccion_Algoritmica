def obtener_area_triangulo(lado, altura_sobre_lado):
#     Calcula el área de un triángulo utilizando la longitud de uno de sus lados y la altura relativa a ese lado.
    """
    La fórmula para calcular el área de un triángulo es (base * altura) / 2, donde
    la 'base' es la longitud del lado del triángulo, y la 'altura' es la altura relativa
    a ese lado.

    Args:
        lado (float): Longitud del lado del triángulo.
        altura_sobre_lado (float): Altura del triángulo relativa al lado proporcionado.

    Returns:
        float: El área del triángulo.
    """
    return (lado * altura_sobre_lado) / 2

def solicitar_datos(mensaje):
# Solicita al usuario un valor numérico positivo, mostrando un mensaje personalizado.

    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un valor mayor a 0.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

# Solicitar al usuario la longitud del lado y la altura relativa a ese lado
longitud_lado = solicitar_datos("Ingrese la longitud del lado del triángulo (metros): ")
altura_relativa = solicitar_datos("Ingrese la altura relativa a ese lado del triángulo (metros): ")

# Calcular el área del triángulo
area = obtener_area_triangulo(longitud_lado, altura_relativa)

# Mostrar el resultado
print(f"El área del triángulo es: {area} metros cuadrados.")
