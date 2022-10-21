# Ejercicio No. 21: Triángulo equilátero, isósceles o escaleno.

# input
a = float(input("Longitud del lado a: "))
b = float(input("Longitud del lado b: "))
c = float(input("Longitud del lado c: "))

# processing
if a == b == c:
    print("Es equilátero.") # output
elif a == b or a == c or b == c:
    print("Es isósceles.") # output
else:
    print("Es escaleno.") # output