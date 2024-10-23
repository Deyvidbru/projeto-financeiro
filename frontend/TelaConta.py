import customtkinter
from backend.ContaBanco import ContaBanco
from backend.Conta import Conta

class TelaConta:
    def __init__(self):
        self.conta_banco = ContaBanco()  

        self.janela_conta = customtkinter.CTk() 
        self.janela_conta.geometry("500x650")  
        self.janela_conta.title("Tela de Conta")  

        self.label_titulo = customtkinter.CTkLabel(self.janela_conta, text="Gerenciamento de Conta", font=("Arial", 24, "bold"))
        self.label_titulo.pack(padx=10, pady=20)

        self.label_conta_id = customtkinter.CTkLabel(self.janela_conta, text="ID Conta:")
        self.label_conta_id.pack(padx=10, pady=5)
        self.entry_conta_id = customtkinter.CTkEntry(self.janela_conta)
        self.entry_conta_id.pack(padx=10, pady=5)
        
        self.label_nome_conta = customtkinter.CTkLabel(self.janela_conta, text="Nome da Conta:")
        self.label_nome_conta.pack(padx=10, pady=5)
        self.entry_nome_conta = customtkinter.CTkEntry(self.janela_conta)
        self.entry_nome_conta.pack(padx=10, pady=5)

        self.label_saldo = customtkinter.CTkLabel(self.janela_conta, text="Saldo:")
        self.label_saldo.pack(padx=10, pady=5)
        self.entry_saldo = customtkinter.CTkEntry(self.janela_conta)
        self.entry_saldo.pack(padx=10, pady=5)

        self.frame_botoes = customtkinter.CTkFrame(self.janela_conta)
        self.frame_botoes.pack(padx=10, pady=20)

        self.botao_criar = customtkinter.CTkButton(self.frame_botoes, text="Criar Conta", command=self.criar_conta)
        self.botao_criar.grid(row=0, column=0, padx=10, pady=10)

        self.botao_buscar = customtkinter.CTkButton(self.frame_botoes, text="Buscar Conta", command=self.buscar_conta)
        self.botao_buscar.grid(row=0, column=1, padx=10, pady=10)

        self.botao_atualizar = customtkinter.CTkButton(self.frame_botoes, text="Atualizar Conta", command=self.atualizar_conta)
        self.botao_atualizar.grid(row=1, column=0, padx=10, pady=10)

        self.botao_deletar = customtkinter.CTkButton(self.frame_botoes, text="Deletar Conta", command=self.deletar_conta)
        self.botao_deletar.grid(row=1, column=1, padx=10, pady=10)

        self.resultado_label = customtkinter.CTkLabel(self.janela_conta, text="", font=("Arial", 12))
        self.resultado_label.pack(padx=10, pady=10)

        self.botao_voltar = customtkinter.CTkButton(self.janela_conta, text="Voltar", command=self.voltar)
        self.botao_voltar.pack(padx=10, pady=20)

        self.janela_conta.mainloop()  

    def criar_conta(self):
        try:
            id_conta = int(self.entry_conta_id.get())
            nome_conta = self.entry_nome_conta.get()
            saldo = float(self.entry_saldo.get())

            conta = Conta(id_conta, nome_conta, saldo)  
            self.conta_banco.criar_conta(conta)
            self.resultado_label.configure(text="Conta criada com sucesso!", text_color="green")
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")

    def buscar_conta(self):
        try:
            conta_id = int(self.entry_conta_id.get())  
            conta = self.conta_banco.pegar_conta(conta_id)

            if conta:
                self.resultado_label.configure(
                    text=f"Conta: {conta.id_conta}, Nome: {conta.nome_conta}, Saldo: {conta.saldo}",
                    text_color="blue"
                )
            else:
                self.resultado_label.configure(text="Conta não encontrada", text_color="red")
        
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")
        
    def atualizar_conta(self):
        try:
            conta_id = int(self.entry_conta_id.get())
            nome_conta = self.entry_nome_conta.get()
            saldo = float(self.entry_saldo.get())

            conta = Conta(conta_id, nome_conta, saldo)
            self.conta_banco.atualizar_conta(conta)

            self.resultado_label.configure(text="Conta atualizada com sucesso!", text_color="green")
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")

    def deletar_conta(self):
        try:
            conta_id = int(self.entry_conta_id.get())
            self.conta_banco.deletar_conta(conta_id)
            self.resultado_label.configure(text="Conta deletada com sucesso!", text_color="red")
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")
        
    def voltar(self):
        from frontend.TelaHome import TelaHome 
        self.janela_conta.destroy()  
        TelaHome()  
