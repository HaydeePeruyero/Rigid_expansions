import itertools
from simplicial import *
from itertools import combinations


def triangulacion_binaria(triangulos, vertices):
    # Proporcionar lista de triangulos en formato [(v1,v2,v3),(v4,v5,v6),...]
    # Proporcionar lista de vertices en formato [v1,v2,v3,v4,v5,v6,...]
    # Se obtendrá al final la lista de triangulos, lista de aristas y lista de triangulos en ese orden.
    dic_triang_aris = {}
    aristas_set = set()

    for triang in triangulos:
        longitud = len(triang)
        aristas = []
        for i in range(longitud):
            arista = tuple(sorted([triang[i], triang[(i + 1) % longitud]]))
            aristas.append(arista)
            dic_triang_aris[triang] = aristas
            aristas_set.add(arista)

    aristas_unicas = list(aristas_set)

    ultimo_vertice = max(max(t) for t in triangulos)
    vertices_nuevos = []
    dic_aris_vert = {}

    for i in range(len(aristas_unicas)):
        vert = ultimo_vertice + i + 1
        vertices_nuevos.append(vert)
        dic_aris_vert[vert] = aristas_unicas[i]

    nuevas_aristas = []
    for i, tupla in enumerate(aristas_unicas):
        vertice = vertices_nuevos[i]
        nueva_arista_1 = (tupla[0], vertice)
        nueva_arista_2 = (tupla[1], vertice)
        nuevas_aristas.extend([nueva_arista_1, nueva_arista_2])

    dic_vertN_t = {}

    for key2, value2 in dic_triang_aris.items():
        keys_dic1 = []
        for tupla in value2:
            keys = [key for key, value in dic_aris_vert.items() if all(elem in value for elem in tupla)]
            keys_dic1.extend(keys)
        dic_vertN_t[key2] = keys_dic1

    aristas_entre_triangulos = []

    for valores in dic_vertN_t.values():
        combinaciones = list(combinations(valores, 2))
        aristas_entre_triangulos.extend(combinaciones)

    vert_fin = vertices + vertices_nuevos
    aristas_fin = nuevas_aristas + aristas_entre_triangulos

    combinaciones_aristas = combinations(aristas_fin, 3)

    triangulos_triangulacion = []

    for combo in combinaciones_aristas:
        vertices_combinados = set()
        for arista in combo:
            vertices_combinados.update(arista)
        if len(vertices_combinados) == 3:
            triangulo = tuple(sorted(vertices_combinados))
            if triangulo not in triangulos_triangulacion:
                triangulos_triangulacion.append(triangulo)

    return triangulos_triangulacion, aristas_fin, vert_fin