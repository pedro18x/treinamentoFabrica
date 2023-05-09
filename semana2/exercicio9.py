while True:
    num = int(input('Digite um número para ver a sua tabuada: '))
    
    if num < 0:
        print('Programa encerrado.')
        break
    
    print(f'Tabuada de {num}:')
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')