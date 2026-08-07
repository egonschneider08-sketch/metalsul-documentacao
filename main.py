from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioDAO


def exibir_menu():
    print("\n" + "=" * 40)
    print(" SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS ".center(40))
    print("=" * 40)
    print("1. Inserir novo funcionário")
    print("2. Listar todos os funcionários")
    print("3. Buscar funcionário por ID")
    print("4. Excluir funcionário")
    print("0. Sair")
    print("=" * 40)


def main():
    dao = FuncionarioDAO()

    while True:
        exibir_menu()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Funcionário ---")
            nome = input("Nome: ")
            cpf = input("CPF (apenas números): ")
            cargo = input("Cargo: ")

            # Criando o objeto com os dados digitados e preenchendo o resto com dados mockados (teste)
            novo_funcionario = Funcionario(
                nome=nome,
                cpf=cpf,
                rg="00.000.000-0",
                data_nascimento="1990-01-01",
                sexo="M",
                estado_civil="Solteiro",
                email=f"{nome.lower().replace(' ', '.')}@email.com",
                telefone="0000000000",
                celular="00000000000",
                cargo=cargo,
                departamento="Geral",
                salario=3000.00,
                data_admissao="2026-08-07",
                data_demissao=None,
                turno="Comercial",
                status="ATIVO",
                observacoes="Inserido via menu interativo."
            )

            dao.inserir(novo_funcionario)

        elif opcao == "2":
            print("\n--- Lista de Funcionários ---")
            funcionarios = dao.buscar_todos()
            if funcionarios:
                for f in funcionarios:
                    # Garantindo o acesso seguro aos atributos
                    f_id = getattr(f, 'id_funcionario', 'N/A')
                    print(f"ID: {f_id} | Nome: {f.nome} | CPF: {f.cpf} | Cargo: {f.cargo}")
            else:
                print("Nenhum funcionário cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Funcionário ---")
            try:
                id_busca = int(input("Digite o ID do funcionário: "))
                resultado = dao.buscarFuncionario(id_busca)
                if resultado:
                    print(f"Funcionário encontrado: {resultado}")
                else:
                    print("Funcionário não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Funcionário ---")
            try:
                id_exclusao = int(input("Digite o ID do funcionário a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirFuncionario(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()