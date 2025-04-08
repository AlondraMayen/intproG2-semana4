tareas = float(input("Ingrese la nota de tareas (sobre 100): "))
examen_parcial = float(input("Ingrese la nota del examen parcial (sobre 100): "))
examen_final = float(input("Ingrese la nota del examen final (sobre 100): "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)

print("Calificación final:", calificacion_final)