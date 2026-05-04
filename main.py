from steampy import SteamPy

def menu():
    sistema = SteamPy()

    while True:
        print("\n===== STEAMPY =====")
        print("1. Carregar catálogo")
        print("2. Buscar jogo por nome")
        print("3. Filtrar por gênero")
        print("4. Filtrar por console")
        print("5. Filtrar por nota")
        print("6. Adicionar ao backlog")
        print("7. Jogar próximo do backlog")
        print("8. Ver jogos recentes")
        print("9. Registrar sessão de jogo")
        print("10. Ver histórico")
        print("11. Ver dashboard")
        print("0. Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            sistema.carregar_jogos("dataset.csv")

        elif op == "2":
            termo = input("Digite o nome do jogo: ")
            sistema.buscar_jogo_por_nome(termo)

        elif op == "3":
            genero = input("Digite o gênero: ")
            sistema.filtrar_por_genero(genero)

        elif op == "4":
            console = input("Digite o console: ")
            sistema.filtrar_por_console(console)

        elif op == "5":
            try:
                nota = float(input("Digite a nota mínima: "))
                sistema.filtrar_por_nota(nota)
            except:
                print("Digite um número válido!")

        elif op == "6":
            try:
                id_jogo = int(input("Digite o ID do jogo: "))
                sistema.adicionar_ao_backlog(id_jogo)
            except:
                print("ID inválido!")

        elif op == "7":
            sistema.jogar_proximo()

        elif op == "8":
            sistema.recentes.mostrar()

        elif op == "9":
            try:
                id_jogo = int(input("Digite o ID do jogo: "))
                tempo = float(input("Digite as horas jogadas: "))
                sistema.registrar_sessao(id_jogo, tempo)
            except:
                print("Dados inválidos!")

        elif op == "10":
            sistema.mostrar_historico()

        elif op == "11":
            sistema.exibir_dashboard()

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()