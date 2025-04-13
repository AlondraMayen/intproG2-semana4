producto1 = float(input("Precio del producto 1: "))
producto2 = float(input("Precio del producto 2: "))
producto3 = float(input("Precio del producto 3: "))

subtotal = producto1 + producto2 + producto3
iva = subtotal * 0.15
total = subtotal + iva

print("Subtotal:", subtotal)
print("IVA (15%):", iva)
print("Total a pagar:", total)