nums = []

while True:
    numero = input("Digite um número ('fim' para finalizar): ")
    
    if numero == "fim":
        break
    
    numero = int(numero)
    nums.append(numero)

print(f"Quantidade de números digitados: {len(nums)}")
numeros_ord = sorted(nums, reverse=True)
print("Lista de valores de forma decrescente:", numeros_ord)

if 5 in nums:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não se encontra na lista.")