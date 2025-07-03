numeros = 0, 1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 , 18 ,19 ,20
numero_do_usuario = input('escreva um numero de 0 a 20: ')
while not numero_do_usuario.isdigit():
    numero_do_usuario = input('numero invalido digite de novo de 0 a 20:')
numero_do_usuario = int(numero_do_usuario)

if numeros.count(numero_do_usuario):
    print("tem")

else:
    print('nao tem ')