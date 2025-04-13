# Exercício 06 - Sequência de Fibonacci

numero = int(input("Digite até qual número você deseja saber a sequência de Fibonacci: "))
x = 0
fibonacci = 1
while x <= numero:
    print(x)
    x =  fibonacci-x
    fibonacci = x+fibonacci
