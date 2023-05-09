import random

vitorias = 0

while True:
    jogador = int(input('Digite um número entre 0 e 10: '))
    escolha = input('Par ou ímpar? [P/I]: ').upper()
    
    while escolha not in ['P', 'I']:
        escolha = input('Opção inválida. Par ou ímpar? [P/I]: ').upper()
    
    computador = random.randint(0, 10)
    soma = jogador + computador
    resultado = soma % 2
    
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}.', end=' ')
    
    if resultado == 0:
        print('DEU PAR!')
        if escolha == 'P':
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    else:
        print('DEU ÍMPAR!')
        if escolha == 'I':
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    
print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')