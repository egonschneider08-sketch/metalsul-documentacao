from database.conexao import Conexao


class ItemPedidoCompra(Conexao):
    def __init__(self,
                 id_item_compra=None,
                 quantidade=0,
                 valor_unitario=0.0,
                 desconto=0.0,
                 subtotal=0.0,
                 id_pedido_compra=None,
                 id_produto=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_item_compra = id_item_compra
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.desconto = desconto
        self.subtotal = subtotal
        self.id_pedido_compra = id_pedido_compra
        self.id_produto = id_produto