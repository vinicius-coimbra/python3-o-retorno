termo = int(input('escreva o termo de uma p.a:'))
razao = int(input('escreva a razao de uma p.a:'))
resposta = 10
relogio = 0
soma_dos_termos = 0
while resposta != 0:
      print(f'{termo}',end= ' > ')
      termo += razao
 
      relogio += 1
      if resposta == 0:
          break
      
      if relogio == resposta:
         soma_dos_termos += resposta
         relogio = 0
         resposta = int(input('\nvoce que ver mais guandos termos?:'))
     
    

print('cabou')
print(soma_dos_termos)
