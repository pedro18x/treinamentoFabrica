def contador(inicio, fim, passo):
    if passo == 0:
        print("O passo não pode ser igual a zero.")
    elif passo > 0:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ")
    print()


print("Contagem de 1 até 10, de 1 em 1:")
contador(1, 10, 1)

print("Contagem de 10 até 0, de 2 em 2:")
contador(10, 0, -2)

print("Contagem personalizada:")
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))
contador(inicio, fim, passo)