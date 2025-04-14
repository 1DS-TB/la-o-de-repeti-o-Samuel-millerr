# Exercício 05 - Fatorial

numero = int(input("Digite um número para verificar se ele é primo: "))

if numero < 1:
    print("INVALIDO")
else:
    if numero == 1:
        primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

            else:
                primo = True

    if primo:
        print(f"O número {numero} é primo!")
    else:
        print(f"O número {numero} não é primo!")


