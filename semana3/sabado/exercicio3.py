val = []

while True:
    valor = input("Digite um valor numérico ('fim' para finalizar): ")
    
    if valor == "fim":
        break
    
    valor = int(valor)
    
    if valor not in val:
        val.append(valor)

valores_unicos = sorted(val)
print("Valores únicos digitados (em ordem crescente): ", valores_unicos)