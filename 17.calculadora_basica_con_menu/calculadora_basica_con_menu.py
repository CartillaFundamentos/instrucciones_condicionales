# Ejercicio No. 17: Calculadora básica con menú.

from math import log
bandera = False

print("1 ---> Suma (x + y)")
print("2 ---> Resta (x - y)")
print("3 ---> Multiplicación (x * y)")
print("4 ---> División (x ÷ y)")
print("5 ---> Potencia (x ^ y)")
print("6 ---> Logaritmo (base = x, argumento = y)")

# input
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
opcion = int(input("Operación que desea realizar: "))

# processing
if opcion == 1:
    r = x+y
elif opcion == 2:
    r = x-y
elif opcion == 3:
    r = x*y
elif opcion == 4 and y != 0:
    r = x/y
elif opcion == 4 and y == 0:
    bandera = True
elif opcion == 5:
    r = x**y
elif opcion == 6 and x > 0:
    r = log(y, x)
else:
    bandera = True

# output
if bandera == False:
    print("Resultado:", r)
else:
    print("Entrada inválida.")