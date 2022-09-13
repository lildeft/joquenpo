from random import randint


def player_vs_player(): #início da função jogador contra jogador
    continuar = True
    vitorias1 = 0
    vitorias2 = 0
    while continuar: #loop do jogo
        while True:
            try: #tratamento de erros caso jogador coloque algo inválido
                jogada1 = int(input('Digite 1 para pedra 2 para papel ou 3 para tesoura: '))
                jogada2 = int(input('Digite 1 para pedra 2 para papel ou 3 para tesoura: '))
                break
            except ValueError:
                print('Inválido')
        if jogada1 == 1 and jogada2 == 2: #pedra vs papel
            print('jogador2 venceu')
            vitorias2 += 1
        elif jogada1 == 1 and jogada2 == 3: #pedra vs tesoura
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 == 2 and jogada2 == 1: #papel vs pedra
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 == 2 and jogada2 == 3: #papel vs tesoura
            print('jogador2 venceu')
            vitorias2 += 1 
        elif jogada1 == 3 and jogada2 == 1: #tesoura vs pedra
            print('jogador2 venceu')
            vitorias2 +=1
        elif jogada1 == 3 and jogada2 == 2: #tesoura vs papel
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 > 3 or jogada2 > 3: #tesoura vs tesoura
            print('jogada inválida')
        elif jogada1 < 1 or jogada2 < 1: #pedra vs pedra
            print('jogada inválida')
        else: #empate
            print('empate')
        print(f'Placar atual \n {vitorias1} e {vitorias2}')
        while True: #loop de continuação de jogo
            try: #tratamento de erros
                prosseguir = int(input('Digite 1 para continuar ou qualquer outro para sair: '))
                if prosseguir != 1:
                    continuar = not continuar #fiz not continuar de sacanagem, poderia ser false
                break #sai do loop da continuação
            except ValueError: #exceção
                print('o caractere digitado não é um número')    
    print(f'Placar geral \n {vitorias1} e {vitorias2}')


def player_vs_machine(): 
    continuar = True
    vitorias1 = 0
    vitorias2 = 0
    while continuar:
        while True:
            try:
                jogada1 = int(input('Digite 1 para pedra 2 para papel ou 3 para tesoura: '))
                break
            except ValueError:
                print('Inválido')
        jogada2 = randint(1, 3)
        print(f'o computador escolheu {jogada2} ')
        if jogada1 == 1 and jogada2 == 2:
            print('jogador2 venceu')
            vitorias2 += 1
        elif jogada1 == 1 and jogada2 == 3:
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 == 2 and jogada2 == 1:
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 == 2 and jogada2 == 3:
            print('jogador2 venceu')
            vitorias2 += 1 
        elif jogada1 == 3 and jogada2 == 1:
            print('jogador2 venceu')
            vitorias2 +=1
        elif jogada1 == 3 and jogada2 == 2:
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 > 3 or jogada2 > 3:
            print('jogada inválida')
        elif jogada1 < 1 or jogada2 < 1:
            print('jogada inválida')
        else:
            print('empate')
        print(f'Placar atual \n {vitorias1} e {vitorias2}')
        while True:
            try:
                prosseguir = int(input('Digite 1 para continuar ou qualquer outro para sair: '))
                if prosseguir != 1:
                    continuar = not continuar
                break
            except ValueError:
                print('o caractere digitado não é um número')
    print(f'Placar geral \n {vitorias1} e {vitorias2}')


def machine_vs_machine():
    continuar = True
    vitorias1 = 0
    vitorias2 = 0
    while continuar:
        jogada1 = randint(1, 3)
        print(f'o computador 1 escolheu {jogada1}')
        jogada2 = randint(1, 3)
        print(f'o computador 2 escolheu {jogada2} ')
        if jogada1 == 1 and jogada2 == 2:
            print('jogador2 venceu')
            vitorias2 += 1
        elif jogada1 == 1 and jogada2 == 3:
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 == 2 and jogada2 == 1:
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 == 2 and jogada2 == 3:
            print('jogador2 venceu')
            vitorias2 += 1 
        elif jogada1 == 3 and jogada2 == 1:
            print('jogador2 venceu')
            vitorias2 +=1
        elif jogada1 == 3 and jogada2 == 2:
            print('jogador1 venceu')
            vitorias1 += 1
        elif jogada1 > 3 or jogada2 > 3:
            print('jogada inválida')
        elif jogada1 < 1 or jogada2 < 1:
            print('jogada inválida')
        else:
            print('empate')
        print(f'Placar atual \n {vitorias1} e {vitorias2}')
        while True:
            try:
                prosseguir = int(input('Digite 1 para continuar ou qualquer outro para sair: '))
                if prosseguir != 1:
                    continuar = not continuar
                break
            except ValueError:
                print('o caractere digitado não é um número')
    print(f'Placar geral \n {vitorias1} e {vitorias2}')


modalidade = input('Escolha a modalidade: 1 = Player VS Player, 2 = Player VS Machine, 3 = Machine VS Machine: ') #escolha do modo de jogo
if modalidade == '1':
    player_vs_player()
elif modalidade == '2':
    player_vs_machine()
elif modalidade == '3':
    machine_vs_machine()
else:
    print('Inválido')
print('Projeto desenvolvido por Eduardo Babinski(vulgo Dudu Pitbull🐶)  Pedro Henrique(vulgo Tio Orochi PHP🐘) João Merlin(Vulgo Bruxão🧙🏻) \nAgradecimentos: Profe Marina e PUCPR 🥳')









