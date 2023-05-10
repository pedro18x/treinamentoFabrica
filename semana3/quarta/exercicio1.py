
valores = tuple(int(input(f'Digite o {i+1}º valor: ')) for i in range(4))

quantidade_nove = valores.count(9)

posicao_tres = valores.index(3) if 3 in valores else -1

numeros_pares = tuple(filter(lambda x: x % 2 == 0, valores))

print(f'O valor 9 apareceu {quantidade_nove} vezes na tupla.')
if posicao_tres >= 0:
    print(f'O primeiro valor 3 foi digitado na posição {posicao_tres}.')
else:
    print('Não foi digitado nenhum valor 3 na tupla.')
print(f'Os números pares digitados foram: {numeros_pares}.')