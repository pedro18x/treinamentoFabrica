ano_atual = 2023

ano_nasc = int(input("Informe o ano de nascimento do atleta: "))

idade = ano_atual - ano_nasc

if idade <= 9:
    print(f"O atleta tem {idade} anos e está na categoria mirim.")
elif idade <= 14:
    print(f"O atleta tem {idade} anos e está na categoria infantil.")
elif idade <= 19:
    print(f"O atleta tem {idade} anos e está na categoria junior.")
elif idade <= 20:
    print(f"O atleta tem {idade} anos e está na categoria sênior.")
else:
    print(f"O atleta tem {idade} anos e está na categoria master.")