def visualizacion(vertices, vertices_ponchaduras, ponchaduras, resolucion, subdivision=0):
    # Parámetros
    n = ponchaduras
    r = 2 * resolucion + 1

    # Dividir la lista en sublistas de tamaño 2n + 1
    sublistas = [vertices[i:i + r] for i in range(0, len(vertices), r)]

    # Diccionario para almacenar las coordenadas
    coordenadas = {}

    # Convertir cada sublista en el formato deseado
    for i, sublista in enumerate(sublistas):
        x_offset = i  # Incremento de x para cada sublista
        for j, elemento in enumerate(sublista):
            coordenadas[elemento] = (x_offset, j)

    # Añadir los vértices adicionales
    esquinas = {
        "0a": (0, r),
        "0c": (n * r, 0),
        "0b": (n * r, r)
    }
    coordenadas.update(esquinas)

    # Filtrar los primeros 2n vértices del primer paquete que tienen x = 0 (excluyendo el (0, 0))
    vertices_horizontales = [coordenadas[key] for key in range(1, r) if coordenadas[key][0] == 0]

    # Crear y agregar nuevos vértices con coordenadas horizontales
    for idx, coord in enumerate(vertices_horizontales, start=1):
        new_key = f"{idx}'"
        new_value = (n * r, coord[1])
        coordenadas[new_key] = new_value 

    # Filtrar los vértices donde y = 0 (excluyendo (0, 0))
    vertices_verticales = [key for key in coordenadas if coordenadas[key][1] == 0 and key != 0 and coordenadas[key] != (n * r, 0)]

    # Crear y agregar nuevos vértices con coordenadas verticales
    for key in vertices_verticales:
        new_key = f"{key}'"
        new_value = (coordenadas[key][0], r)
        coordenadas[new_key] = new_value

    coordenadas_unicas = {}
    valores_vistos = set()

    for key, value in coordenadas.items():
        if value not in valores_vistos:
            valores_vistos.add(value)
            coordenadas_unicas[key] = value

    #Almacenar las coordenadas de los cuadrados en una lista
    #cuadrados = []
    #for i in range
            
    # Graficar las coordenadas
    x = [coordenada[0] for coordenada in coordenadas.values()]
    y = [coordenada[1] for coordenada in coordenadas.values()]
    etiquetas = list(coordenadas.keys())

    plt.figure(figsize=(max(x)+3, max(y)+2))
    plt.scatter(x, y, color='blue')  # Dibujar los puntos

    # Colorear los cuadrados
    for i in range(0, len(vertices_ponchaduras), 4):
        if i + 3 < len(vertices_ponchaduras):  # Asegurarse de que hay cuatro vértices
            square_vertices = [coordenadas[vertices_ponchaduras[j]] for j in range(i, i + 4)]
            square_x = [coord[0] for coord in square_vertices]
            square_y = [coord[1] for coord in square_vertices]
            plt.fill(square_x, square_y, color='gray', alpha=0.5)  # Colorear el cuadrado en gris

    # Añadir etiquetas a cada punto
    for i, etiqueta in enumerate(etiquetas):
        plt.text(x[i] + 0.1, y[i] + 0.1, str(etiqueta), fontsize=12, ha='left', va='bottom')

    # Dibujar líneas horizontales y verticales entre los puntos
    # Agrupar puntos por fila
    filas = {}
    for i in range(len(x)):
        if y[i] not in filas:
            filas[y[i]] = []
        filas[y[i]].append(x[i])

    # Dibujar líneas horizontales
    for y_value, x_values in filas.items():
        plt.plot(x_values, [y_value] * len(x_values), color='gray', linestyle='--')

    # Agrupar puntos por columna
    columnas = {}
    for i in range(len(y)):
        if x[i] not in columnas:
            columnas[x[i]] = []
        columnas[x[i]].append(y[i])

    # Dibujar líneas verticales
    for x_value, y_values in columnas.items():
        plt.plot([x_value] * len(y_values), y_values, color='gray', linestyle='--')

    # Ajustes del gráfico
    plt.xlim(min(x)-2, max(x)+2)
    plt.xlim(min(y)-2, max(y)+2)
    plt.title(f'Toro con {ponchaduras} ponchadura(s) y resolución {r}')
    #plt.grid(True)
    plt.axis('equal')
    plt.xticks([])  # Quitar ticks en el eje x
    plt.yticks([])
    plt.show()