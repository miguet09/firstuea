# Creación y escritura del archivo de notas
file = open('my_notes.txt', 'w')
file.write("Estas son mis notas personales:\n")
file.write("1. Recordar comprar leche en el supermercado.\n")
file.write("2. Llamar a Juan para confirmar la cita.\n")
file.close()

# Lectura del archivo de notas
file = open('my_notes.txt', 'r')
print("Contenido del archivo my_notes.txt:")
# Leemos y mostramos cada línea del archivo
for line in file.readlines():
    print(line.strip())  # Eliminamos los espacios en blanco alrededor de la línea
file.close()