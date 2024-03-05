# Se debe proporcionar la lista de vertices=[v1,v2,v3,v4,...]
# La lista de aristas=[(v1,v2),(v2,v3),...]
# Y la lista de triangulos=[(v1,v2,v3),(v2,v3,v4),...]
def caracteristica_euler(vertices, aristas, triangulos):
    # Número de vértices
    V = len(vertices)

    # Número de aristas
    E = len(aristas)

    # Número de caras (triángulos en este caso)
    F = len(triangulos)

    # Calcular la característica de Euler
    euler_characteristic = V - E + F

    return euler_characteristic