# Definir_matriz 3x3
matriz = [
    [13, 15, 17],
    [21, 23, 25],
    [31, 35, 37]
]
# Definir_valor
valor = 56
# Realizar_la_busqueda
encontrado = False
for fila in matriz:
    for elemento in fila:
        if elemento == valor:
            encontrado = True
# Mostrar_resultado
if encontrado:
    print("El valor se encontró en la matriz")
else:
    print("El valor no se encontró")
