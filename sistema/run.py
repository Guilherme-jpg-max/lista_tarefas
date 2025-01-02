import os
from app.sistema import Sistema


# Função para limpar terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Mostrar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")


def main():

    sistema = Sistema()

    while True:
        limpar_tela()
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            sistema.adicionar_tarefa()
        elif escolha == "2":
            sistema.mostrar_tarefas()
        elif escolha == "3":
            sistema.concluir_tarefas()
        elif escolha == "4":
            sistema.excluir_tarefas()
        elif escolha == "5":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        # função para pausar o sys que limpa o terminal
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
