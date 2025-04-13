nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: ")) / 100

precio_final = precio_producto - (precio_producto * porcentaje_descuento)

print("Producto:", nombre_producto)
print("Precio final:", precio_final)