import psycopg2
from .Conta import Conta

class ContaBanco:
    def __init__(self):
        self.db_connection = psycopg2.connect(dbname='projeto-financas',
                                              user='postgres',
                                              password='1910',
                                              host='localhost',
                                              port=5432)
        self.db_cursor = self.db_connection.cursor()
        
        self.criar_tabela_conta()

    def criar_tabela_conta(self):
        cmd_sql = """
        CREATE TABLE IF NOT EXISTS conta (
            id_conta INT,  
            nome_conta VARCHAR(255) NOT NULL,
            saldo DECIMAL(10, 2) NOT NULL,
            CONSTRAINT pk_conta PRIMARY KEY (id_conta)
        );
        """
        self.db_cursor.execute(cmd_sql)
        self.db_connection.commit()

    def criar_conta(self, conta: Conta):
        try:
            cmd_sql = """
            INSERT INTO conta (id_conta, nome_conta, saldo)
            VALUES (%s, %s, %s);
            """
            self.db_cursor.execute(cmd_sql, (conta.get_id_conta(), conta.get_nome_conta(), conta.get_saldo()))
            self.db_connection.commit()
            
            print(f"Conta criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar conta: {e}")
            return None

    def pegar_conta(self, id_conta):
        try:
            cmd_sql = """SELECT id_conta, nome_conta, saldo 
                         FROM conta WHERE id_conta = %s;"""
            self.db_cursor.execute(cmd_sql, (id_conta,))
            linha = self.db_cursor.fetchone()

            if linha:
                id_conta, nome_conta, saldo = linha
                conta = Conta(id_conta, nome_conta, saldo)
            else:
                conta = None

            return conta
        except Exception as e:
            print(f"Erro ao buscar conta: {e}")
            return None

    def atualizar_conta(self, conta: Conta):
        try:
            cmd_sql = """
            UPDATE conta
            SET nome_conta = %s, saldo = %s
            WHERE id_conta = %s;
            """
            self.db_cursor.execute(cmd_sql, (conta.get_nome_conta(), conta.get_saldo(), conta.get_id_conta()))
            self.db_connection.commit()
            print("Conta atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar conta: {e}")
            return None

    def deletar_conta(self, id_conta):
        try:
            cmd_sql = "DELETE FROM conta WHERE id_conta = %s;"
            self.db_cursor.execute(cmd_sql, (id_conta,))
            self.db_connection.commit()
            print("Conta deletada com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar conta: {e}")
            return None

    def close_connection(self):
        self.db_cursor.close()
        self.db_connection.close()
        print("Conexão com o banco de dados encerrada.")
