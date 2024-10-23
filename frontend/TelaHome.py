import customtkinter

class TelaHome:
    def __init__(self):
        self.janela_home = customtkinter.CTk() 
        self.janela_home.geometry("500x300")
        
        label_titulo = customtkinter.CTkLabel(self.janela_home, text="Tela de Interação", font=("Arial", 24, "bold"))
        label_titulo.pack(padx=10, pady=20)

        transacao_botao = customtkinter.CTkButton(self.janela_home, text="Interação de Transação", command=self.abrir_tela_transacao)
        transacao_botao.pack(padx=10, pady=10)

        conta_botao = customtkinter.CTkButton(self.janela_home, text="Interação de Conta", command=self.abrir_tela_conta)
        conta_botao.pack(padx=10, pady=10)
        
        fechamento_botao = customtkinter.CTkButton(self.janela_home, text="Fechar Projeto", command=self.fechamento_projeto)
        fechamento_botao.pack(padx=10, pady=10)
        
        self.janela_home.mainloop()  

    def abrir_tela_transacao(self):
        self.janela_home.destroy()  
        from frontend.TelaTransacao import TelaTransacao  
        TelaTransacao() 

    def abrir_tela_conta(self):
        self.janela_home.destroy()  
        from frontend.TelaConta import TelaConta 
        TelaConta()  
        
    def fechamento_projeto(self):
        self.janela_home.destroy()