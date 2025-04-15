# Exercício 03 - Tabuada

numero = int(input("Insira o número para realizar a tabuada: "))


if numero >= 1:
    print(f"\nA tabuada do número {numero} é: ")
    for i in range(10):
        print(f"{numero} x {i + 1} = {numero * (i+1)}")
else: print("INVALIDO")

# 5 x 10 = 50