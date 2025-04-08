presupuesto_total = float(input("Ingrese el monto total del presupuesto: "))

urgencias = presupuesto_total * 0.37
pediatria = presupuesto_total * 0.42
traumatologia = presupuesto_total * 0.21

print("Urgencias recibe:", urgencias)
print("Pediatría recibe:", pediatria)
print("Traumatología recibe:", traumatologia)