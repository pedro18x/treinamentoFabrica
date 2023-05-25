class Pessoa:
    def __init__(self, Nome, Idade):
        self.nome = Nome
        self.idade = Idade

    def mostrar_dados(self):
        return f"Olá meu nome é {self.nome} e tenho {self.idade} anos."