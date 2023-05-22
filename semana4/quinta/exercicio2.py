import random

def sorteia():
    num = []
    for _ in range(5):
        num.append(random.randint(0, 10))
    return num

def somaPar(num):
    soma = 0
    for num in num:
        if num % 2 == 0:
            soma += num
    return soma

num = sorteia()
print("Números sorteados:", num)
soma_pares = somaPar(num)
print("Soma dos valores pares:", soma_pares)