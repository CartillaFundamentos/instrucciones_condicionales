# Ejercicio No. 20: ¿Puede formar un triángulo?

# input
a = float(input("Digite la longitud del lado a: "))
b = float(input("Digite la longitud del lado b: "))
c = float(input("Digite la longitud del lado c: "))

# processing
if a + b > c and a + c> b and b + c >a:
    print("Pueden formar los lados de un triángulo.") # output
else:
    print("No pueden formar los lados de un triángulo.") # output