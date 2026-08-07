from database.conexao import Conexao
from models.item_pedido_compra import ItemPedidoCompra


class ItemPedidoCompraDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, item):
        """Insere um novo item de pedido de compra no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.item_pedido_compra
              (quantidade, valor_unitario, desconto, subtotal, id_pedido_compra, id_produto)
              VALUES (%s, %s, %s, %s, %s, %s)
              RETURNING id_item_compra;
              """

        valores = (
            item.quantidade,
            item.valor_unitario,
            item.desconto,
            item.subtotal,
            item.id_pedido_compra,
            item.id_produto
        )

        try:
            self.cursor.execute(sql, valores)
            item.id_item_compra = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Item de compra inserido com ID {item.id_item_compra}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir item do pedido de compra: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os itens de pedido de compra e retorna uma lista de objetos."""
        sql = "SELECT * FROM empresa.item_pedido_compra;"
        lista_itens = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                item = ItemPedidoCompra(
                    id_item_compra=linha[0],
                    quantidade=linha[1],
                    valor_unitario=linha[2],
                    desconto=linha[3],
                    subtotal=linha[4],
                    id_pedido_compra=linha[5],
                    id_produto=linha[6]
                )
                lista_itens.append(item)

            return lista_itens
        except Exception as e:
            print(f"Erro ao buscar itens do pedido de compra: {e}")
            return []

    def buscarItemPedidoCompra(self, id_item_compra):
        """Busca um item de pedido de compra pelo ID."""
        sql = "SELECT * FROM empresa.item_pedido_compra WHERE id_item_compra = %s"
        try:
            self.cursor.execute(sql, (id_item_compra,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar item do pedido de compra! Erro: {erro}")
            return None

    def ExcluirItemPedidoCompra(self, id_item_compra):
        """Exclui um item de pedido de compra pelo ID."""
        sql = "DELETE FROM empresa.item_pedido_compra WHERE id_item_compra = %s"
        try:
            self.cursor.execute(sql, (id_item_compra,))
            self.conexao.commit()
            print("Item do pedido de compra excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir item do pedido de compra! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")