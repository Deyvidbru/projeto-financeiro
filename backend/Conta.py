class Conta:
    def __init__(self, id_conta, nome_conta, saldo):
        self.id_conta = id_conta
        self.nome_conta = nome_conta
        self.saldo = saldo  

    def get_id_conta(self):
        return self.id_conta
    
    def set_id_conta(self, id_conta):
        self.id_conta = id_conta

    def get_nome_conta(self):
        return self.nome_conta
    
    def set_nome_conta(self, nome_conta):
        self.nome_conta = nome_conta

    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self, saldo):
        self.saldo = saldo
