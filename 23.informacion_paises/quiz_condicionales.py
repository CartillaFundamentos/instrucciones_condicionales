
print("Países disponibles--------Código")
print("Colombia--------------------1")
print("India-----------------------2")
print("Brasil----------------------3")
print("España----------------------4")
print("China-----------------------5")

# input
country_code = int(input("Ingrese el código de país: "))

# processing & output
if country_code == 1:
    print("País: Colombia")
    print("Capital: Bogotá")
    print("Continente: Sudamérica")
    print("Idioma: Español")
    print("Religión: Mayoritariamente el Cristianismo")
    print("Moneda oficial: Peso colombiano")
elif country_code == 2:
    print("País: India")
    print("Capital: Nueva Delhi")
    print("Continente: Asia del Sur")
    print("Idiomas: Hindi e inglés")
    print("Religión: Mayoritariamente el Hinduismo")
    print("Moneda oficial: Rupia india")
elif country_code == 3:
    print("País: Brasil")
    print("Capital: Brasilia")
    print("Continente: Sudamérica")
    print("Idioma: Portugués")
    print("Religión: Mayoritariamente el Cristianismo")
    print("Moneda oficial: Real brasileño")
elif country_code == 4:
    print("País: España")
    print("Capital: Madrid")
    print("Continente: Europa")
    print("Idioma: Español")
    print("Religión: Mayoritariamente el Cristianismo")
    print("Moneda oficial: Euro")
elif country_code == 5:
    print("País: China")
    print("Capital: Pekín")
    print("Continente: Asia")
    print("Idioma: Mandarín")
    print("Religiones: Mayoritariamente budismo, el taoísmo, el confucianismo y la religión tradicional china")
    print("Moneda oficial: Yuan")
else:
    print("Entrada no válida")    