

ano_nasc = int(input("Digite o ano de nascimento: "))


idade = 2023 - ano_nasc 

if idade >= 18:
    print("Você é maior de idade e tem", idade, "anos.")
else:
    print("Você é menor de idade e tem", idade, "anos.")