n = int(input('escreva um numero pra fatorizar:'))
r = n
f = 1
while n > 0:
    print(f'{n}',end= '')
    print(' x ' if n > 1  else ' = ',end='')
    f *=n
    n -= 1

print(f)