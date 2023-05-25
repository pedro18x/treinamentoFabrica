class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calc_area(self):
        return self.largura * self.altura
    
    def calc_perimetro(self):
        return 2 * (self.largura + self.altura)