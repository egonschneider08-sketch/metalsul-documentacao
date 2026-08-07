from database.conexao import Conexao
from models.usuario import Usuario


class UsuarioDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, usuario):
        """Insere um novo usuário no banco PostgreSQL e atualiza o objeto com o ID gerado."""
        sql = """
              INSERT INTO empresa.usuario
              (nome, email, senha, perfil, status, data_cadastro, ultimo_acesso, observacoes, id_funcionario)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_usuario;
              """

        valores = (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.perfil,
            usuario.status,
            usuario.data_cadastro,
            usuario.ultimo_acesso,
            usuario.observacoes,
            usuario.id_funcionario
        )

        try:
            self.cursor.execute(sql, valores)
            usuario.id_usuario = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Usuário inserido com ID {usuario.id_usuario}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir usuário: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os usuários e retorna uma lista de objetos Usuario."""
        sql = "SELECT * FROM empresa.usuario;"
        lista_usuarios = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                u = Usuario(
                    id_usuario=linha[0],
                    nome=linha[1],
                    email=linha[2],
                    senha=linha[3],
                    perfil=linha[4],
                    status=linha[5],
                    data_cadastro=linha[6],
                    ultimo_acesso=linha[7],
                    observacoes=linha[8],
                    id_funcionario=linha[9]
                )
                lista_usuarios.append(u)

            return lista_usuarios
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            return []

    def buscarUsuario(self, id_usuario):
        """Busca um usuário pelo ID."""
        sql = "SELECT * FROM empresa.usuario WHERE id_usuario = %s"
        try:
            self.cursor.execute(sql, (id_usuario,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar usuário! Erro: {erro}")
            return None

    def ExcluirUsuario(self, id_usuario):
        """Exclui um usuário pelo ID."""
        sql = "DELETE FROM empresa.usuario WHERE id_usuario = %s"
        try:
            self.cursor.execute(sql, (id_usuario,))
            self.conexao.commit()
            print("Usuário excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir usuário! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")