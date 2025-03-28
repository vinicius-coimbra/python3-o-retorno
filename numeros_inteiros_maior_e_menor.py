resposta = 'sim'
contidade_de_numero = 0
maior = float('-inf')
menor = float('inf')
soma = 0
while resposta != 'N':
    contidade_de_numero += 1
    numero = int(input("escreva um numero:"))
    resposta = input('que continuar\ns/n?:').upper()

    soma += numero
    media = soma / contidade_de_numero
    
    if maior < numero:
        maior = numero
    
    if menor > numero:
        menor = numero

print(f'a media entre eles e {media} o maior e {maior} o menor e {menor}')
print(soma)