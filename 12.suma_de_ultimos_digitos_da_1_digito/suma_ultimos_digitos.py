# Ejercicio No. 12: ¿La suma de los últimos dos dígitos da un número de un dígito?

# input
num = int(input("Ingrese un número: "))

# processing
digito1 = num%10
digito2 = (num%100)//10
suma = digito1 + digito2

# output
if suma < 10:
    print("El resultado de la suma es un número de un dígito.")
else:
    print("El resultado de la suma no es un número de un dígito.")