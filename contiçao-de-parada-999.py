n1 = 0
v = 0
r = 0
while r != 999:
    r = int(input('escreva um numero:'))
    if r != 999:
        v +=1
        n1 += r
print('~' * 20)
print('a soma dos numeros e {}\na guantidade de numeros digitatos e {}'.format(n1,v))
print('~' * 20)