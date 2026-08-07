from database.conexao import Conexao


class PedidoVenda(Conexao):
    def __init__(self,
                 id_pedido_venda=None,
                 data_pedido=None,
                 data_entrega_prevista=None,
                 data_entrega_real=None,
                 valor_total=0.0,
                 desconto=0.0,
                 valor_final=0.0,
                 status="PENDENTE",
                 condicao_pagamento="",
                 forma_pagamento="",
                 observacoes="",
                 id_cliente=None,
                 id_funcionario=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_pedido_venda = id_pedido_venda
        self.data_pedido = data_pedido
        self.data_entrega_prevista = data_entrega_prevista
        self.data_entrega_real = data_entrega_real
        self.valor_total = valor_total
        self.desconto = desconto
        self.valor_final = valor_final
        self.status = status
        self.condicao_pagamento = condicao_pagamento
        self.forma_pagamento = forma_pagamento
        self.observacoes = observacoes
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario