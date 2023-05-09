soma = 0
contador = 0
maior = menor = valor = 0
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    
    if contador == 0 and valor == 0:
        print('Nenhum valor foi digitado!')
        break
    
    if contador == 0:
        maior = menor = valor
    
    if valor > maior:
        maior = valor
        
    if valor < menor:
        menor = valor
    
    soma += valor
    contador += 1
    
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    
if contador == 0:
    print('Nenhum valor foi digitado!')
else:
    media = soma / contador
    print(f'A média dos {contador} valores digitados foi {media:.2f}.')
    print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')