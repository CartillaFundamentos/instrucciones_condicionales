# Ejercicio No. 13: Ecuación de primer grado.

print("Ecuación de la forma ax + b = 0")

# input
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

# processing
if a != 0:
    x = -b/a
else: 
    x = "No tiene solución"

# output
print("Resultado:" + str(x))