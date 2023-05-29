from projetocadastro import CadastroFilmes

cadastro = CadastroFilmes()

while True:
    print("\n----- Menu -----")
    print("1. Adicionar filme")
    print("2. Buscar filme")
    print("3. Mostrar lista de filmes")
    print("4. Remover filme")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_filme = input("Digite o nome do filme: ")
        cadastro.adicionar_filme(nome_filme)
    elif opcao == "2":
        nome_filme = input("Digite o nome do filme: ")
        filme_encontrado = cadastro.buscar_filme(nome_filme)
        if filme_encontrado:
            print("Filme encontrado:", filme_encontrado)
        else:
            print("Filme não encontrado.")
    elif opcao == "3":
        cadastro.mostrar_lista_filmes()
    elif opcao == "4":
        nome_filme = input("Digite o nome do filme: ")
        cadastro.remover_filme(nome_filme)
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
