# Ejercicio No. 19: Piedra, papel o tijera.

import random

print("1 ---> Piedra")
print("2 ---> Papel")
print("3 ---> Tijera")
bot = random.randint(1, 3)

# input
jugador = int(input("Digite su jugada: "))

# processing
if jugador == bot:
    print("Hubo un empate.") # output

elif jugador == 1 and bot == 3:
    print("Ganaste, piedra le gana a tijera.") # output
elif jugador == 1 and bot == 2:
    print("Perdiste, papel le gana a piedra.") # output

elif jugador == 2 and bot == 1:
    print("Ganaste, papel le gana a piedra.") # output
elif jugador == 2 and bot == 3:
    print("Perdiste, tijera le gana a papel.") # output

elif jugador == 3 and bot == 2:
    print("Ganaste, tijera le gana a papel.") # output
elif jugador == 3 and bot == 1:
    print("Perdiste, piedra le gana a tijera.") # output

else:
    print("Entrada inválida.") # output