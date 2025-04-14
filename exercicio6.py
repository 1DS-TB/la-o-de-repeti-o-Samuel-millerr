# Exercício 06 - Sequência de Fibonacci

numero = int(input("Digite até qual número você deseja saber a sequência de Fibonacci: "))
if numero > 0:
    x = 0
    fibonacci = 1
    while x <= numero:
        x =  fibonacci-x
        fibonacci = x+fibonacci
        print(x)
else:
    print("INVALIDO")

