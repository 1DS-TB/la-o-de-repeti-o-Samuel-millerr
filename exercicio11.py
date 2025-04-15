import random
from time import sleep
from random import randint

# Exercício 10 - Jogo
print("BEM VINDO AO DUELO DE HEROIS!!!\nEscolha sua opção: ")
escolha_menu_principal = int(input(("[1] Jogar\n[0] Fechar o jogo\n > ")))
while escolha_menu_principal not in [1, 0]:
    print("\nA opção que você escolheu é inválida! Por gentileza tente novamente.")
    escolha_menu_principal = int(input(("[1] Jogar\n[0] Fechar o jogo\n > ")))

while escolha_menu_principal == 1:
    vida = random.randint(200, 1000)
    print("\n-- DUELO DE HEROIS --")
    print("== VOCÊ ==")
    vida_usuario = vida; print(f"hp: {vida}")
    ataque_usuario = random.randint(1, 50); print(f"ATQ: {ataque_usuario}")
    defesa_usuario = random.randint(1, 50); print(f"DEF {defesa_usuario}")

    print("\n== INIMIGO == ")
    vida_inimigo = vida; print(f"HP: {vida_inimigo}")
    ataque_inimigo = random.randint(max(defesa_usuario, 1), 50); print(f"ATQ: {ataque_inimigo}")
    defesa_inimigo = random.randint(1, max(ataque_usuario, 1)); print(f"DEF: {defesa_inimigo}")

    item_usado_usuario = []
    item_usado_inimigo = []

    round = 1
    while vida_usuario > 0 or vida_inimigo > 0:
        print(f"\n=== ROUND {round} ===")
        print(f"Seu HP: {vida_usuario} | Inimigo HP: {vida_inimigo}")
        # TOMADA DE DECISÃO DO USUÁRIO
        escolha_usuario = int(input("Seu turno, escolha: \n[1] Atacar \n[2] Curar \n[3] Usar Itens \n[0] Ir para o menu\n > "))

        # TRATAMENTO DE ERRO CASO O USUÁRIO DIGITE ALGUMA OPÇÃO QUE NÃO ESTÁ DISPONÍVEL
        while escolha_usuario not in [1, 2, 3, 0]:
            print("\nA opção que você escolheu é inválida! Por gentileza tente novamente.")
            escolha_usuario = int(input("Seu turno, escolha: \n[1] Atacar \n[2] Curar \n[3] Usar Itens \n[0] Ir para o menu\n > "))

        # CASO O USUÁRIO ACESSE O MENU ESSE CÓDIGO SERÁ TRATADO
        if escolha_usuario == 0:
            print("\n=== Você está no MENU ===")
            print("Escolha uma das opções abaixo: ")
            escolha_menu = int(input("[1] Retornar ao jogo\n[0] Sair do jogo\n > "))

            # TRATAMENTO DE ERRO CASO O USUÁRIO DIGITE ALGUMA OPÇÃO QUE NÃO ESTÁ DISPONÍVEL
            while escolha_menu not in [1, 0]:
                print("\n=== Você está no MENU ===")
                print("A opção que você escolheu é inválida! Por gentileza tente novamente.")
                escolha_menu = int(input("[1] Retornar ao jogo\n[0] Sair do jogo\n > "))

            if escolha_menu == 0:
                break
            elif escolha_menu == 1:
                print(f"\n=== ROUND {round} ===")
                print(f"Seu HP: {vida_usuario} | Inimigo HP: {vida_inimigo}")
                escolha_usuario = int(input("Seu turno, escolha: \n[1] Atacar \n[2] Curar \n[3] Usar Itens \n > "))
                # TRATAMENTO DE ERRO CASO O USUÁRIO DIGITE ALGUMA OPÇÃO QUE NÃO ESTÁ DISPONÍVEL
                while escolha_usuario not in [1, 2, 3]:
                    print("\nA opção que você escolheu é inválida! Por gentileza tente novamente.")
                    escolha_usuario = int(input("Seu turno, escolha: \n[1] Atacar \n[2] Curar \n[3] Usar Itens \n > "))

        # TOMADA DE DECISÃO DO USUÁRIO
        if escolha_usuario == 1:
            acao_ataque_usuario = ataque_usuario - defesa_inimigo
            if random.random() <= 0.1:
                print("VOCÊ DEU UM DANO CRITÍCO (DANO x2)!")
                acao_ataque_usuario = (ataque_usuario - defesa_inimigo)*2
            vida_inimigo = vida_inimigo - ataque_usuario
            print(f"Você atacou! O inimigo perdeu {acao_ataque_usuario} HP")
        elif escolha_usuario == 2:
            print("Você se curou! Você recuperou 20 HP")
            vida_usuario = min(vida_usuario + 20, 1000)
        elif escolha_usuario == 3:
            print("[1] Poção de Força (+ATQ por 2 turnos)")
            print("[2] Poção de Cura (+100 HP)")
            print("[3] Poção de Defesa (DEF +20 5 turnos)")
            print("[4] Poção Explosiva (dano direto de 60)")
            item = input("Escolha o item: ")

            # TRATAMENTO DE ERRO CASO O USUÁRIO DIGITE ALGUMA OPÇÃO QUE NÃO ESTÁ DISPONÍVEL
            while item not in [1, 2, 3, 4]:
                print("\nA opção que você escolheu é inválida! Por gentileza tente novamente.")
                print(("Seu turno, escolha: \n[1] Poção de Força (+ATQ por 2 turnos) \n[2] Poção de Cura (+100 HP) \n[3] Poção de Defesa (DEF +20 5 turnos) \n[4] Poção Explosiva (dano direto de 60) \n > "))
                item = input("Escolha o item: ")

            if item not in item_usado_usuario:
                if item == "1": ataque_usuario += 20; item_usado_usuario.append(item); print("Força aumentada em 20 pontos!")
                elif item == "2": vida_usuario += 100; item_usado_usuario.append(item); print("Curado em 100 pontos de HP!")
                elif item == "3": defesa_usuario += 20; item_usado_usuario.append(item); print("Defesa aumentada em 20 pontos!")
                elif item == "4": vida_inimigo -= 60; item_usado_usuario.append(item); print("Explosão no inimigo! O inimigo perde 60 pontos de HP")
            else:
                print("Item já usado!")

        # TOMADA DE DECISÃO DO INIMIGO
        escolha_inimigo = random.choice(["atacar", "curar","usar_itens"])
        if escolha_inimigo == "atacar":
            acao_ataque_inimigo = ataque_inimigo-defesa_usuario
            if random.random() <= 0.1:
                print("VOCÊ RECEBEU UM DANO CRITÍCO (DANO x2)!")
                acao_ataque_inimigo = (ataque_inimigo - defesa_usuario)*2
            vida_usuario = vida_usuario - ataque_inimigo
            print(f"O inimigo atacou! Você perdeu {acao_ataque_inimigo} HP")
        elif escolha_inimigo == "curar":
            print("O inimigo se curou! ELe recuperou 20 HP")
            vida_inimigo = min(vida_inimigo+20, 1000)
        elif escolha_inimigo == "usar_itens" and len(item_usado_inimigo) < 5:
            print("O inimigo irá usar um item!")
            sleep(0.5)
            print(".")
            sleep(0.5)
            print(".")
            item = str(random.randint(1,4))
            if item not in item_usado_inimigo and len(item_usado_inimigo) < 5:
                if item == "1": ataque_inimigo += 20; item_usado_inimigo.append(item); print("O inimigo escolheu a poção de Força. O ataque do inimigo é aumentado em 20 pontos!")
                elif item == "2": vida_inimigo += 100; item_usado_inimigo.append(item); print("O inimigo escolheu a poção de cura. O inimigo é curado em 100 pontos de HP!")
                elif item == "3": defesa_inimigo += 20; item_usado_inimigo.append(item); print("O inimigo escolheu a poção de defesa. A defesa do inimigo é aumentada em 20 pontos!")
                elif item == "4": vida_usuario -= 60; item_usado_inimigo.append(item); print("Explosão em VOCÊ! Você perdeu 60 pontos de HP")
            else:
                print("O inimigo não tem mais itens!")

        if vida_usuario <= 0 or vida_inimigo <= 0:
            break

        round += 1

    print("\nO JOGO ACABOU!")
    if vida_inimigo <= 0 and vida_usuario > 0: print("PARABÉNS! Você ganhou, o inimigo perdeu todo o HP. (:"); resultado = "GANHOU"
    elif vida_usuario <= 0 and vida_inimigo > 0: print("QUE PENA! Você perdeu todo seu HP. :( "); resultado = "PERDEU"
    elif vida_usuario <= 0 and vida_inimigo <= 0: print("Você conseguiu empatar o jogo. Tá de parabéns! :/"); resultado = "EMPATOU :/"

    print(f"\n=== DUELO DE HEROIS ===\n Agora que o jogo acabou, o que deseja fazer?")
    escolha_menu_principal = int(input(("[1] Jogar Novamente\n[0] Fechar o jogo\n > ")))
