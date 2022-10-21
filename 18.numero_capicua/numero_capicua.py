# Ejercicio No. 18: Número capicúa.

# input
num = int(input("Digite un número: "))

# processing
if num > 9999 and num <= 99999:
    dig1 = (num%100000)//10000
    dig2 = (num%10000)//1000
    dig4 = (num%100)//10
    dig5 = num%10
    if dig1 == dig5 and dig2 == dig4:
        print("Es capicúa.") # output
    else:
        print("No es capicúa.") # output
else:
    print("Entrada inválida.") # output