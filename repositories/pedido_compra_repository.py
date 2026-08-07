from database.conexao import Conexao
from models.pedido_compra import PedidoCompra


class PedidoCompraDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, pedido):
        """Insere um novo pedido de compra no banco PostgreSQL e atualiza o objeto com o ID gerado."""
        sql = """
              INSERT INTO empresa.pedido_compra
              (data_pedido, data_entrega_prevista, data_entrega_real, valor_total,
               desconto, valor_final, status, condicao_pagamento, forma_pagamento,
               observacoes, id_fornecedor, id_funcionario)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_pedido_compra;
              """

        valores = (
            pedido.data_pedido,
            pedido.data_entrega_prevista,
            pedido.data_entrega_real,
            pedido.valor_total,
            pedido.desconto,
            pedido.valor_final,
            pedido.status,
            pedido.condicao_pagamento,
            pedido.forma_pagamento,
            pedido.observacoes,
            pedido.id_fornecedor,
            pedido.id_funcionario
        )

        try:
            self.cursor.execute(sql, valores)
            pedido.id_pedido_compra = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Pedido de compra inserido com ID {pedido.id_pedido_compra}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir pedido de compra: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os pedidos de compra e retorna uma lista de objetos PedidoCompra."""
        sql = "SELECT * FROM empresa.pedido_compra;"
        lista_pedidos = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                p = PedidoCompra(
                    id_pedido_compra=linha[0],
                    data_pedido=linha[1],
                    data_entrega_prevista=linha[2],
                    data_entrega_real=linha[3],
                    valor_total=linha[4],
                    desconto=linha[5],
                    valor_final=linha[6],
                    status=linha[7],
                    condicao_pagamento=linha[8],
                    forma_pagamento=linha[9],
                    observacoes=linha[10],
                    id_fornecedor=linha[11],
                    id_funcionario=linha[12]
                )
                lista_pedidos.append(p)

            return lista_pedidos
        except Exception as e:
            print(f"Erro ao buscar pedidos de compra: {e}")
            return []

    def buscarPedidoCompra(self, id_pedido_compra):
        """Busca um pedido de compra pelo ID."""
        sql = "SELECT * FROM empresa.pedido_compra WHERE id_pedido_compra = %s"
        try:
            self.cursor.execute(sql, (id_pedido_compra,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar pedido de compra! Erro: {erro}")
            return None

    def ExcluirPedidoCompra(self, id_pedido_compra):
        """Exclui um pedido de compra pelo ID."""
        sql = "DELETE FROM empresa.pedido_compra WHERE id_pedido_compra = %s"
        try:
            self.cursor.execute(sql, (id_pedido_compra,))
            self.conexao.commit()
            print("Pedido de compra excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir pedido de compra! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")