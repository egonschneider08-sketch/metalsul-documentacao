from database.conexao import Conexao

def main():
    conexao = Conexao()
    print("Conexão realizada com sucesso")

    conexao.fechar()

if __name__ == "__main__":
    main()