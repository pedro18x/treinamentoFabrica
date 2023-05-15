jogador = {}

jogador['nome'] = input("Digite o nome do jogador: ")
partidas_jogadas = int(input("Digite a quantidade de partidas jogadas: "))

gols_totais = 0
for partida in range(1, partidas_jogadas + 1):
    gols = int(input(f"Digite a quantidade de gols feitos na partida {partida}: "))
    gols_totais += gols
    jogador[f'partida {partida}'] = gols

jogador['total_gols'] = gols_totais

print("\nAproveitamento do jogador:")
for chave, valor in jogador.items():
    print(f"{chave.capitalize()}: {valor}")