# Ejercicio No. 7: Costo de llamada telefónica

# input
mins = int(input("Digite los minutos de llamada: "))

# processing
if mins <= 3:
    costo = 300
else:
    costo = (mins-3) * 50 + 300

# output
print("La cantidad a pagar es de $" + str(costo))