def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
# Pedir al usuario que ingrese el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))

# Llamada a la función proporcionando solo el monto total de la compra
descuento1 = calcular_descuento(monto_total)
monto_final = monto_total - descuento1
print("Monto total:", monto_total)
print("Descuento:", descuento1)
print("Monto final:", monto_total - descuento1)
print()
# Pedir al usuario que ingrese el porcentaje de descuento
porcentaje_descuento2 = float(input("Ingrese el porcentaje de descuento: "))

# Llamada a la función proporcionando tanto el monto total de la compra como el porcentaje de descuento
descuento2 = calcular_descuento(monto_total, porcentaje_descuento2)
monto_final2 = monto_total - descuento2
print("Monto total:", monto_total)
print("Descuento:", descuento2)
print("Monto final:", monto_final2)
