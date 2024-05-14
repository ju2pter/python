

"""
Este projeto terá as seguintes funcionalidades:

1- Adicionar um novo funcionário.
2- Listar todos os funcionários.
3- Buscar um funcionário pelo seu ID.
4- Remover um funcionário pelo seu ID.
"""



class Empresa:
    def __init__(self):
        self.funcionarios = []
        self.proximo_id = 1

    def adicionar_funcionario(self, nome, cargo):
        self.funcionarios.append({"id": self.proximo_id, "nome": nome, "cargo": cargo})
        self.proximo_id += 1
        print(f"Funcionário '{nome}' adicionado com sucesso!")

    def listar_funcionarios(self):
        print("Lista de Funcionários:")
        for funcionario in self.funcionarios:
            print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}")

    def buscar_funcionario_por_id(self, id):
        for funcionario in self.funcionarios:
            if funcionario['id'] == id:
                print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}")
                return
        print(f"Funcionário com ID {id} não encontrado.")

    def remover_funcionario_por_id(self, id):
        for funcionario in self.funcionarios:
            if funcionario['id'] == id:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário '{funcionario['nome']}' removido com sucesso.")
                return
        print(f"Funcionário com ID {id} não encontrado.")


# Função para mostrar as opções do menu
def mostrar_menu():
    print("\n### Sistema de Gerenciamento de Funcionários ###")
    print("1. Adicionar Funcionário")
    print("2. Listar Funcionários")
    print("3. Buscar Funcionário por ID")
    print("4. Remover Funcionário por ID")
    print("5. Sair")


if __name__ == "__main__":
    empresa = Empresa()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            empresa.adicionar_funcionario(nome, cargo)
        elif opcao == "2":
            empresa.listar_funcionarios()
        elif opcao == "3":
            id = int(input("Digite o ID do funcionário: "))
            empresa.buscar_funcionario_por_id(id)
        elif opcao == "4":
            id = int(input("Digite o ID do funcionário a ser removido: "))
            empresa.remover_funcionario_por_id(id)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
