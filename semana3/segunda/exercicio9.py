from datetime import date

ano_atual = date.today().year 

pessoa = {}  
pessoa['nome'] = input("Digite o nome da pessoa: ")
ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = int(input("Digite o número da carteira de trabalho (0 se não tiver): "))

if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input("Digite o ano de contratação: "))
    pessoa['salario'] = float(input("Digite o salário: "))

    idade_aposentadoria = pessoa['ano_contratacao'] - ano_nascimento + 35
    pessoa['idade_aposentadoria'] = idade_aposentadoria

print("\nDados cadastrados:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")