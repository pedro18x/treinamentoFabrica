pessoas = []  
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para finalizar): ")
    if nome.lower() == "sair":
        break

    peso = float(input("Digite o peso da pessoa em kilogramas: "))

    pessoa = (nome, peso) 
    pessoas.append(pessoa)


quantidade_pessoas = len(pessoas)
print(f"\nForam cadastradas {quantidade_pessoas} pessoas.")

pessoas.sort(key=lambda x: x[1], reverse=True)

print("\nPessoas mais pesadas:")
for pessoa in pessoas[:3]:
    nome, peso = pessoa
    print(f"Nome: {nome}, Peso: {peso} kg")

print("\nPessoas mais leves:")
for pessoa in pessoas[-3:]:
    nome, peso = pessoa
    print(f"Nome: {nome}, Peso: {peso} kg")