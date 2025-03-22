n = int(input('escreva um numero pra fatorizar:'))
r = n
while n != 1:
    r = r * (n-1)
    n -= 1

print(r)