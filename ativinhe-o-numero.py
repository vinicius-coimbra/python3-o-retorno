import random
cpu = random.randint(0,10)
jogador = 100
tentadivass = 0
while jogador != cpu:
    tentadivass += 1
    cpu = random.randint(0,10)
    print('_'*20)
    jogador = int(input('ativinhe o numero:'))
    if jogador != cpu:
        print('erro lixo eu pensei no numero {} tanda de novo'.format(cpu))

print('boa fi mas se precisso de {} tentadivas pra ir'.format(tentadivass))