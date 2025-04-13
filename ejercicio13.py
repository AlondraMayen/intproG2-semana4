salario_actual = float(input("Ingrese el salario actual: "))
incremento = salario_actual * 0.08
descuento = salario_actual * 0.025
nuevo_salario = salario_actual + incremento - descuento

print("Nuevo salario:", nuevo_salario)