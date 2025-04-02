termo = int(input('escreva o termo da P.A:'))
razao = int(input('escreva a razao da P.A:'))
relogio = 0
while relogio != 10:
    print(f'{termo}',end='')
    print(' >> ' if relogio < 9 else ' fim',end='' )
    relogio +=1
    termo += razao