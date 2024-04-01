import time
import random

# Función para imprimir el estado actual del juego
def imprimir_estado(espacio_aereo, aviones):
    print("Espacio aéreo:")
    for fila in espacio_aereo:
        print("".join(fila))
    print("\nAviones:")
    for avion in aviones:
        print(avion)

# Función para mover los aviones hacia abajo
def mover_aviones(espacio_aereo, aviones):
    for i in range(len(aviones)):
        aviones[i][0] += 1
        if aviones[i][0] >= len(espacio_aereo):
            aviones[i][0] = 0

# Función principal del juego
def juego_controlador_trafico_aereo():
    # Tamaño del espacio aéreo
    filas = 10
    columnas = 10

    # Inicializar el espacio aéreo
    espacio_aereo = [['.' for _ in range(columnas)] for _ in range(filas)]

    # Lista para almacenar las coordenadas de los aviones [fila, columna]
    aviones = []

    # Bucle principal del juego
    while True:
        # Limpiar el espacio aéreo
        for fila in espacio_aereo:
            fila[:] = ['.'] * columnas

        # Generar un nuevo avión aleatorio
        if random.random() < 0.1:  # Probabilidad de generar un nuevo avión
            avion_nuevo = [0, random.randint(0, columnas - 1)]
            aviones.append(avion_nuevo)

        # Actualizar la posición de los aviones
        mover_aviones(espacio_aereo, aviones)

        # Imprimir el estado actual del juego
        imprimir_estado(espacio_aereo, aviones)

        # Esperar un tiempo antes de la próxima actualización
        time.sleep(0.5)

# Iniciar el juego
juego_controlador_trafico_aereo()