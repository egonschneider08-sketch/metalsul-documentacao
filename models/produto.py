from database.conexao import Conexao


class Produto(Conexao):
    def __init__(self,
                 id_produto=None,
                 nome="",
                 descricao="",
                 codigo_barras="",
                 preco_custo=0.0,
                 preco_venda=0.0,
                 quantidade_estoque=0,
                 estoque_minimo=0,
                 unidade_medida="UN",
                 status="ATIVO",
                 data_cadastro=None,
                 observacoes="",
                 id_categoria=None,
                 id_fornecedor=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.quantidade_estoque = quantidade_estoque
        self.estoque_minimo = estoque_minimo
        self.unidade_medida = unidade_medida
        self.status = status
        self.data_cadastro = data_cadastro
        self.observacoes = observacoes
        self.id_categoria = id_categoria
        self.id_fornecedor = id_fornecedor