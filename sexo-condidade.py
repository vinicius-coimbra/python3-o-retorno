homem = 0 
mais_de_18 = 0
mulher_menos_20 = 0
while True:
    sexo = str(input('sexo[M/F]:')).upper().strip()
    while sexo not in ['M', 'F']:
        sexo = input('sexo invalido digite de novo [M/F]:').upper().strip()
 
    idade =  input('idade:')
    while not idade.isdigit():
        idade = input('idade invalida digite de novo:')
    idade = int(idade)

    if sexo == 'F' and idade <= 20:
        mulher_menos_20 += 1

    if sexo == 'M':
        homem += 1

    if idade >= 18:
        mais_de_18 += 1
    
    resposta = input('quer continuar? [S/N]:').upper().strip()

    while resposta not in ['S', 'N']:
        resposta = input('resposta invalida digite de forma correta [S/N]')  
        

    if resposta == 'N':
        break    

print(f'{'~' * 20}\no numero de homens e {homem}\no numero de pessoas que tem 18 ou mais e {mais_de_18}\no numero de mulheres com menos de 20 sao {mulher_menos_20}\n{'~' * 20}')
