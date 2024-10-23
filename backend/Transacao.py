class Transacao:
    def __init__(self, id_transacao, descricao, valor, tipo, categoria_id, conta_id):
        self.id_transacao = id_transacao
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria_id = categoria_id
        self.conta_id = conta_id  

    def set_id_transacao(self, id_transacao):
        self.id_transacao = id_transacao

    def get_id_transacao(self):
        return self.id_transacao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao

    def set_valor(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id

    def get_categoria_id(self):
        return self.categoria_id

    def set_conta_id(self, conta_id):
        self.conta_id = conta_id

    def get_conta_id(self):
        return self.conta_id