total_mujeres = int(input("Ingrese la cantidad de mujeres: "))
total_varones = int(input("Ingrese la cantidad de varones: "))
total_estudiantes = total_mujeres + total_varones

porcentaje_mujeres = (total_mujeres / total_estudiantes) * 100
porcentaje_varones = (total_varones / total_estudiantes) * 100

print("Porcentaje de mujeres:", porcentaje_mujeres, "%")
print("Porcentaje de varones:", porcentaje_varones, "%")