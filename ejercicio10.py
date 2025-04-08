#Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una
#variable auxiliar para hacerlo.

a = 20
b = 50

print("Antes del intercambio:")
print("a =", a)
print("b =", b)

aux = a
a = b
b = aux

print("Después del intercambio:")
print("a =", a)
print("b =", b)