soma = 0
guantidade_de_numero = 0
while True:
    numero = int(input('escreva um numero[999 para parar]:'))
    if numero == 999:
        break
    
    else:
        guantidade_de_numero += 1
        soma +=numero        
    
print(f'tem {guantidade_de_numero} numeros e a soma  deles e {soma}')