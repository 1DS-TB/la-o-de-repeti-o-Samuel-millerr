# Exercício 09 - Número Perfeito

for numero in range(1, 10000):
    divisores = []
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores.append(divisor)
    if sum(divisores) == numero:
        print(numero)
