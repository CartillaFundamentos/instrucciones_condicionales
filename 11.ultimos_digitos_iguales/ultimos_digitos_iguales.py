# Ejercicio No. 11: ¿Los últimos dos dígitos son iguales?

# input
num = int(input("Ingrese un número: "))

# processing
digito1 = num % 10
digito2 = (num % 100)//10

if digito1 == digito2:
    print("Son iguales.") # output
else:
    print("No son iguales.") # output