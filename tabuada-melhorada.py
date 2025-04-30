while True :
    numero = int(input('gual tabuada voce quer ver?:' ))
    if numero < 0 :
        print('o programa acaba aqui')
        break

   
    for tabuada in range(1, 11):
        print(f'{tabuada} X {numero} = {tabuada * numero}')