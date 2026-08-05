#from database.conexao import Conexao
from models.funcionario import Funcionario
from repositories import Funcionario
from repositories.funcionario_repository import FuncionarioDAO

def main():
    # Arquivo: main.py

    # Importações hipotéticas das suas pastas
    # from models.funcionario import Funcionario
    # from dao.funcionario_dao import FuncionarioDAO

    # 1. Cria o objeto contendo os dados do funcionário
    novo_funcionario = Funcionario(
        nome="Maria Oliveira",
        cpf="123.456.789-00",
        cargo="Analista de Dados",
        salario=6000.00,
        data_admissao="2026-08-05"  # Formato aceito pelo Postgres
    )

    # 2. Instancia a DAO
    dao = FuncionarioDAO()

    # 3. Manda a DAO inserir o objeto no banco
    dao.inserir(novo_funcionario)

    # 4. Imprime o objeto (agora ele já deve ter o ID gerado pelo banco)
    print(novo_funcionario)

    # 5. Listar todos do banco para testar
    print("\n--- Lista de todos os funcionários no Banco ---")
    todos_funcionarios = dao.buscar_todos()
    for f in todos_funcionarios:
        print(f.nome, "-", f.cargo)

if __name__ == "__main__":
    main()