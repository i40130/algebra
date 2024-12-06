def imprimir_matriz(A):
    for fila in A:
        print(["{:.6f}".format(x) for x in fila])
    print()


# Lectura de la matriz por columnas
A = [[0.0 for _ in range(4)] for _ in range(4)]
for c in range(4):
    col_str = input(f"Introduzca la columna {c} (4 valores separados por comas): ")
    valores = col_str.split(',')
    # Convertir a float
    valores = [float(v) for v in valores]
    for r in range(4):
        A[r][c] = valores[r]

print("\nMatriz inicial:")
imprimir_matriz(A)

# Eliminación Gaussiana con pivotaje parcial escalado (reescalando en cada etapa)
scale = [0.0] * 4

for k in range(3):  # k = 0 a 2
    # Mostrar submatriz activa
    print(f"Etapa {k + 1}: Considerando la submatriz activa desde fila {k} a 3 y columna {k} a 3:")
    imprimir_matriz([fila[k:] for fila in A[k:]])

    # Calcular escala para las filas activas
    for i in range(k, 4):
        max_abs = 0.0
        for j in range(k, 4):
            val = abs(A[i][j])
            if val > max_abs:
                max_abs = val
        scale[i] = max_abs

    print("Vector de escalas para las filas activas:")
    for i in range(k, 4):
        print(f"scale[{i}] = {scale[i]}")
    print()

    # Seleccionar pivote con pivotaje parcial escalado
    pivot_row = k
    max_ratio = 0.0

    # Calcular y mostrar los ratios
    ratios = []
    for i in range(k, 4):
        if scale[i] != 0:
            ratio = abs(A[i][k]) / scale[i]
        else:
            ratio = 0.0
        ratios.append((i, ratio))

    print("Ratios calculados para la selección del pivote:")
    for (fila_idx, r_val) in ratios:
        print(f"Fila {fila_idx} => ratio = {r_val}")
    print()

    # Determinar la fila pivote a partir de los ratios
    for (fila_idx, r_val) in ratios:
        if r_val > max_ratio:
            max_ratio = r_val
            pivot_row = fila_idx

    print(f"Fila pivote seleccionada: {pivot_row}")
    if pivot_row != k:
        # Intercambio de filas
        A[k], A[pivot_row] = A[pivot_row], A[k]
        scale[k], scale[pivot_row] = scale[pivot_row], scale[k]
        print(f"Se intercambian las filas {k} y {pivot_row}:")
        imprimir_matriz(A)

    # Normalizar pivote
    pivot_value = A[k][k]
    if pivot_value == 0:
        print("Advertencia: pivote = 0, no se puede continuar.")
        break
    for j in range(k, 4):
        A[k][j] = A[k][j] / pivot_value

    print(f"Normalización de la fila pivote, ahora A[{k}][{k}] = 1:")
    imprimir_matriz(A)

    # Eliminación para generar ceros debajo del pivote
    for i in range(k + 1, 4):
        m = A[i][k]
        for j in range(k, 4):
            A[i][j] = A[i][j] - m * A[k][j]

    print("Después de la eliminación para generar ceros debajo del pivote:")
    imprimir_matriz(A)

# Ahora que ya tenemos la matriz triangular superior, normalizamos la última fila
# para que A[3][3] sea 1, garantizando que toda la diagonal principal sea 1.
ultima_pivote = A[3][3]
if ultima_pivote != 0:
    for j in range(3, 4):
        A[3][j] = A[3][j] / ultima_pivote

print("Matriz final (triangular superior) obtenida:")
imprimir_matriz(A)