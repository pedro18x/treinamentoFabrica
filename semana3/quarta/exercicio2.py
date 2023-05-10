produtos_restaurante = ('Hamburguer', 25.00,
            'Suco', 6.00,
            'Refrigerante', 8.00,
            'Almoço/Quentinha', 30.00,
            'Batata Frita', 12.00,
            'Churrasco', 45.00,)


print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(produtos_restaurante), 2):
    nome = produtos_restaurante[i]
    preco = produtos_restaurante[i+1]
    print(f'{nome:.<30} R${preco:>7.2f}')
print('-' * 40)