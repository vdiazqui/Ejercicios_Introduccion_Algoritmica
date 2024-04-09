""" El algoritmo original se aplica perfectamente para determinar el área de un triángulo rectángulo
utilizando las medidas de los lados perpendiculares. En este caso, los dos lados perpendiculares 
funcionan como la base y la altura del triángulo, respectivamente. Por lo tanto, al conocer la 
longitud de estos dos lados, es posible calcular el área del triángulo rectángulo directamente,
considerando uno de los lados como la base y el otro como la altura en la fórmula del área.
"""

def hallar_area_triangulo_recto(cateto1, cateto2):
# Calcula el área de un triángulo rectángulo a partir de las longitudes de sus catetos.
    """
    Utiliza la fórmula área = (cateto1 * cateto2) / 2, donde cateto1 y cateto2 son las
    longitudes de los lados perpendiculares del triángulo rectángulo.

    Args:
        cateto1 (float): Longitud del primer cateto del triángulo rectángulo.
        cateto2 (float): Longitud del segundo cateto del triángulo rectángulo.

    Returns:
        float: El área calculada del triángulo rectángulo.
    """
    return (cateto1 * cateto2) / 2

def pedir_longitud(mensaje):

# Solicita al usuario ingresar la longitud de un lado, asegurando que sea un valor positivo.

    while True:
        try:
            longitud = float(input(mensaje))
            if longitud <= 0:
                print("Ingrese un valor mayor a 0. Intente nuevamente.")
            else:
                return longitud
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Solicitar al usuario la longitud de los dos catetos
cateto1 = pedir_longitud("Ingrese la longitud del primer lado perpendicular (cateto): ")
cateto2 = pedir_longitud("Ingrese la longitud del segundo lado perpendicular (cateto): ")

# Calcular el área del triángulo rectángulo
area = hallar_area_triangulo_recto(cateto1, cateto2)

# Mostrar el resultado
print(f"El área del triángulo rectángulo es: {area}")
