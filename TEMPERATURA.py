# Matriz de 3 Dimensiones para datos de temperaturas
# Primera dimensión: Ciudad
# Segunda dimensión: Días de la semana
# Tercera dimensión: Semanas

temperaturas = [
    [   # Ciudad 1
        [18, 20, 21, 23, 21, 20, 20],  # Semana 1
        [18, 23, 21, 21, 23, 21, 24],  # Semana 2
        [23, 21, 23, 21, 24, 21, 17],  # Semana 3
        [21, 20, 23, 21, 22, 19, 17]   # Semana 4
    ],
    [   # Ciudad 2
        [12, 10, 13, 11, 12, 14, 11],  # Semana 1
        [16, 12, 12, 10, 13, 15, 14],  # Semana 2
        [14, 10, 12, 11, 10, 12, 11],  # Semana 3
        [13, 15, 14, 12, 15, 14, 11]   # Semana 4
    ],
]

# Calcular promedio de temperaturas
for primera_ciudad, ciudad in enumerate(temperaturas):
    for primera_semana, semana in enumerate(ciudad):
        suma = sum(semana)
        promedio = round (suma / len(semana),2)
        print("Promedio de temperatura para Ciudad", primera_ciudad +1, "Semana",primera_semana + 1, ":", promedio)
