from main import menu_funcionario
from main import menu_fornecedor
from main import menu_cliente
from main import menu_categoria
from main import menu_produto
from main import menu_usuario
from main import menu_item_compra
from main import menu_item_venda
from main import menu_pedido_compra
from main import menu_pedido_venda


def exibir_menu_principal():
    print("\n" + "=" * 40)
    print(" SISTEMA DE GESTÃO DA EMPRESA ".center(40))
    print("=" * 40)
    print("1. Gerenciar Funcionários")
    print("2. Gerenciar Fornecedores")
    print("3. Gerenciar Clientes")
    print("4. Gerenciar Categorias de Produtos")
    print("5. Gerenciar Produtos")
    print("6. Gerenciar Usuários")
    print("7. Gerenciar Itens de Pedido de Compra")
    print("8. Gerenciar Itens de Pedido de Venda")
    print("9. Gerenciar Pedidos de Compra")
    print("10. Gerenciar Pedidos de Venda")
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
            menu_produto()
        elif opcao == "6":
            menu_usuario()
        elif opcao == "7":
            menu_item_compra()
        elif opcao == "8":
            menu_item_venda()
        elif opcao == "9":
            menu_pedido_compra()
        elif opcao == "10":
            menu_pedido_venda()
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()