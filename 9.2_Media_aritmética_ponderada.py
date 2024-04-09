def calcular_media_ponderada(valores, pesos):
# Calcula la media ponderada de un conjunto de valores, dados sus pesos.
    """
    La media ponderada se obtiene sumando los productos de cada valor por su peso correspondiente
    y dividiendo el resultado por la suma total de los pesos.
    
    Args:
        valores (list of float): Lista de valores numéricos.
        pesos (list of float): Lista de pesos correspondientes a cada valor.
    
    Returns:
        float: La media ponderada de los valores, redondeada a dos decimales.
    """
    suma_ponderada = sum(valor * peso for valor, peso in zip(valores, pesos))
    total_pesos = sum(pesos)
    return round(suma_ponderada / total_pesos, 2)

def solicitar_valores_y_pesos(n):
#Solicita al usuario ingresar un conjunto de valores y sus pesos.

    valores = []
    pesos = []
    for i in range(1, n + 1):
        valor = float(input(f"Ingrese el valor número {i}: "))
        peso = float(input(f"Ingrese el peso para este valor: "))
        valores.append(valor)
        pesos.append(peso)
    return valores, pesos

# Solicitar al usuario la cantidad de valores a ingresar
n = int(input("¿Cuántos valores desea ingresar?: "))

# Obtener los valores y pesos del usuario
valores, pesos = solicitar_valores_y_pesos(n)

# Calcular la media ponderada
media_ponderada = calcular_media_ponderada(valores, pesos)

# Mostrar la media ponderada
print(f"La media ponderada de los valores ingresados es: {media_ponderada}")
