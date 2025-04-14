import random
from random import randint

# Exercício 10 - Jogo
vida = random.randint(200, 1000)
print("-- DUELO DE HEROIS --")
print("== VOCÊ ==")
vida_usuario = vida; print(f"hp: {vida}")
ataque_usuario = random.randint(1, 50); print(f"ATQ: {ataque_usuario}")
defesa_usuario = random.randint(1, 50); print(f"DEF {defesa_usuario}")

print("\n== INIMIGO == ")
vida_inimigo = vida; print(f"HP: {vida_inimigo}")
ataque_inimigo = random.randint(defesa_usuario+1, 50); print(f"ATQ: {ataque_inimigo}")
defesa_inimigo = random.randint(1, ataque_usuario-1); print(f"DEF: {defesa_inimigo}")

round = 1
while vida_usuario or vida_inimigo > 0:
    print(f"=== ROUND {round} ===")
    print(f"Seu HP: {vida_usuario} | Inimigo HP: {vida_inimigo}")
    escolha_usuario = int(input("Seu turno, escolha: \n[1] Atacar \n[2] Curar \n[0] Ir para o menu\n > "))


    







