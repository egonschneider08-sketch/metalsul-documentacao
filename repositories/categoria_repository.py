from database.conexao import Conexao
from models.categoria_produto import CategoriaProduto


class CategoriaProdutoDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, categoria):
        """Insere uma nova categoria de produto e atualiza o objeto com o ID gerado."""
        sql = """
              INSERT INTO empresa.categoria_produto
              (nome, descricao, ativo)
              VALUES (%s, %s, %s)
              RETURNING id_categoria;
              """

        valores = (categoria.nome, categoria.descricao, categoria.ativo)

        try:
            self.cursor.execute(sql, valores)
            categoria.id_categoria = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Categoria '{categoria.nome}' inserida com ID {categoria.id_categoria}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir categoria: {e}")
            return False

    def buscar_todos(self):
        """Busca todas as categorias e retorna uma lista de objetos CategoriaProduto."""
        sql = "SELECT * FROM empresa.categoria_produto;"
        lista_categorias = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                cat = CategoriaProduto(
                    id_categoria=linha[0],
                    nome=linha[1],
                    descricao=linha[2],
                    ativo=linha[3]
                )
                lista_categorias.append(cat)

            return lista_categorias
        except Exception as e:
            print(f"Erro ao buscar categorias: {e}")
            return []

    def buscarCategoria(self, id_categoria):
        """Busca uma categoria pelo ID e retorna o registro encontrado."""
        sql = "SELECT * FROM empresa.categoria_produto WHERE id_categoria = %s"
        try:
            self.cursor.execute(sql, (id_categoria,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar categoria! Erro: {erro}")
            return None

    def ExcluirCategoria(self, id_categoria):
        """Exclui uma categoria do banco de dados pelo ID."""
        sql = "DELETE FROM empresa.categoria_produto WHERE id_categoria = %s"
        try:
            self.cursor.execute(sql, (id_categoria,))
            self.conexao.commit()
            print("Categoria excluída com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir categoria! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")