
salario_recebido = float(input("Informe o seu salário: "))
gasto_total = float(input("Informe o total gasto em despesas: "))

if gasto_total <= salario_recebido:
    print("Gastos dentro do orçamento")
else:
    print("Gastos acima do orçamento")