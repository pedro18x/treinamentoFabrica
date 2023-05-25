class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo=0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O depósito de {valor} foi realizado com sucesso!")
        else:
            print("O valor inserido é inválido para depósito.")
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"O  saque de {valor} foi realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def saldo(self):
        print(f"O seu saldo atual é de {self.saldo}.")

    def consultar_conta(self):
        print(f"O nome do titular é {self.nome} e o número da conta bancária é {self.numero_conta}.")