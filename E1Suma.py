# Supongamos que tienes una matriz llamada 'matriz'
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializar la variable suma
suma = 0

# Recorrer cada fila de la matriz
for fila in matriz:
    # Recorrer cada elemento de la fila y sumarlo a la variable suma
    for elemento in fila:
        suma += elemento

# Imprimir el resultado
print("La suma total de los elementos de la matriz es:", suma)