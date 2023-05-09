from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade < 18:
    print(f"Você tem {idade} anos e ainda não precisa se alistar.")
    tempo_falta = 18 - idade
    print(f"Falta(m) {tempo_falta} ano(s) para o seu alistamento.")
elif idade == 18:
    print(f"Você tem {idade} anos e precisa se alistar.")
else:
    print(f"Você tem {idade} anos e já passou da idade de se alistar.")
    tempo_passou = idade - 18
    print(f"Já se passaram {tempo_passou} ano(s) do prazo para o seu alistamento.")