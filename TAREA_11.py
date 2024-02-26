# Definir una matriz 3x3
matriz = [
    [13, 31, 25],
    [65, 47, 61],
    [89, 27, 83]
]

# Imprimir_matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Especificar_fila_para_ordenar
ordenar_fila = 0

# Obtener la longitud de la fila específica
n = len(matriz[ordenar_fila])

# Algoritmo de ordenación
for paso in range(n - 1):
    for comparador in range(0, n - paso - 1):
        # Comparar elementos adyacentes y intercambiar si están en el orden incorrecto
        if matriz[ordenar_fila][comparador] > matriz[ordenar_fila][comparador + 1]:
            matriz[ordenar_fila][comparador], matriz[ordenar_fila][comparador + 1] = matriz[ordenar_fila][comparador + 1], matriz[ordenar_fila][comparador]

# Imprimir_fila ordenada
print("\nMatriz con Fila Ordenada:")
for fila in matriz:
    print(fila)