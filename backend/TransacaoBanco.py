import psycopg2
from .Transacao import Transacao

class TransacaoBanco:
    def __init__(self):
        self.db_connection = psycopg2.connect(dbname='projeto-financas',
                                              user='postgres',
                                              password='1910',
                                              host='localhost',
                                              port=5432)
        self.db_cursor = self.db_connection.cursor()
        
        self.criar_tabela_transacao()

    def criar_tabela_transacao(self):
        cmd_sql = """
        CREATE TABLE IF NOT EXISTS transacao (
            id_transacao INT,  
            descricao VARCHAR(255) NOT NULL,
            valor DECIMAL(10, 2) NOT NULL,
            tipo VARCHAR(50),
            categoria_id INT,
            conta_id INT,
            CONSTRAINT pk_transacao PRIMARY KEY (id_transacao),
            CONSTRAINT fk_conta
            FOREIGN KEY (conta_id) REFERENCES conta(id_conta)
        );
        """
        self.db_cursor.execute(cmd_sql)
        self.db_connection.commit()

    def criar_transacao(self, transacao: Transacao):
        try:
            cmd_sql = """
            INSERT INTO transacao (id_transacao, descricao, valor, tipo, categoria_id, conta_id) 
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            self.db_cursor.execute(cmd_sql, (transacao.get_id_transacao(), transacao.get_descricao(), 
                                              transacao.get_valor(), transacao.get_tipo(), 
                                              transacao.get_categoria_id(), transacao.get_conta_id()))
            self.db_connection.commit()
            print("Transação inserida com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir transação: {e}")
            return None

    def pegar_transacao(self, id_transacao):
        try:
            cmd_sql = """SELECT id_transacao, descricao, valor, tipo, categoria_id, conta_id
                         FROM transacao WHERE id_transacao = %s;"""
            self.db_cursor.execute(cmd_sql, (id_transacao,))
            linha = self.db_cursor.fetchone()

            if linha:
                id_transacao, descricao, valor, tipo, categoria_id, conta_id = linha
                transacao = Transacao(id_transacao, descricao, valor, tipo, categoria_id, conta_id)
            else:
                transacao = None

            return transacao
        except Exception as e:
            print(f"Erro ao buscar transação: {e}")
            return None

    def atualizar_transacao(self, transacao: Transacao):
        try:
            cmd_sql = """
            UPDATE transacao
            SET descricao = %s, valor = %s, tipo = %s, categoria_id = %s, conta_id = %s
            WHERE id_transacao = %s;
            """
            self.db_cursor.execute(cmd_sql, (transacao.get_descricao(), transacao.get_valor(), 
                                              transacao.get_tipo(), transacao.get_categoria_id(), 
                                              transacao.get_conta_id(), transacao.get_id_transacao()))
            self.db_connection.commit()
            print("Transação atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar transação: {e}")
            return None

    def deletar_transacao(self, id_transacao):
        try:
            cmd_sql = "DELETE FROM transacao WHERE id_transacao = %s;"
            self.db_cursor.execute(cmd_sql, (id_transacao,))
            self.db_connection.commit()
            print("Transação deletada com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar transação: {e}")
            return None

    def close_connection(self):
        self.db_cursor.close()
        self.db_connection.close()
        print("Conexão com o banco de dados encerrada.")
