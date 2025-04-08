#Crea un algoritmo que, dado el año de nacimiento de una persona y el año actual,
#calcule su edad actual y su edad en 10 años.

año_nacimiento = int(input("Ingrese su año de nacimiento:"))
año_actual = int(input("Ingrese el año actual:"))
edad_actual= año_actual-año_nacimiento
edad_futura= edad_actual + 10

print ("Su edad actual es de:", edad_actual)
print ("Su edad en 10 años sera de:", edad_futura)