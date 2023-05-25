from exercício3dados import ContaBancaria

conta = ContaBancaria("Pedro", 23445)

print(f"O seu saldo é de {conta.saldo}")
conta.depositar(250)
print(f"O seu saldo é de {conta.saldo}")
conta.sacar(50)
print(f"O seu saldo é de {conta.saldo}")

