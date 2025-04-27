mais_de_mil = 0
total = 0
nome_do_barado = 'None'
presso_mais_barado = 0
while True:
    nome = input('nome do produto:').strip()
    presso = input('presso do produto:')

    while presso.isdigit() is not True:
        presso = input('esse presso e invalido digite de novo:')  
    if presso.isdigit() is True:
        presso = int(presso)

    if presso_mais_barado == 0:
        presso_mais_barado = presso
        nome_do_barado = nome
    
    if presso < presso_mais_barado:
        presso_mais_barado = presso
        nome_do_barado = nome

    if presso >= 1000:
        mais_de_mil += 1
    
    total += presso
    
    resposta = input('que continuar?[S/N]:').upper().strip()

    while resposta not in ['N', 'S']:
        resposta = input('resposta invalida!!![S/N]:')
    
    if resposta == 'N':
        break

print(f'{'~' * 20}\no valor total da compra e de {total}\ntem {mais_de_mil} que custam mais de mil\ne o item mais barato foi {nome_do_barado} que custa {presso_mais_barado}\n{'~' * 20}')