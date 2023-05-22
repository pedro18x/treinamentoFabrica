def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: valor inválido. Digite um número inteiro válido.")

n = leiaInt('Digite um número inteiro: ')
print(f"Você digitou: {n}")