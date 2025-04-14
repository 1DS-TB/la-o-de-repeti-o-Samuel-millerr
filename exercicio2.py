# Exercício 02 - Soma de números

numero = int(input("Insira um número intero positivo: "))

if numero >= 0:
    contador = 1
    soma = 0
    while contador <= numero:
        soma = soma + contador
        contador += 1
    print(soma)
else:
    print("INVALIDO")