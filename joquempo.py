from random import randint


def player_vs_player():
    continuar = True
    vitorias1 = 0
    vitorias2 = 0
    while continuar:
        while True:
            try:
                jogada1 = int(input('Digite 1 para pedra 2 para papel ou 3 para tesoura: '))
                jogada2 = int(input('Digite 1 para pedra 2 para papel ou 3 para tesoura: '))
                break
            except ValueError:
                print('Inválido')
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


modalidade = input('Escolha a modalidade: 1 = Player VS Player, 2 = Player VS Machine, 3 = Machine VS Machine: ')
if modalidade == '1':
    player_vs_player()
elif modalidade == '2':
    player_vs_machine()
elif modalidade == '3':
    machine_vs_machine()
else:
    print('Inválido')
print('Projeto desenvolvido por Eduardo Babinski(vulgo Dudu Pitbull🐶)  Pedro Henrique(vulgo Tio Orochi PHP🐘) João Merlin(Vulgo Bruxão🧙🏻) \nAgradecimentos: Profe Marina e PUCPR 🥳')









