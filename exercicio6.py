# Exercício 06 - Sequência de Fibonacci

numero = int(input("Digite a quantidade de números de fibonacci que você deseja saber: "))
if numero > 0:
    x = 0
    fibonacci = 1
    posicao = 0
    while posicao < numero:
        x, fibonacci = x+fibonacci, x
        if fibonacci == 0:
            print(f"{fibonacci}", end="")
        else:
            print(f", {fibonacci}", end="")
        posicao += 1
else:
    print("INVALIDO")

