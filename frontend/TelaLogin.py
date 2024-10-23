import customtkinter
from frontend.TelaHome import TelaHome

from backend.UsuarioBanco import UsuarioBanco

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class TelaLogin:
    def __init__(self):
        self.janela = None
        self.janela_cadastro = None

    def clique(self, username, senha, mensagem_label):
        gerenciador_usuario = UsuarioBanco()

        if username and senha:
            usuario = gerenciador_usuario.get_usuario(username, senha)
            if usuario is not None:
                mensagem_label.configure(text="Login realizado com sucesso!", text_color="green")
                self.janela.destroy()
                TelaHome()
            else:
                mensagem_label.configure(text="Usuário ou senha incorretos", text_color="red")
        else:
            mensagem_label.configure(text="Por favor, insira o username e a senha.", text_color="orange")

        gerenciador_usuario.close_connection()

    def cadastrar(self, username, senha, mensagem_label):
        gerenciador_usuario = UsuarioBanco()

        if username and senha:
            gerenciador_usuario.insert_tabela_usuario(username, senha)
            mensagem_label.configure(text="Cadastro realizado com sucesso!", text_color="green")
        else:
            mensagem_label.configure(text="Por favor, insira o username e a senha.", text_color="orange")

        gerenciador_usuario.close_connection()

    def run_login(self):
        self.janela = customtkinter.CTk()
        self.janela.geometry("500x400")

        label_titulo = customtkinter.CTkLabel(self.janela, text="Login", font=("Arial", 24, "bold"))
        label_titulo.pack(padx=10, pady=20)

        username_entry = customtkinter.CTkEntry(self.janela, placeholder_text="Seu username")
        username_entry.pack(padx=10, pady=10)

        senha_entry = customtkinter.CTkEntry(self.janela, placeholder_text="Sua senha", show="*")
        senha_entry.pack(padx=10, pady=10)

        mensagem_label = customtkinter.CTkLabel(self.janela, text="")
        mensagem_label.pack(padx=10, pady=10)

        botao_login = customtkinter.CTkButton(self.janela, text="Login", command=lambda: self.clique(username_entry.get(), senha_entry.get(), mensagem_label))
        botao_login.pack(padx=10, pady=10)

        botao_cadastro = customtkinter.CTkButton(self.janela, text="Cadastrar", command=self.run_cadastro)
        botao_cadastro.pack(padx=10, pady=10)

        self.janela.mainloop()

    def run_cadastro(self):
        self.janela_cadastro = customtkinter.CTk()
        self.janela_cadastro.geometry("500x400")

        label_titulo = customtkinter.CTkLabel(self.janela_cadastro, text="Cadastro", font=("Arial", 24, "bold"))
        label_titulo.pack(padx=10, pady=20)

        username_cadastro_entry = customtkinter.CTkEntry(self.janela_cadastro, placeholder_text="Novo username")
        username_cadastro_entry.pack(padx=10, pady=10)

        senha_cadastro_entry = customtkinter.CTkEntry(self.janela_cadastro, placeholder_text="Nova senha", show="*")
        senha_cadastro_entry.pack(padx=10, pady=10)

        mensagem_label = customtkinter.CTkLabel(self.janela_cadastro, text="")
        mensagem_label.pack(padx=10, pady=10)

        botao_cadastrar = customtkinter.CTkButton(self.janela_cadastro, text="Cadastrar", command=lambda: self.cadastrar(username_cadastro_entry.get(), senha_cadastro_entry.get(), mensagem_label))
        botao_cadastrar.pack(padx=10, pady=10)

        botao_voltar = customtkinter.CTkButton(self.janela_cadastro, text="Voltar", command=self.janela_cadastro.destroy)
        botao_voltar.pack(padx=10, pady=10)

        self.janela_cadastro.mainloop()