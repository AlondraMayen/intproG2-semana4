#Crea un programa en Python que:
#Pida al usuario tres notas (del 0 al 100).

#Calcule el promedio de esas tres notas.
#Muestre el promedio en pantalla.
#Diga si el estudiante aprobó o reprobó (mínimo 60 puntos para aprobar).

nota1 = int(input("Ingrese la primer nota:"))
nota2 = int(input("Ingrese la segunda nota:"))
nota3 = int(input("Ingrese la tercer nota:"))

promedio= (nota1+nota2+nota3)/3

print ("El promedio es:", promedio)