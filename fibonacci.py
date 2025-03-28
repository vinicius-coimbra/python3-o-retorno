numero_da_sequencia = int(input('escreva um numero pra ver a sequencia de fibonacci:'))
relogio = 0
numero = 0
soma = numero
while relogio != numero_da_sequencia:
    print(f'{numero}',end=' > ')
    relogio += 1
    if numero == 0:
        numero += 1
    numero +=soma 
    