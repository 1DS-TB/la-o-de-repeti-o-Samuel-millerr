# Exercício 08 - Série Harmônica

limite = int(input("Digite até qual número você gostaria de fazer a série harmônica: "))

numero = 1
serie_harmonica = 0
if limite <= 0 :
    print("INVALIDO")
else:
    while numero <= limite:
        serie_harmonica += 1/numero
        numero += 1
    print(f"{serie_harmonica:.2f}")