# Ejercicio No. 8: Número mayor entre tres números

# input
a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
c = int(input("Digite el tercer número: "))

# processing
if a>b:
    if a>c:
        mayor = a
    else:
        mayor = c
else:
    if b>c:
        mayor = b
    else:
        mayor = c

# output
print("El número mayor es:" + str(mayor))