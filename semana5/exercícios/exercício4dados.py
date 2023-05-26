class Animal:
    def __init__(self, nome_espécie, idade):
        self.nome_espécie = nome_espécie
        self.idade = idade

    def som(self):
        return "Auuu"
    
    def movimento(self):
        return "Correndo de patas"