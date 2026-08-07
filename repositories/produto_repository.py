from database.conexao import Conexao
from models.produto import Produto


class ProdutoDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, produto):
        """Insere um novo produto no banco PostgreSQL e atualiza o objeto com o ID gerado."""
        sql = """
              INSERT INTO empresa.produto
              (nome, descricao, codigo_barras, preco_custo, preco_venda,
               quantidade_estoque, estoque_minimo, unidade_medida, status,
               data_cadastro, observacoes, id_categoria, id_fornecedor)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_produto;
              """

        valores = (
            produto.nome,
            produto.descricao,
            produto.codigo_barras,
            produto.preco_custo,
            produto.preco_venda,
            produto.quantidade_estoque,
            produto.estoque_minimo,
            produto.unidade_medida,
            produto.status,
            produto.data_cadastro,
            produto.observacoes,
            produto.id_categoria,
            produto.id_fornecedor
        )

        try:
            self.cursor.execute(sql, valores)
            produto.id_produto = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Produto inserido com ID {produto.id_produto}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir produto: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os produtos e retorna uma lista de objetos Produto."""
        sql = "SELECT * FROM empresa.produto;"
        lista_produtos = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                p = Produto(
                    id_produto=linha[0],
                    nome=linha[1],
                    descricao=linha[2],
                    codigo_barras=linha[3],
                    preco_custo=linha[4],
                    preco_venda=linha[5],
                    quantidade_estoque=linha[6],
                    estoque_minimo=linha[7],
                    unidade_medida=linha[8],
                    status=linha[9],
                    data_cadastro=linha[10],
                    observacoes=linha[11],
                    id_categoria=linha[12],
                    id_fornecedor=linha[13]
                )
                lista_produtos.append(p)

            return lista_produtos
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
            return []

    def buscarProduto(self, id_produto):
        """Busca um produto pelo ID."""
        sql = "SELECT * FROM empresa.produto WHERE id_produto = %s"
        try:
            self.cursor.execute(sql, (id_produto,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar produto! Erro: {erro}")
            return None

    def ExcluirProduto(self, id_produto):
        """Exclui um produto pelo ID."""
        sql = "DELETE FROM empresa.produto WHERE id_produto = %s"
        try:
            self.cursor.execute(sql, (id_produto,))
            self.conexao.commit()
            print("Produto excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir produto! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")