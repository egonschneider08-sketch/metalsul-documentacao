from database.conexao import Conexao


class Usuario(Conexao):
    def __init__(self,
                 id_usuario=None,
                 nome="",
                 email="",
                 senha="",
                 perfil="OPERADOR",
                 status="ATIVO",
                 data_cadastro=None,
                 ultimo_acesso=None,
                 observacoes="",
                 id_funcionario=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.status = status
        self.data_cadastro = data_cadastro
        self.ultimo_acesso = ultimo_acesso
        self.observacoes = observacoes
        self.id_funcionario = id_funcionario