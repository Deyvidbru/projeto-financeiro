class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha = senha
    
    def set_username(self, username):
        self.username = username
        
    def get_username(self):
        return self.username
    
    def set_senha(self, senha):
        self.senha = senha
        
    def get_senha(self):
        return self.senha