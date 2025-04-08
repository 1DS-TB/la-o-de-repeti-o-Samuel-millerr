# Exercício 03 - Tabuada

numero = int(input("Insira o número para realizar a tabuada: "))

print(f"\nA tabuada do número {numero} é: ")
for i in range(10):
    print(f"{numero} * {i + 1} = {numero * (i+1)}")