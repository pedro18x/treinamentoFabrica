import random

jogadores = ["Jogador1", "Jogador2", "Jogador3", "Jogador4"]
resultados = {}

for jogador in jogadores:
    resultado = random.randint(1, 6) 
    resultados[jogador] = resultado

print("Resultados:")
for jogador, resultado in resultados.items():
    print(f"{jogador}: {resultado}")

resultados_ordenados = dict(sorted(resultados.items(), key=lambda x: x[1], reverse=True))

print("\nClassificação:")
posicao = 1
for jogador, resultado in resultados_ordenados.items():
    print(f"{posicao}º lugar: {jogador} - Resultado: {resultado}")
    posicao += 1