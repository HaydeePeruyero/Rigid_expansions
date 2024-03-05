import itertools
from simplicial import *
from itertools import combinations

# La siguiente función genera una triangulación de una superficie de genero n
# Regresa tres listas, la de vertices, aristas y triangulos en ese orden.

def generar_triangulacion(genus):
    # Indicar el género de la superficie
    # El polígono tendrá n = 4*g lados
    n = 4 * genus
    g = int(genus)
    # Crear una lista de vértices para el polígono exterior
    vertice_exterior = list([0])

    # Inicializar lista de aristas para la triangulación
    vertice_central = list([1])
    
    # Crear una lista de vértices para el polígono interior
    vertices_interior = list(range(2, n+2))

    #Vertices extrar polígono interior
    vertices_int_extra = list(range(n+2,2*n+2))
    
    # Clases de puntos exteriores
    puntos_ext = list(range(2*n+2,3*n+2))
    
    # Crear 4 listas para cada una de las 4 clases de vértices en las aristas exteriores
    bloques = [puntos_ext[i:i+4] for i in range(0, len(puntos_ext), 4)]

    ai1 = []
    ai2 = []
    bi1 = []
    bi2 = []

    for bloque in bloques:
        parte_1 = [bloque[0]]
        ai1.extend(parte_1)

    for bloque in bloques:
        parte_2 = [bloque[1]]
        ai2.extend(parte_2)

    for bloque in bloques:
        parte_3 = [bloque[2]]
        bi1.extend(parte_3)

    for bloque in bloques:
        parte_4 = [bloque[3]]
        bi2.extend(parte_4)
    
    # Se necesigan 4 listas donde se tengan los diferentes vértices con los que se unirán los vértices exteriores
    bloques_int = [vertices_interior[i:i+4] for i in range(0, len(vertices_interior), 4)]
    
    aux_int_1 = []
    aux_int_2 = []
    aux_int_3 = []
    aux_int_4 = []
    
    for bloque in bloques_int:
        aux1 = [bloque[0],bloque[3]]
        aux_int_1.extend(aux1)
    
    for bloque in bloques_int:
        aux2 = [bloque[1],bloque[2]]
        aux_int_2.extend(aux2)

    for bloque in bloques_int:
        aux3 = [bloque[0],bloque[1]]
        aux_int_3.extend(aux3)
    
    for bloque in bloques_int:
        aux4 = [bloque[2],bloque[3]]
        aux_int_4.extend(aux4)
    
    # Dividir los vértices interiores en pares e impares
    vertices_int_extra_impares = vertices_int_extra[1::2]  # Obtiene los elementos en posiciones impares
    vertices_int_extra_pares = vertices_int_extra[0::2]    # Obtiene los elementos en posiciones pares
    
    # Lista total de vértices
    vertices = []
    
    vertices = vertice_exterior + vertice_central +  vertices_interior + vertices_int_extra + ai1 + ai2 + bi1 + bi2
    
    # Inicializar lista de aristas para la triangulación
    aristas = []
    triangulos = []

    # Agregar aristas del poligono exterior
    for i in range(n):
        v1 = vertice_exterior[0]
        v2 = vertice_central[0]
        v3 = vertices_interior[i]
        v4 = vertices_int_extra[i]
        v9 = vertices_interior[(i+1) % n]
        
        aristas.append((v1, v3))
        aristas.append((v2, v3))
        aristas.append((v2, v4))
        aristas.append((v3, v4))
        aristas.append((v4, v9))
        
    aristas_ext = []
    # Agregar aristas del poligono exterior
    for k in range(g):
        v8 = vertice_exterior[0]
        v10 = ai1[k]
        v11 = ai2[k]
        v12 = bi1[k]
        v13 = bi2[k]
        
        aristas_ext.append((v8, v10))
        aristas_ext.append((v8, v11))
        aristas_ext.append((v10, v11))
        aristas_ext.append((v8, v12))
        aristas_ext.append((v8, v13))
        aristas_ext.append((v12, v13))
                
    ai1_int = []
    ai2_int = []
    bi1_int = []
    bi2_int = []
    
    ai1_aux = []
    ai2_aux = []
    bi1_aux = []
    bi2_aux = []

    for elemento in ai1:
        ai1_aux.extend([elemento, elemento])
    
    for elemento in ai2:
        ai2_aux.extend([elemento, elemento])
    
    for elemento in bi1:
        bi1_aux.extend([elemento, elemento])
    
    for elemento in bi2:
        bi2_aux.extend([elemento, elemento])
    
    for elemento_a, elemento_b in zip(aux_int_1, ai1_aux * len(aux_int_1)):
        ai1_int.append((elemento_a, elemento_b))

    for elemento_a, elemento_b in zip(aux_int_2, ai2_aux * len(aux_int_2)):
        ai2_int.append((elemento_a, elemento_b))
    
    aux_int_3t = aux_int_3[1:] + [aux_int_3[0]]
    
    for elemento_a, elemento_b in zip(aux_int_3t, bi1_aux * len(aux_int_3t)):
        bi1_int.append((elemento_a, elemento_b))

    for elemento_a, elemento_b in zip(aux_int_4, bi2_aux * len(aux_int_4)):
        bi2_int.append((elemento_a, elemento_b))
        
    aristas_int_ord = vertices_int_extra_pares + vertices_int_extra_impares
    
    ai1_ai2 = ai1 + bi1
    ai1_ai2_aux = []
    for elemento in ai1_ai2:
        ai1_ai2_aux.extend([elemento, elemento])
    
    bi1_bi2 = ai2 + bi2
    bi1_bi2_aux = []
    for elemento in bi1_bi2:
        bi1_bi2_aux.extend([elemento, elemento])
    
    ai12_vert_int = []
    bi12_vert_int = []
    
    for j in range(len(ai1_ai2_aux)):
        v5 = aristas_int_ord[j]
        v6 = ai1_ai2_aux[j]
        v7 = bi1_bi2_aux[j]
        ai12_vert_int.append((v5,v6))
        bi12_vert_int.append((v5,v7))
    
    
    aristas_int_ext = ai1_int + ai2_int + bi1_int + bi2_int
    
    edges = aristas + aristas_int_ext + ai12_vert_int + bi12_vert_int + aristas_ext
    
    triangulos = []
    
    vert_int_t = vertices_interior[1:] + [vertices_interior[0]]
    aux_int_13 = aux_int_1+aux_int_3t
    aux_int_24 = aux_int_2+aux_int_4
    
    for l in range(n):
        t1 = vertice_exterior[0]
        t2 = vertice_central[0]
        t3 = vertices_interior[l]
        t4 = vert_int_t[l]
        t10 = vertices_int_extra[l]
        t5 = aristas_int_ord[l]
        t6 = aux_int_13[l]
        t7 = aux_int_24[l]
        t8 = ai1_ai2_aux[l]
        t9 = bi1_bi2_aux[l]
        
        triangulos.append((t2, t3, t10))
        triangulos.append((t2, t4, t10))
        triangulos.append((t1, t6, t8))
        triangulos.append((t1, t7, t9))
        triangulos.append((t5, t8, t9))
        triangulos.append((t6, t5, t8))
        triangulos.append((t7, t5, t9))
        
    
    
    return vertices, edges, triangulos