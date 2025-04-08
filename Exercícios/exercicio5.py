# Exercício 05 - Fatorial

numero = int(input("Digite um número para verificar se ele é primo: "))

if numero < 1:
    print("INVÁLIDO!")

else:
    lista_resto = []
    for i in range(numero):
        i += 1

        divisao = numero % i
        lista_resto.append(divisao)

    if lista_resto[1] == 1 and lista_resto(len(lista_resto)-1)

print(lista_resto)
