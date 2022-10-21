# Ejercicio No. 15: Problema de un negocio.

print("Cliente general = g")
print("Cliente afiliado = a")
print("Al contado = c")
print("En plazos = p")

# input
cliente = input("Ingrese el tipo de cliente: ")
monto = int(input("Digite el monto: "))
metodo = input("Ingrese el tipo de pago:")

# processing
if cliente == "g":
    if metodo == "c":
        precio = monto - (monto * 0.15)
    else:
        precio = monto + (monto * 0.1)
else:
    if metodo == "c":
        precio = monto - (monto * 0.2)
    else:
        precio = monto + (monto * 0.05)

# output
print("El total a pagar es de:", precio)