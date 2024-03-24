#Crear Diccionario con información personal
Informacion_personal = [
    {"Nombre": "Camila", "Apellido": "García", "Ciudad": "Tena", "Edad": (5), "Profesión": "Militar"},
    {"Nombre": "Madeline", "Apellido": "Garcia", "Ciudad": "Tena", "Edad":(12), "Profesion": "Estudiante"},
    {"Nombre": "Mary", "Apellido": "Garcia", "Ciudad": "Tena", "Edad":(14), "Profesion": "Estudiante"},
    {"Nombre": "Juan", "Apellido": "Garcia", "Ciudad": "Tena", "Edad":(15), "Profesion": "Profesor"}
]
#Acceder al valor de las clave "Ciudad" y modificar
Informacion_personal[1]["Ciudad"] = "Quito"
#Agregar nueva clave al registro profesion
Informacion_personal[2]["Profesion"] = "Estudiante"
#Verificar si la clave telefono existe en el primer registro
telephone="telefono"
if telephone not in Informacion_personal:
    print("El telefono no existe")
    #Si no existe, agregar un numero de telefono
    Informacion_personal[0]["telefono"]="0989770724"
#Eliminar la clave "Edad" del registro
del Informacion_personal[0]["Edad"]
print(Informacion_personal [0]["Nombre"])
primera_persona=Informacion_personal[0]
print(primera_persona)