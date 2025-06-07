import tkinter as tk
from tkinter import messagebox
from utils.database import check_user, add_user
from utils.data import validar_username, validar_senha
from screens.menu import criar_menu

class LoginScreen:
    def __init__(self):
        self.login_janela = tk.Tk()
        self.login_janela.title("Login do Sistema")
        self.login_janela.geometry("300x200")
        self.login_janela.configure(bg="#ffffff")
        
        self.criar_widgets()
        
    def criar_widgets(self):
        tk.Label(self.login_janela, text="Usuário:", bg="#ffffff").pack(pady=5)
        self.entrada_usuario = tk.Entry(self.login_janela)
        self.entrada_usuario.pack()

        tk.Label(self.login_janela, text="Senha:", bg="#ffffff").pack(pady=5)
        self.entrada_senha = tk.Entry(self.login_janela, show="*")
        self.entrada_senha.pack()

        tk.Button(self.login_janela, text="Login", command=self.fazer_login, 
                 bg="#006400", fg="white").pack(pady=5)
        tk.Button(self.login_janela, text="Registrar", command=self.fazer_registro, 
                 bg="#888", fg="white").pack()

    def fazer_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        if check_user(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.login_janela.destroy()
            criar_menu()
        else:
            messagebox.showwarning("Erro", "Usuário ou senha incorretos!")

    def fazer_registro(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        
        if not usuario or not senha:
            messagebox.showwarning("Atenção", "Preencha usuário e senha.")
            return
            
        # Validar username
        username_valido, msg_username = validar_username(usuario)
        if not username_valido:
            messagebox.showwarning("Erro", msg_username)
            return
            
        # Validar senha
        senha_valida, msg_senha = validar_senha(senha)
        if not senha_valida:
            messagebox.showwarning("Erro", msg_senha)
            return
            
        if add_user(usuario, senha):
            messagebox.showinfo("Registrado", "Usuário registrado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Usuário já existe!")

    def iniciar(self):
        self.login_janela.mainloop() 