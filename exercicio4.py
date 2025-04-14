# Exercício 04 - Fatorial

numero = int(input("Insira o número intero e positivo para realizar o calculo do fatorial: "))

if numero < 0:
    print("INVALIDO")
else:
    fatorial = 1
    while numero > 1:
        fatorial = fatorial*numero
        numero -= 1
    print(fatorial)
