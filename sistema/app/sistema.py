class Sistema:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self):
        tarefa = input("Adicione uma nova tarefa: ")
        self.tarefas.append({"Nome": tarefa, "Concluida": False})
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    def mostrar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada!")
            return

        print("--- Tarefas ---")
        for i, tarefa in enumerate(self.tarefas):
            status = " Concluída" if tarefa.get("Concluida", False) else " Não concluída"
            print(f"{i + 1}. {tarefa['Nome']} - {status}")

    def concluir_tarefas(self):
        self.mostrar_tarefas()
        if not self.tarefas:
            return
        try:
            indice = int(input("Informe o número da tarefa a concluir: ")) - 1
            if 0 <= indice < len(self.tarefas):
                self.tarefas[indice]["Concluida"] = True
                print(f"Tarefa '{self.tarefas[indice]['Nome']}' marcada como concluída!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, insira um número válido!")

    def excluir_tarefas(self):
        self.mostrar_tarefas()
        if not self.tarefas:
            return
        try:
            indice = int(input("Digite o número da tarefa a excluir: ")) - 1
            if 0 <= indice < len(self.tarefas):
                tarefa_removida = self.tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida['Nome']}' excluída!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, insira um número válido.")
