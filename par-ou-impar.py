venceu = 0
import random
while True:
    cpu = random.randint(0,10)
    jogador = int(input('escolha um numero'))
    par_impar = str(input('par o impar [P/I]:'))
    soma = jogador + cpu
    perde = 'nada'
    print('~' * 20)
    if par_impar in 'Ii':
        if soma % 2:
            print('o jogador venceu')
        else:
            print('o jogador perdeu')
            perde = 'perdeu'

    if par_impar in 'Pp':
        if soma % 2 :
            print('jogador perdeu')
            perde = 'perdeu'
        else:
            print('jogador venceu')

    if perde == 'perdeu':
        print('perdeu mane fica sem joga ai!')
        if venceu == 1:
            print('venceu so 1 vez que isso mane')

        elif venceu > 0:
            print(f'voce venceu {venceu} vezes')
        else:
            print('bixo se nao venceu UMA kkkkkk muito otario!!!!')
        break
    venceu += 1
    print(f'a CPU escolheu {cpu} voce escolheu {jogador}')
    print('~' * 20)