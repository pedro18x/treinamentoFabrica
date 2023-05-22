def notar(*notas, situacao=False):
    resultado = {}
    quantidade = len(notas)
    resultado['Quantidade de notas'] = quantidade

    if quantidade > 0:
        resultado['Maior nota'] = max(notas)
        resultado['Menor nota'] = min(notas)
        resultado['Média da turma'] = sum(notas) / quantidade

        if situacao:
            media_minima = 7
            if resultado['Média da turma'] >= media_minima:
                resultado['Situação'] = 'Aprovado'
            else:
                resultado['Situação'] = 'Reprovado'

    return resultado

notas = []
quantidade_notas = int(input("Digite a quantidade de notas: "))

for i in range(quantidade_notas):
    nota = float(input("Digite a nota {}: ".format(i + 1)))
    notas.append(nota)

situacao_informada = input("Deseja incluir a situação? (S/N): ")
situacao = True if situacao_informada.lower() == 's' else False

resultado = notar(*notas, situacao=situacao)
print(resultado)