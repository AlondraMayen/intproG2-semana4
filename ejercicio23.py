lunes = float(input("Tiempo del lunes (en minutos): "))
miercoles = float(input("Tiempo del miércoles (en minutos): "))
viernes = float(input("Tiempo del viernes (en minutos): "))

promedio_tiempo = (lunes + miercoles + viernes) / 3

print("Tiempo promedio de recorrido en la semana:", promedio_tiempo, "minutos")