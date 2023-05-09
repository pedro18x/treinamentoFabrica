nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"A média do aluno foi {media:.1f} e ele está reprovado.")
elif media < 7.0:
    print(f"A média do aluno foi {media:.1f} e ele está em recuperação.")
else:
    print(f"A média do aluno foi {media:.1f} e ele está aprovado.")