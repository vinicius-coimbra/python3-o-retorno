import random
numeros = tuple(random.randint(1, 100) for _ in range(5))

print(*numeros)
print(f"o menor numero da lista e {max(numeros)}")
print(f"menor numero da lista e {min(numeros)}")


""""O for _ in range(5) é que repete a chamada do randint 5 vezes, cada vez gerando um valor novo.

O tuple(...) empacota tudo isso numa tupla.

As vírgulas da tupla não aparecem no código, mas o Python monta a tupla com elas por baixo dos panos, pegando os valores da generator expression."""