# Exercício 07 - Sequência de *

numero = int(input("Digite um número: "))
if numero <= 0:
        print("INVALIDO")
else:
        for i in range(1, numero+1):
                print("*"*i)

