numeros = 'zero', 'um', 'dois' , 'tres' ,'quadro' ,'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' ,'onze' ,'' , 'treze' , 'quadorze' , 'quinze' , 'desezes' , 'desezede' , 'tezoido' ,'dezenove' ,'vinde'
numero_do_usuario = input('escreva um numero de 0 a 20: ')
while not numero_do_usuario.isdigit():
    numero_do_usuario = input('numero invalido digite de novo de 0 a 20:')
numero_do_usuario = int(numero_do_usuario)
if numero_do_usuario <= 20 and numero_do_usuario >= 0:
    print(f'voce escolheu o numero {numeros[numero_do_usuario]}')
else:
    while numero_do_usuario <0 or numero_do_usuario >20:
        numero_do_usuario = int(input("numero invalido escolha outro entre 0 e 20:"))
    print(f'voce escolheu o numero {numeros[numero_do_usuario]}')
