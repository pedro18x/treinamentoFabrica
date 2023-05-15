boletim = [] 

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar o programa): ")
    if nome.lower() == "sair":
        break

    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))

    aluno = [nome, n1, n2]  
    boletim.append(aluno)

print("\nBoletim:")
for aluno in boletim:
    nome = aluno[0]
    n1 = aluno[1]
    n2 = aluno[2]
    media = (n1 + n2) / 2
    print(f"Aluno: {nome} - Média: {media:.2f}")

    exibir_notas = input("Deseja exibir as notas individuais deste aluno? (s/n): ")
    if exibir_notas.lower() == "s":
        print(f"Notas do aluno {nome}:")
        print(f"Nota 1: {n1}")
        print(f"Nota 2: {n2}")
    print()