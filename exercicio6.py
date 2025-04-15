# Exercício 06 - Sequência de Fibonacci

numero = int(input("Digite a quantidade de números de fibonacci que você deseja saber: "))
if numero > 0:
    x = 0
    fibonacci = 1
    posicao = 0
    while posicao < numero:
        x, fibonacci = x+fibonacci, x
        print(fibonacci)
        posicao += 1
else:
    print("INVALIDO")
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
