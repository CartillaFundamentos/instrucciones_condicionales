# Ejercicio No. 9: ¿Es un positivo de 4 dígitos?

# input
num = int(input("Ingrese un número: "))

# processing
if num >= 1000:
    if num < 10000:
        print("Es un positivo de 4 dígitos.") # output
    else:
        print("No es un positivo de 4 dígitos.") # output
else:
    print("No es un positivo de 4 dígitos.") # output