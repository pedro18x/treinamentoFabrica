numeros = []
pares = []
impares = []

while True:
    num = input("Digite um número ('fim' para finalizar): ")
    
    if num == "fim":
        break
    
    num = int(num)
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Números digitados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")