def contagem_regressia(numero):
    for contagem in range(0,numero):
        print(contagem)

lista1 = [1, 2,3,4,5,6,7,8,9]
lista2 = [10,54,100,60]


def maior_numero(listas):
    return(max(listas))

def soma_de_numeros_maiores(*numeros):
    resuldado = 0
    for numero in numeros:
        resuldado += numero
    print(resuldado)

soma_de_numeros_maiores(maior_numero(lista1),maior_numero(lista2))
#isso deve dar tudo cagado mas funciona e é isso que importa.
#agora que eu vi que tem uma forma de fazer isso sem o max() mas e inutil fazer dessa forma.
# eu ja sabia que tinha aquela outra forma ja fiz outra fez mas nao vale apena. 
