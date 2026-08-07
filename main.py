from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioDAO
from models.fornecedor import Fornecedor
from repositories.fornecedor_repository import FornecedorDAO


# ==========================================================
# SUBMENU: FUNCIONÁRIOS
# ==========================================================
def exibir_menu_funcionario():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE FUNCIONÁRIOS ".center(40))
    print("=" * 40)
    print("1. Inserir novo funcionário")
    print("2. Listar todos os funcionários")
    print("3. Buscar funcionário por ID")
    print("4. Excluir funcionário")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_funcionario():
    dao = FuncionarioDAO()

    while True:
        exibir_menu_funcionario()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Funcionário ---")
            nome = input("Nome: ")
            cpf = input("CPF (apenas números): ")
            cargo = input("Cargo: ")

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
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: FORNECEDORES
# ==========================================================
def exibir_menu_fornecedor():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE FORNECEDORES ".center(40))
    print("=" * 40)
    print("1. Inserir novo fornecedor")
    print("2. Listar todos os fornecedores")
    print("3. Buscar fornecedor por ID")
    print("4. Excluir fornecedor")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_fornecedor():
    dao = FornecedorDAO()

    while True:
        exibir_menu_fornecedor()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Fornecedor ---")
            razao_social = input("Razão Social: ")
            nome_fantasia = input("Nome Fantasia: ")
            cnpj = input("CNPJ (14 dígitos): ")

            novo_fornecedor = Fornecedor(
                razao_social=razao_social,
                nome_fantasia=nome_fantasia,
                cnpj=cnpj,
                inscricao_estadual="123456789",
                email=f"{razao_social.lower().replace(' ', '')}@fornecedor.com",
                telefone="0000000000",
                celular="00000000000",
                site="www.fornecedor.com",
                cep="00000000",
                endereco="Rua do Fornecedor",
                numero="100",
                complemento="",
                bairro="Industrial",
                cidade="Cidade",
                estado="UF",
                pais="Brasil",
                nome_contato="Contato Comercial",
                cargo_contato="Vendedor",
                status="ATIVO",
                observacoes="Inserido via menu interativo."
            )

            dao.inserir(novo_fornecedor)

        elif opcao == "2":
            print("\n--- Lista de Fornecedores ---")
            fornecedores = dao.buscar_todos()
            if fornecedores:
                for f in fornecedores:
                    f_id = getattr(f, 'id_fornecedor', 'N/A')
                    print(f"ID: {f_id} | Razão Social: {f.razao_social} | CNPJ: {f.cnpj} | Nome Fantasia: {f.nome_fantasia}")
            else:
                print("Nenhum fornecedor cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Fornecedor ---")
            try:
                id_busca = int(input("Digite o ID do fornecedor: "))
                resultado = dao.buscarFornecedor(id_busca)
                if resultado:
                    print(f"Fornecedor encontrado: {resultado}")
                else:
                    print("Fornecedor não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Fornecedor ---")
            try:
                id_exclusao = int(input("Digite o ID do fornecedor a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirFornecedor(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break
else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# MENU PRINCIPAL
# ==========================================================
def exibir_menu_principal():
    print("\n" + "=" * 40)
    print(" SISTEMA DE GESTÃO DA EMPRESA ".center(40))
    print("=" * 40)
    print("1. Gerenciar Funcionários")
    print("2. Gerenciar Fornecedores")
    print("0. Sair do Sistema")
    print("=" * 40)


def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha o módulo desejado: ")

        if opcao == "1":
            menu_funcionario()
        elif opcao == "2":
            menu_fornecedor()
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
