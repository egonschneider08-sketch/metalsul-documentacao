from database.conexao import Conexao
from models.pedido_venda import PedidoVenda


class PedidoVendaDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, pedido):
        """Insere um novo pedido de venda no banco PostgreSQL e atualiza o objeto com o ID gerado."""
        sql = """
              INSERT INTO empresa.pedido_venda
              (data_pedido, data_entrega_prevista, data_entrega_real, valor_total,
               desconto, valor_final, status, condicao_pagamento, forma_pagamento,
               observacoes, id_cliente, id_funcionario)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_pedido_venda;
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
            pedido.id_cliente,
            pedido.id_funcionario
        )

        try:
            self.cursor.execute(sql, valores)
            pedido.id_pedido_venda = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Pedido de venda inserido com ID {pedido.id_pedido_venda}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir pedido de venda: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os pedidos de venda e retorna uma lista de objetos PedidoVenda."""
        sql = "SELECT * FROM empresa.pedido_venda;"
        lista_pedidos = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                p = PedidoVenda(
                    id_pedido_venda=linha[0],
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
                    id_cliente=linha[11],
                    id_funcionario=linha[12]
                )
                lista_pedidos.append(p)

            return lista_pedidos
        except Exception as e:
            print(f"Erro ao buscar pedidos de venda: {e}")
            return []

    def buscarPedidoVenda(self, id_pedido_venda):
        """Busca um pedido de venda pelo ID."""
        sql = "SELECT * FROM empresa.pedido_venda WHERE id_pedido_venda = %s"
        try:
            self.cursor.execute(sql, (id_pedido_venda,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar pedido de venda! Erro: {erro}")
            return None

    def ExcluirPedidoVenda(self, id_pedido_venda):
        """Exclui um pedido de venda pelo ID."""
        sql = "DELETE FROM empresa.pedido_venda WHERE id_pedido_venda = %s"
        try:
            self.cursor.execute(sql, (id_pedido_venda,))
            self.conexao.commit()
            print("Pedido de venda excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir pedido de venda! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")