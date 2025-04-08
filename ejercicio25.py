nombre_trabajador = input("Ingrese el nombre del: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))

sueldo_bruto = horas_trabajadas * precio_por_hora
descuento_renta = sueldo_bruto * 0.05
salario_neto = sueldo_bruto - descuento_renta

print("\nResumen del pago:")
print("Trabajador:", nombre_trabajador)
print("Sueldo bruto:", sueldo_bruto)
print("Descuento por renta (5%):", descuento_renta)
print("Salario a pagar:", salario_neto)