import random
cpu = random.randint(0,10)
jogador = 100
tentadivass = 0
while jogador != cpu:
    tentadivass += 1
    print('_'*20)
    jogador = int(input('ativinhe o numero:'))


    if jogador > cpu:
        print('um pouco menos')

    elif jogador < cpu:
        print("um pouco mais")


if tentadivass != 1:
    print('boa fi mas se precisso de {} tentadivas pra ir'.format(tentadivass))

else:
    print("slk so 1 tentadiva pra acerta ce e pika")