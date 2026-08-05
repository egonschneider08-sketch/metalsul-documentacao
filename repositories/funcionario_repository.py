# Arquivo: dao.py (ou dao/funcionario_dao.py)

from database.conexao import Conexao
from models.funcionario import Funcionario # Lembre-se de importar sua model aqui

class FuncionarioDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, funcionario):
        """Recebe um objeto Funcionario e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO funcionarios (nome, cpf, rg, data_nascimento, sexo, estado_civil, email, \
                                        telefone, celular, cargo, departamento, salario, \
                                        data_admissao, data_demissao, turno, status, observacoes) \
              VALUES (%s, %s, %s, %s, %s, %s, %s, \
                      %s, %s, %s, %s, %s, \
                      %s, %s, %s, %s, %s) RETURNING id_funcionario; \
              """

        valores = (
            funcionario.nome, funcionario.cpf, funcionario.rg, funcionario.data_nascimento,
            funcionario.sexo, funcionario.estado_civil, funcionario.email,
            funcionario.telefone, funcionario.celular, funcionario.cargo,
            funcionario.departamento, funcionario.salario, funcionario.data_admissao,
            funcionario.data_demissao, funcionario.turno, funcionario.status,
            funcionario.observacoes
        )

        try:
            # self.cursor e self.conexao devem vir da sua classe 'Conexao'
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            funcionario.id_funcionario = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Funcionário {funcionario.nome} inserido com ID {funcionario.id_funcionario}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir funcionário: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os funcionários e retorna uma lista de objetos Funcionario."""
        sql = "SELECT * FROM funcionarios;"
        lista_funcionarios = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                func = Funcionario(
                    id_funcionario=linha[0], nome=linha[1], cpf=linha[2], rg=linha[3],
                    data_nascimento=linha[4], sexo=linha[5], estado_civil=linha[6],
                    email=linha[7], telefone=linha[8], celular=linha[9], cargo=linha[10],
                    departamento=linha[11], salario=linha[12], data_admissao=linha[13],
                    data_demissao=linha[14], turno=linha[15], status=linha[16], observacoes=linha[17]
                )
                lista_funcionarios.append(func)

            return lista_funcionarios

        except Exception as e:
            print(f"Erro ao buscar funcionários: {e}")
            return []

    # Aqui você pode adicionar no futuro: atualizar(), deletar(), buscar_por_id()...