import tkinter as tk
from tkinter import messagebox
from utils.data import validar_cpf, validar_email
from utils.database import add_aluno

def voltar_para_menu(janela_adicionar, menu_janela):
    janela_adicionar.destroy()
    menu_janela.deiconify()

def concluir_adicao(campos, janela_adicionar, menu_janela):
    nome = campos['nome'].get()
    cpf = campos['cpf'].get()
    email = campos['email'].get()
    endereco = campos['endereco'].get()
    curso = campos['curso'].get()

    if nome and cpf and email and endereco and curso:
        if not validar_cpf(cpf):
            messagebox.showwarning("Erro", "CPF inválido.")
            return
        if not validar_email(email):
            messagebox.showwarning("Erro", "E-mail inválido.")
            return
        
        if add_aluno(nome, cpf, email, endereco, curso):
            messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
            voltar_para_menu(janela_adicionar, menu_janela)
        else:
            messagebox.showwarning("Erro", "CPF já cadastrado.")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")

def abrir_tela_adicionar(menu_janela):
    menu_janela.withdraw()

    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Aluno")
    janela_adicionar.geometry("400x400")
    janela_adicionar.configure(bg="#FFFFFF")

    # Botão Voltar no topo
    tk.Button(janela_adicionar, text="← Voltar",
              command=lambda: voltar_para_menu(janela_adicionar, menu_janela),
              bg="#666666", fg="white").pack(anchor="nw", padx=10, pady=5)

    fonte = ("Segoe UI", 10)
    campos = {}

    tk.Label(janela_adicionar, text="Nome:", bg="#ffffff", font=fonte).pack(pady=5)
    campos['nome'] = tk.Entry(janela_adicionar, width=40)
    campos['nome'].pack()

    tk.Label(janela_adicionar, text="CPF:", bg="#ffffff", font=fonte).pack(pady=5)
    campos['cpf'] = tk.Entry(janela_adicionar, width=40)
    campos['cpf'].pack()

    tk.Label(janela_adicionar, text="Email:", bg="#ffffff", font=fonte).pack(pady=5)
    campos['email'] = tk.Entry(janela_adicionar, width=40)
    campos['email'].pack()

    tk.Label(janela_adicionar, text="Endereço:", bg="#ffffff", font=fonte).pack(pady=5)
    campos['endereco'] = tk.Entry(janela_adicionar, width=40)
    campos['endereco'].pack()

    tk.Label(janela_adicionar, text="Curso:", bg="#ffffff", font=fonte).pack(pady=5)
    campos['curso'] = tk.Entry(janela_adicionar, width=40)
    campos['curso'].pack()

    tk.Button(janela_adicionar, text="Concluir", 
              command=lambda: concluir_adicao(campos, janela_adicionar, menu_janela),
              bg="#006400", fg="white", width=20).pack(pady=20)

    janela_adicionar.protocol("WM_DELETE_WINDOW", 
                            lambda: voltar_para_menu(janela_adicionar, menu_janela)) 