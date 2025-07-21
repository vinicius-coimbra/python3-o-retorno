numeros = tuple(int(input("escreva um numero:")) for _ in range(4))
numeros_9 = numeros.count(9)
if numeros.count(3):
    posiçao_do_3 = numeros.index(3)
'''for par in numeros:
    if par % 2 == 0:
        pares = tuple()'''
pares = tuple( par for par in numeros if par % 2 == 0 )
print('-'*20)

if numeros.count(9):
    print(f"tem {numeros_9} noves na tupla")
else:
    print("nao tem nenhum nove na tupla")

if numeros.count(3):
    print(f"o primeiro tres esta na possiçao {posiçao_do_3}")
else:
    print("nao tem nenhum tres na tupla")

if len(pares) > 0:
    print(f"os numeros pares foram {pares}")
else:
    print("nao teve valores paras")
print("_" * 40)
