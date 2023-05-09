import random

numero = random.randint(0, 10)
palpites = 0

print("Vou pensar em um número entre 0 e 10. Adivinhe!")

while True:
    palpite = int(input("Qual é o seu palpite? "))
    palpites += 1
    
    if palpite == numero:
        print(f"Parabéns, você acertou em {palpites} palpites!")
        break
    elif palpite < numero:
        print("O número que estou pensando é maior. Tente mais uma vez!")
    else:
        print("O número que estou pensando é menor. Tente mais uma vez!")