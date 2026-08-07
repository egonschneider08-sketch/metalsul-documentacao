from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioDAO
from models.fornecedor import Fornecedor
from repositories.fornecedor_repository import FornecedorDAO
from models.cliente import Cliente
from repositories.cliente_repository import ClienteDAO
from models.categoria_produto import CategoriaProduto
from repositories.categoria_repository import CategoriaProdutoDAO
from models.item_pedido_compra import ItemPedidoCompra
from repositories.item_pedido_compra_repository import ItemPedidoCompraDAO
from models.item_pedido_venda import ItemPedidoVenda
from repositories.item_pedido_venda_repository import ItemPedidoVendaDAO
from models.pedido_compra import PedidoCompra
from repositories.pedido_compra_repository import PedidoCompraDAO
from models.pedido_venda import PedidoVenda
from repositories.pedido_venda_repository import PedidoVendaDAO


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
# SUBMENU: ITENS DE PEDIDO DE COMPRA
# ==========================================================
def exibir_menu_item_compra():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE ITENS DE COMPRA ".center(40))
    print("=" * 40)
    print("1. Inserir novo item de compra")
    print("2. Listar todos os itens de compra")
    print("3. Buscar item de compra por ID")
    print("4. Excluir item de compra")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_item_compra():
    dao = ItemPedidoCompraDAO()

    while True:
        exibir_menu_item_compra()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Item de Compra ---")
            try:
                id_pedido_compra = int(input("ID do Pedido de Compra: "))
                id_produto = int(input("ID do Produto: "))
                quantidade = int(input("Quantidade: "))
                valor_unitario = float(input("Valor Unitário: "))
                desconto_in = input("Desconto [Padrão 0.0]: ")
                desconto = float(desconto_in) if desconto_in else 0.0

                subtotal = (quantidade * valor_unitario) - desconto

                novo_item = ItemPedidoCompra(
                    quantidade=quantidade,
                    valor_unitario=valor_unitario,
                    desconto=desconto,
                    subtotal=subtotal,
                    id_pedido_compra=id_pedido_compra,
                    id_produto=id_produto
                )

                dao.inserir(novo_item)
            except ValueError:
                print("Por favor, informe valores numéricos válidos.")

        elif opcao == "2":
            print("\n--- Lista de Itens de Compra ---")
            itens = dao.buscar_todos()
            if itens:
                for i in itens:
                    i_id = getattr(i, 'id_item_compra', 'N/A')
                    print(f"ID: {i_id} | Pedido ID: {i.id_pedido_compra} | Produto ID: {i.id_produto} | Qtd: {i.quantidade} | Subtotal: R$ {i.subtotal:.2f}")
            else:
                print("Nenhum item cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Item de Compra ---")
            try:
                id_busca = int(input("Digite o ID do item de compra: "))
                resultado = dao.buscarItemPedidoCompra(id_busca)
                if resultado:
                    print(f"Item encontrado: {resultado}")
                else:
                    print("Item não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Item de Compra ---")
            try:
                id_exclusao = int(input("Digite o ID do item de compra a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirItemPedidoCompra(id_exclusao)
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
# SUBMENU: ITENS DE PEDIDO DE VENDA
# ==========================================================
def exibir_menu_item_venda():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE ITENS DE VENDA ".center(40))
    print("=" * 40)
    print("1. Inserir novo item de venda")
    print("2. Listar todos os itens de venda")
    print("3. Buscar item de venda por ID")
    print("4. Excluir item de venda")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_item_venda():
    dao = ItemPedidoVendaDAO()

    while True:
        exibir_menu_item_venda()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Item de Venda ---")
            try:
                id_pedido_venda = int(input("ID do Pedido de Venda: "))
                id_produto = int(input("ID do Produto: "))
                quantidade = int(input("Quantidade: "))
                valor_unitario = float(input("Valor Unitário: "))
                desconto_in = input("Desconto [Padrão 0.0]: ")
                desconto = float(desconto_in) if desconto_in else 0.0

                subtotal = (quantidade * valor_unitario) - desconto

                novo_item = ItemPedidoVenda(
                    quantidade=quantidade,
                    valor_unitario=valor_unitario,
                    desconto=desconto,
                    subtotal=subtotal,
                    id_pedido_venda=id_pedido_venda,
                    id_produto=id_produto
                )

                dao.inserir(novo_item)
            except ValueError:
                print("Por favor, informe valores numéricos válidos.")

        elif opcao == "2":
            print("\n--- Lista de Itens de Venda ---")
            itens = dao.buscar_todos()
            if itens:
                for i in itens:
                    i_id = getattr(i, 'id_item_venda', 'N/A')
                    print(f"ID: {i_id} | Pedido ID: {i.id_pedido_venda} | Produto ID: {i.id_produto} | Qtd: {i.quantidade} | Subtotal: R$ {i.subtotal:.2f}")
            else:
                print("Nenhum item cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Item de Venda ---")
            try:
                id_busca = int(input("Digite o ID do item de venda: "))
                resultado = dao.buscarItemPedidoVenda(id_busca)
                if resultado:
                    print(f"Item encontrado: {resultado}")
                else:
                    print("Item não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Item de Venda ---")
            try:
                id_exclusao = int(input("Digite o ID do item de venda a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirItemPedidoVenda(id_exclusao)
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
# SUBMENU: PEDIDOS DE COMPRA
# ==========================================================
def exibir_menu_pedido_compra():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE PEDIDOS DE COMPRA ".center(40))
    print("=" * 40)
    print("1. Inserir novo pedido de compra")
    print("2. Listar todos os pedidos de compra")
    print("3. Buscar pedido de compra por ID")
    print("4. Excluir pedido de compra")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_pedido_compra():
    dao = PedidoCompraDAO()

    while True:
        exibir_menu_pedido_compra()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Pedido de Compra ---")
            try:
                id_fornecedor = int(input("ID do Fornecedor: "))
                id_funcionario = int(input("ID do Funcionário Responsável: "))
                valor_total = float(input("Valor Total: "))
                desconto_in = input("Desconto [Padrão 0.0]: ")
                desconto = float(desconto_in) if desconto_in else 0.0
                valor_final = valor_total - desconto

                condicao_pagamento = input("Condição de Pagamento (ex: 30 dias): ") or "À Vista"
                forma_pagamento = input("Forma de Pagamento (ex: PIX, Boleto): ") or "Boleto"

                novo_pedido = PedidoCompra(
                    data_pedido="2026-08-07",
                    data_entrega_prevista="2026-08-15",
                    data_entrega_real=None,
                    valor_total=valor_total,
                    desconto=desconto,
                    valor_final=valor_final,
                    status="PENDENTE",
                    condicao_pagamento=condicao_pagamento,
                    forma_pagamento=forma_pagamento,
                    observacoes="Inserido via menu interativo.",
                    id_fornecedor=id_fornecedor,
                    id_funcionario=id_funcionario
                )

                dao.inserir(novo_pedido)
            except ValueError:
                print("Por favor, informe valores numéricos válidos.")

        elif opcao == "2":
            print("\n--- Lista de Pedidos de Compra ---")
            pedidos = dao.buscar_todos()
            if pedidos:
                for p in pedidos:
                    p_id = getattr(p, 'id_pedido_compra', 'N/A')
                    print(f"ID: {p_id} | Fornecedor ID: {p.id_fornecedor} | Data: {p.data_pedido} | Valor Final: R$ {p.valor_final:.2f} | Status: {p.status}")
            else:
                print("Nenhum pedido de compra cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Pedido de Compra ---")
            try:
                id_busca = int(input("Digite o ID do pedido de compra: "))
                resultado = dao.buscarPedidoCompra(id_busca)
                if resultado:
                    print(f"Pedido encontrado: {resultado}")
                else:
                    print("Pedido de compra não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Pedido de Compra ---")
            try:
                id_exclusao = int(input("Digite o ID do pedido de compra a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirPedidoCompra(id_exclusao)
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
# SUBMENU: PEDIDOS DE VENDA
# ==========================================================
def exibir_menu_pedido_venda():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE PEDIDOS DE VENDA ".center(40))
    print("=" * 40)
    print("1. Inserir novo pedido de venda")
    print("2. Listar todos os pedidos de venda")
    print("3. Buscar pedido de venda por ID")
    print("4. Excluir pedido de venda")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_pedido_venda():
    dao = PedidoVendaDAO()

    while True:
        exibir_menu_pedido_venda()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Pedido de Venda ---")
            try:
                id_cliente = int(input("ID do Cliente: "))
                id_funcionario = int(input("ID do Funcionário Responsável: "))
                valor_total = float(input("Valor Total: "))
                desconto_in = input("Desconto [Padrão 0.0]: ")
                desconto = float(desconto_in) if desconto_in else 0.0
                valor_final = valor_total - desconto

                condicao_pagamento = input("Condição de Pagamento (ex: À Vista, 30 dias): ") or "À Vista"
                forma_pagamento = input("Forma de Pagamento (ex: PIX, Cartão): ") or "PIX"

                novo_pedido = PedidoVenda(
                    data_pedido="2026-08-07",
                    data_entrega_prevista="2026-08-15",
                    data_entrega_real=None,
                    valor_total=valor_total,
                    desconto=desconto,
                    valor_final=valor_final,
                    status="PENDENTE",
                    condicao_pagamento=condicao_pagamento,
                    forma_pagamento=forma_pagamento,
                    observacoes="Inserido via menu interativo.",
                    id_cliente=id_cliente,
                    id_funcionario=id_funcionario
                )

                dao.inserir(novo_pedido)
            except ValueError:
                print("Por favor, informe valores numéricos válidos.")

        elif opcao == "2":
            print("\n--- Lista de Pedidos de Venda ---")
            pedidos = dao.buscar_todos()
            if pedidos:
                for p in pedidos:
                    p_id = getattr(p, 'id_pedido_venda', 'N/A')
                    print(f"ID: {p_id} | Cliente ID: {p.id_cliente} | Data: {p.data_pedido} | Valor Final: R$ {p.valor_final:.2f} | Status: {p.status}")
            else:
                print("Nenhum pedido de venda cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Pedido de Venda ---")
            try:
                id_busca = int(input("Digite o ID do pedido de venda: "))
                resultado = dao.buscarPedidoVenda(id_busca)
                if resultado:
                    print(f"Pedido encontrado: {resultado}")
                else:
                    print("Pedido de venda não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Pedido de Venda ---")
            try:
                id_exclusao = int(input("Digite o ID do pedido de venda a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirPedidoVenda(id_exclusao)
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
    print("5. Gerenciar Itens de Pedido de Compra")
    print("6. Gerenciar Itens de Pedido de Venda")
    print("7. Gerenciar Pedidos de Compra")
    print("8. Gerenciar Pedidos de Venda")
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
        elif opcao == "5":
            menu_item_compra()
        elif opcao == "6":
            menu_item_venda()
        elif opcao == "7":
            menu_pedido_compra()
        elif opcao == "8":
            menu_pedido_venda()
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()