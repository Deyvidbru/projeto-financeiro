import psycopg2
from .Usuario import Usuario

class UsuarioBanco:
    def __init__(self):
        self.db_connection = psycopg2.connect(dbname='projeto-financas',
                                              user='postgres',
                                              password='1910',
                                              host='localhost',
                                              port=5432)
        self.db_cursor = self.db_connection.cursor()

        self.criar_tabela_usuario()

    def criar_tabela_usuario(self):
        try:
            cmd_sql = """
            CREATE TABLE IF NOT EXISTS usuario (
                username VARCHAR(100) NOT NULL,
                senha VARCHAR(100) NOT NULL
            );
            """
            self.db_cursor.execute(cmd_sql)
            self.db_connection.commit()
            print("Tabela 'usuario' criada ou já existe.")
        except Exception as e:
            print(f"Erro ao criar a tabela 'usuario': {e}")

    def insert_tabela_usuario(self, username, senha):
        try:
            self.db_cursor.execute("SELECT username FROM usuario WHERE username = %s;", (username,))
            resultado = self.db_cursor.fetchone()
            
            if resultado is None:
                cmd_sql = "INSERT INTO usuario (username, senha) VALUES (%s, %s);"
                self.db_cursor.execute(cmd_sql, (username, senha))
                self.db_connection.commit()
                print(f"Usuário '{username}' inserido com sucesso.")
            else:
                print(f"Usuário '{username}' já existe no banco de dados.")

        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")

    def get_usuario(self, username, senha):
        try:
            cmd_sql = """SELECT username, senha FROM usuario WHERE username = %s AND senha = %s;"""
            self.db_cursor.execute(cmd_sql, (username, senha))
            linhas_banco_dados = self.db_cursor.fetchone()
            
            if linhas_banco_dados:
                username_usuario, senha_usuario = linhas_banco_dados
                usuario = Usuario(username_usuario, senha_usuario)
            else:
                usuario = None

            return usuario

        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        
    def close_connection(self):
        self.db_cursor.close()
        self.db_connection.close()
        print("Conexão com o banco de dados encerrada.")