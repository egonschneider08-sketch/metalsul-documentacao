from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioDAO
from models.fornecedor import Fornecedor
from repositories.fornecedor_repository import FornecedorDAO
from models.cliente import Cliente
from repositories.cliente_repository import ClienteDAO
from models.categoria_produto import CategoriaProduto
from repositories.categoria_repository import CategoriaProdutoDAO


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
# SUBMENU: CLIENTES
# ==========================================================
def exibir_menu_cliente():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE CLIENTES ".center(40))
    print("=" * 40)
    print("1. Inserir novo cliente")
    print("2. Listar todos os clientes")
    print("3. Buscar cliente por ID")
    print("4. Excluir cliente")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_cliente():
    dao = ClienteDAO()

    while True:
        exibir_menu_cliente()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Cliente ---")
            nome = input("Nome: ")
            cpf_cnpj = input("CPF ou CNPJ: ")
            tipo_cliente = input("Tipo (PF/PJ) [Padrão PF]: ").upper() or "PF"

            novo_cliente = Cliente(
                tipo_cliente=tipo_cliente,
                nome=nome,
                cpf_cnpj=cpf_cnpj,
                inscricao_estadual="",
                email=f"{nome.lower().replace(' ', '.')}@cliente.com",
                telefone="0000000000",
                celular="00000000000",
                cep="00000000",
                endereco="Rua do Cliente",
                numero="123",
                complemento="",
                bairro="Centro",
                cidade="Cidade",
                estado="UF",
                pais="Brasil",
                limite_credito=1000.00,
                data_cadastro="2026-08-07",
                status="ATIVO",
                observacoes="Inserido via menu interativo."
            )

            dao.inserir(novo_cliente)

        elif opcao == "2":
            print("\n--- Lista de Clientes ---")
            clientes = dao.buscar_todos()
            if clientes:
                for c in clientes:
                    c_id = getattr(c, 'id_cliente', 'N/A')
                    print(f"ID: {c_id} | Nome: {c.nome} | CPF/CNPJ: {c.cpf_cnpj} | Tipo: {c.tipo_cliente}")
            else:
                print("Nenhum cliente cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Cliente ---")
            try:
                id_busca = int(input("Digite o ID do cliente: "))
                resultado = dao.buscarCliente(id_busca)
                if resultado:
                    print(f"Cliente encontrado: {resultado}")
                else:
                    print("Cliente não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Cliente ---")
            try:
                id_exclusao = int(input("Digite o ID do cliente a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirCliente(id_exclusao)
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
# SUBMENU: CATEGORIAS DE PRODUTO
# ==========================================================
def exibir_menu_categoria():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE CATEGORIAS ".center(40))
    print("=" * 40)
    print("1. Inserir nova categoria")
    print("2. Listar todas as categorias")
    print("3. Buscar categoria por ID")
    print("4. Excluir categoria")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_categoria():
    dao = CategoriaProdutoDAO()

    while True:
        exibir_menu_categoria()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Categoria ---")
            nome = input("Nome da Categoria: ")
            descricao = input("Descrição: ")

            nova_categoria = CategoriaProduto(
                nome=nome,
                descricao=descricao,
                ativo=True
            )

            dao.inserir(nova_categoria)

        elif opcao == "2":
            print("\n--- Lista de Categorias ---")
            categorias = dao.buscar_todos()
            if categorias:
                for cat in categorias:
                    cat_id = getattr(cat, 'id_categoria', 'N/A')
                    status = "Ativo" if cat.ativo else "Inativo"
                    print(f"ID: {cat_id} | Nome: {cat.nome} | Descrição: {cat.descricao} | Status: {status}")
            else:
                print("Nenhuma categoria cadastrada ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Categoria ---")
            try:
                id_busca = int(input("Digite o ID da categoria: "))
                resultado = dao.buscarCategoria(id_busca)
                if resultado:
                    print(f"Categoria encontrada: {resultado}")
                else:
                    print("Categoria não encontrada com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Categoria ---")
            try:
                id_exclusao = int(input("Digite o ID da categoria a ser excluída: "))
                confirmacao = input(f"Tem certeza que deseja excluir a categoria ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirCategoria(id_exclusao)
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
    print("3. Gerenciar Clientes")
    print("4. Gerenciar Categorias de Produtos")
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
        elif opcao == "3":
            menu_cliente()
        elif opcao == "4":
            menu_categoria()
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()