import tkinter as tk
from screens.adicionar import abrir_tela_adicionar
from screens.alterar import abrir_tela_alterar
from screens.remover import abrir_tela_remover
from screens.relatorio import gerar_relatorio

menu_janela = None

def criar_menu():
    global menu_janela
    menu_janela = tk.Tk()
    menu_janela.title("Menu Principal")
    menu_janela.geometry("300x350")
    menu_janela.configure(bg="#ffffff")

    fonte = ("Segoe UI", 11)
    tk.Label(menu_janela, text="Escolha uma opção:", bg="#ffffff", font=fonte).pack(pady=20)

    tk.Button(menu_janela, text="Adicionar Aluno", command=lambda: abrir_tela_adicionar(menu_janela),
              bg="#006400", fg="white", width=25).pack(pady=5)
    tk.Button(menu_janela, text="Alterar Aluno", command=lambda: abrir_tela_alterar(menu_janela),
              bg="#006400", fg="white", width=25).pack(pady=5)
    tk.Button(menu_janela, text="Remover Aluno", command=lambda: abrir_tela_remover(menu_janela),
              bg="#006400", fg="white", width=25).pack(pady=5)
    tk.Button(menu_janela, text="Gerar Relatório", command=gerar_relatorio,
              bg="#34a853", fg="white", width=25).pack(pady=5)

    menu_janela.mainloop() 