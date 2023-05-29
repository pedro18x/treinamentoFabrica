class CadastroFilmes:
    def __init__(self):
        self.lista_filmes = []

    def adicionar_filme(self, filme):
        self.lista_filmes.append(filme)
        print("Filme adicionado com sucesso!")

    def buscar_filme(self, nome_filme):
        for filme in self.lista_filmes:
            if filme.lower() == nome_filme.lower():
                return filme
        return None

    def mostrar_lista_filmes(self):
        if not self.lista_filmes:
            print("A lista de filmes está vazia.")
        else:
            print("Lista de filmes:")
            for filme in self.lista_filmes:
                print(filme)

    def remover_filme(self, nome_filme):
        filme_encontrado = self.buscar_filme(nome_filme)
        if filme_encontrado:
            self.lista_filmes.remove(filme_encontrado)
            print("Filme removido com sucesso!")
        else:
            print("Filme não encontrado.")
