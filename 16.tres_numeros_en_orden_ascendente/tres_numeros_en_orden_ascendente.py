# Ejercicio 16: Organizar tres números en orden ascendente.

# input
a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

# processing
if a > b:
    if a > c:
        if b > c:
            print("Orden:", c, b, a) # output
        else:
            print("Orden:", b, c, a) # output
    else: 
        print("Orden:", b, a, c) # output
else:
    if a > c:
        print("Orden:", c, a, b) # output
    else:
        if b > c:
            print("Orden:", a, c, b) # output
        else:
            print("Orden:", a, b, c) # output