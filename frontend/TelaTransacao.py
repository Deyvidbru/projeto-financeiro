import customtkinter
from frontend.TelaHome import TelaHome
from backend.TransacaoBanco import TransacaoBanco
from backend.Transacao import Transacao

class TelaTransacao:
    def __init__(self):
        self.transacao_banco = TransacaoBanco()  

        self.janela_transacao = customtkinter.CTk()  
        self.janela_transacao.geometry("600x750")  
        
        self.janela_transacao.title("Tela de Transação") 
        
        self.label_titulo = customtkinter.CTkLabel(self.janela_transacao, text="Gerenciamento de Transação", font=("Arial", 24, "bold"))
        self.label_titulo.pack(padx=10, pady=20)

        self.label_transacao_id = customtkinter.CTkLabel(self.janela_transacao, text="ID Transação:")
        self.label_transacao_id.pack(padx=10, pady=5)
        self.entry_transacao_id = customtkinter.CTkEntry(self.janela_transacao)
        self.entry_transacao_id.pack(padx=10, pady=5)
        
        self.label_descricao = customtkinter.CTkLabel(self.janela_transacao, text="Descrição:")
        self.label_descricao.pack(padx=10, pady=5)
        self.entry_descricao = customtkinter.CTkEntry(self.janela_transacao)
        self.entry_descricao.pack(padx=10, pady=5)

        self.label_valor = customtkinter.CTkLabel(self.janela_transacao, text="Valor:")
        self.label_valor.pack(padx=10, pady=5)
        self.entry_valor = customtkinter.CTkEntry(self.janela_transacao)
        self.entry_valor.pack(padx=10, pady=5)

        self.label_tipo = customtkinter.CTkLabel(self.janela_transacao, text="Tipo:")
        self.label_tipo.pack(padx=10, pady=5)
        self.entry_tipo = customtkinter.CTkEntry(self.janela_transacao)
        self.entry_tipo.pack(padx=10, pady=5)
        
        self.label_categoria_id = customtkinter.CTkLabel(self.janela_transacao, text="ID Categoria:")
        self.label_categoria_id.pack(padx=10, pady=5)
        self.entry_categoria_id = customtkinter.CTkEntry(self.janela_transacao)
        self.entry_categoria_id.pack(padx=10, pady=5)

        self.label_conta_id = customtkinter.CTkLabel(self.janela_transacao, text="ID Conta:")
        self.label_conta_id.pack(padx=10, pady=5)
        self.entry_conta_id = customtkinter.CTkEntry(self.janela_transacao)
        self.entry_conta_id.pack(padx=10, pady=5)

        self.frame_botoes = customtkinter.CTkFrame(self.janela_transacao)
        self.frame_botoes.pack(padx=10, pady=20)

        self.botao_criar = customtkinter.CTkButton(self.frame_botoes, text="Criar Transação", command=self.criar_transacao)
        self.botao_criar.grid(row=0, column=0, padx=10, pady=10)

        self.botao_buscar = customtkinter.CTkButton(self.frame_botoes, text="Buscar Transação", command=self.buscar_transacao)
        self.botao_buscar.grid(row=0, column=1, padx=10, pady=10)

        self.botao_atualizar = customtkinter.CTkButton(self.frame_botoes, text="Atualizar Transação", command=self.atualizar_transacao)
        self.botao_atualizar.grid(row=1, column=0, padx=10, pady=10)

        self.botao_deletar = customtkinter.CTkButton(self.frame_botoes, text="Deletar Transação", command=self.deletar_transacao)
        self.botao_deletar.grid(row=1, column=1, padx=10, pady=10)

        self.resultado_label = customtkinter.CTkLabel(self.janela_transacao, text="", font=("Arial", 12))
        self.resultado_label.pack(padx=2, pady=2)
        
        self.botao_voltar = customtkinter.CTkButton(self.janela_transacao, text="Voltar", command=self.voltar)
        self.botao_voltar.pack(padx=10, pady=20)

        self.janela_transacao.mainloop()  

    def criar_transacao(self):
        try:
            id_transacao = int(self.entry_transacao_id.get())
            descricao = self.entry_descricao.get()
            valor = float(self.entry_valor.get())
            tipo = self.entry_tipo.get()
            categoria_id = int(self.entry_categoria_id.get())
            id_conta = int(self.entry_conta_id.get())
            
            transacao = Transacao(id_transacao, descricao, valor, tipo, categoria_id, id_conta)  
            self.transacao_banco.criar_transacao(transacao)
            self.resultado_label.configure(text="Transação criada com sucesso!", text_color="green")
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")

    def buscar_transacao(self):
        try:
            transacao_id = int(self.entry_transacao_id.get())
            transacao = self.transacao_banco.pegar_transacao(transacao_id)

            if transacao:
                self.resultado_label.configure(
                    text=f"Transação {transacao.id_transacao}, Descrição: {transacao.descricao}, Valor: {transacao.valor}, Tipo: {transacao.tipo}, ID Categoria: {transacao.categoria_id}, ID Conta: {transacao.conta_id}",
                    text_color="blue"
                )
            else:
                self.resultado_label.configure(text="Transação não encontrada", text_color="red")

        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")

    def atualizar_transacao(self):
        try:
            transacao_id = int(self.entry_transacao_id.get())
            descricao = self.entry_descricao.get()
            valor = float(self.entry_valor.get())
            tipo = self.entry_tipo.get()
            categoria_id = int(self.entry_categoria_id.get())
            id_conta = int(self.entry_conta_id.get())

            transacao = Transacao(transacao_id, descricao, valor, tipo, categoria_id, id_conta)
            self.transacao_banco.atualizar_transacao(transacao)
            self.resultado_label.configure(text="Transação atualizada com sucesso!", text_color="green")
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")

    def deletar_transacao(self):
        try:
            transacao_id = int(self.entry_transacao_id.get())
            self.transacao_banco.deletar_transacao(transacao_id)
            self.resultado_label.configure(text="Transação deletada com sucesso!", text_color="red")
        except Exception as e:
            self.resultado_label.configure(text=f"Erro: {e}", text_color="red")

    def voltar(self):
        self.janela_transacao.destroy()  
        TelaHome()  