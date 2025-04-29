de50notas = 0
de20notas = 0
de10notas = 0
de1notas  = 0

valor = input('quando voce quer:')
while not valor.isdigit() :
    valor = input('valor invalido digite de novo:')
valor = int(valor)

while True:
    de50notas = valor // 50 
    valor %= 50

    de20notas = valor // 20
    valor %= 20

    de10notas = valor //10
    valor %= 10

    de1notas = valor // 1
    valor %= 1

    if valor == 0:
        break


print('~' * 20)
if de50notas >= 1:
    if de50notas > 1:
        print(f'total de {de50notas} cedulas de 50')
    else:
        print(f'total de {de50notas} cedula de 50')
            

if de20notas >= 1:
    if de20notas > 1:    
        print(f'total de {de20notas} cedulas de 20')
    else:
        print(f'total de {de20notas} cedula de 20')
        

if de10notas >= 1:
    if de10notas > 1:
        print(f'total de {de10notas} cedulas de 10')
    else:
        print(f'total de {de10notas} cedula de 10')
        

if de1notas >= 1:
    if de1notas > 1:
        print(f'total de {de1notas} cedulas de 1')
    else:
        print(f'total de {de1notas} cedula de 1')
print('~' * 20 )