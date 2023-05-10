
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

maior_número = num1

if num2 > maior_número:
    maior_número = num2
if num3 > maior_número:
    maior_número = num3
if num4 > maior_número:
    maior_número = num4
if num5 > maior_número:
    maior_númerocc = num5

print("O maior número digitado foi:", maior_número)