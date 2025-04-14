# Exercício 10 - Números Kaprekar

x = int(input("Insira o de onde começara a contagem: "))
y = int(input("Digite até onde irá a contagem: "))

for numero in range(x, y):
    numero_quadrado = str(numero*numero)
    numero_string = str(numero)
    if numero > 3:
        if len(numero_quadrado) % 2 != 0:
            primeira_parte = numero_quadrado[:len(numero_string)-1]
            segunda_parte = numero_quadrado[len(numero_string)-1:]

            numero_calculado = int(primeira_parte)+int(segunda_parte)
        else:
            primeira_parte = numero_quadrado[:len(numero_string)]
            segunda_parte = numero_quadrado[len(numero_string):]

            numero_calculado = int(primeira_parte)+int(segunda_parte)
    else:
        if numero == 1:
            numero_calculado = numero
        else:
            numero_calculado = numero+1

    if numero_calculado == numero:
        kaprekar = True
        print(numero)
    else:
        kaprekar = False



