def temperatura_promedio_ciudad(temperaturas):
    temperaturas_promedio = []

    # Recorrer las temperaturas de cada ciudad
    for ciudad in temperaturas:
        suma_temperaturas_ciudad = 0
        total_dias_ciudad = 0

        # Recorrer las semanas de cada ciudad
        for semana in ciudad:
            suma_temperaturas_ciudad += sum(semana)
            total_dias_ciudad += len(semana)

        # Calcular el promedio de temperatura de la ciudad y agregarlo a la lista
        promedio_ciudad = suma_temperaturas_ciudad / total_dias_ciudad
        temperaturas_promedio.append(round(promedio_ciudad, 2))

    return temperaturas_promedio


# Datos de temperaturas de 3 ciudades durante 4 semanas
temperaturas = [
    [  # Ciudad 1
        [18, 20, 21, 23, 21, 20, 20],  # Semana 1
        [18, 23, 21, 21, 23, 21, 24],  # Semana 2
        [23, 21, 23, 21, 24, 21, 17],  # Semana 3
        [21, 20, 23, 21, 22, 19, 17]  # Semana 4
    ],
    [  # Ciudad 2
        [12, 10, 13, 11, 12, 14, 11],  # Semana 1
        [16, 12, 12, 10, 13, 10, 14],  # Semana 2
        [14, 10, 12, 11, 10, 12, 11],  # Semana 3
        [13, 15, 14, 12, 15, 14, 11]  # Semana 4
    ],
    [  # Ciudad 3
        [22, 21, 23, 24, 22, 21, 20],  # Semana 1
        [19, 20, 21, 22, 21, 20, 19],  # Semana 2
        [23, 22, 23, 24, 23, 21, 20],  # Semana 3
        [20, 19, 21, 20, 22, 20, 19]  # Semana 4
    ]
]

# Calcular temperatura promedio de cada ciudad
temperaturas_promedio = temperatura_promedio_ciudad(temperaturas)

# Imprimir resultados
for i, promedio in enumerate(temperaturas_promedio):
    print(f"Temperatura promedio de la Ciudad {i + 1}: {promedio} grados Celsius")