from database.conexao import Conexao
from models.item_pedido_venda import ItemPedidoVenda


class ItemPedidoVendaDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, item):
        """Insere um novo item de pedido de venda no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.item_pedido_venda
              (quantidade, valor_unitario, desconto, subtotal, id_pedido_venda, id_produto)
              VALUES (%s, %s, %s, %s, %s, %s)
              RETURNING id_item_venda;
              """

        valores = (
            item.quantidade,
            item.valor_unitario,
            item.desconto,
            item.subtotal,
            item.id_pedido_venda,
            item.id_produto
        )

        try:
            self.cursor.execute(sql, valores)
            item.id_item_venda = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Item de venda inserido com ID {item.id_item_venda}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir item do pedido de venda: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os itens de pedido de venda e retorna uma lista de objetos."""
        sql = "SELECT * FROM empresa.item_pedido_venda;"
        lista_itens = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                item = ItemPedidoVenda(
                    id_item_venda=linha[0],
                    quantidade=linha[1],
                    valor_unitario=linha[2],
                    desconto=linha[3],
                    subtotal=linha[4],
                    id_pedido_venda=linha[5],
                    id_produto=linha[6]
                )
                lista_itens.append(item)

            return lista_itens
        except Exception as e:
            print(f"Erro ao buscar itens do pedido de venda: {e}")
            return []

    def buscarItemPedidoVenda(self, id_item_venda):
        """Busca um item de pedido de venda pelo ID."""
        sql = "SELECT * FROM empresa.item_pedido_venda WHERE id_item_venda = %s"
        try:
            self.cursor.execute(sql, (id_item_venda,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar item do pedido de venda! Erro: {erro}")
            return None

    def ExcluirItemPedidoVenda(self, id_item_venda):
        """Exclui um item de pedido de venda pelo ID."""
        sql = "DELETE FROM empresa.item_pedido_venda WHERE id_item_venda = %s"
        try:
            self.cursor.execute(sql, (id_item_venda,))
            self.conexao.commit()
            print("Item do pedido de venda excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir item do pedido de venda! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")