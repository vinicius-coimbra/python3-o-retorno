r1 = 0
n1 = int(input('digite um numero:'))
n2 = int(input('digite o segundo numero:'))
while r1 != 5 :
    print('[1]soma\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair')
    r1 = int(input('escolha:'))
    if r1 == 1:
        print('_'*20)
        print(n1 + n2)
        print('_'*20)
    elif r1 == 2:
        print('_'*20)
        print(n1 * n2)
        print('_'*20)
    elif r1 == 3:
        print('_'*20)
        if n1 > n2:
            print(n1)
        elif n1 == n2:
            print('os dois tem o mesmo falor')
        else:
            print(n2)
        print('_'*20)
    elif r1 == 4:
        n1 = int(input('digite um numero:'))
        n2 = int(input('digite o segundo numero:'))