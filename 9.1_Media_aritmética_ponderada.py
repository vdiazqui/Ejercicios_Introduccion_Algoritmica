def calcular_media_aritmetica(valor1, valor2, valor3):
#Calcula la media aritmética de tres valores numéricos.
    """
    Esta función toma tres números como argumentos y devuelve su media aritmética,
    que se obtiene sumando los tres valores y dividiendo el resultado entre tres.

    Args:
        valor1 (float): El primer valor numérico.
        valor2 (float): El segundo valor numérico.
        valor3 (float): El tercer valor numérico.
    
    Returns:
        float: La media aritmética de los tres números, redondeada a dos decimales.
    """
    resultado = (valor1 + valor2 + valor3) / 3
    return round(resultado, 2)

def solicitar_valor_numerico(orden):
#Solicita al usuario ingresar un número, asegurándose de que sea un valor flotante válido.
    while True:
        try:
            valor = float(input(f"Ingrese el {orden} número: "))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número real.")

# Solicitar al usuario los tres números
num1 = solicitar_valor_numerico("primer")
num2 = solicitar_valor_numerico("segundo")
num3 = solicitar_valor_numerico("tercer")

# Calcular la media aritmética de los tres números
media_aritmetica = calcular_media_aritmetica(num1, num2, num3)

# Mostrar la media aritmética calculada
print(f"La media aritmética de los tres números es: {media_aritmetica}")
