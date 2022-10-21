# Ejercicio 14: Ecuación de segundo grado.

print("Ecuación de la forma ax² + bx + c = 0")

# input
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# processing
if a != 0:
    x1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
    print("Los valores de x son", x1, "y", x2) # output
else:
    print("No tiene solución.") # output