import tkinter as tk
from tkinter import messagebox
from utils.database import get_all_alunos, delete_aluno

def voltar_para_menu(janela_remover, menu_janela):
    janela_remover.destroy()
    menu_janela.deiconify()

def remover_aluno(lista_box_remover, janela_remover, menu_janela):
    sel = lista_box_remover.curselection()
    if not sel:
        messagebox.showwarning("Erro", "Selecione um aluno.")
        return

    idx = sel[0]
    alunos = get_all_alunos()
    aluno = alunos[idx]
    
    # Adiciona diálogo de confirmação
    confirmacao = messagebox.askyesno(
        "Confirmar Remoção",
        f"Tem certeza que deseja remover o aluno '{aluno['nome']}'?"
    )
    
    if confirmacao:
        delete_aluno(aluno['id'])
        messagebox.showinfo("Removido", f"Aluno '{aluno['nome']}' removido.")
        voltar_para_menu(janela_remover, menu_janela)

def abrir_tela_remover(menu_janela):
    menu_janela.withdraw()

    janela_remover = tk.Toplevel()
    janela_remover.title("Remover Aluno")
    janela_remover.geometry("400x350")
    janela_remover.configure(bg="#FFFFFF")

    # Botão Voltar no topo
    tk.Button(janela_remover, text="← Voltar",
              command=lambda: voltar_para_menu(janela_remover, menu_janela),
              bg="#666666", fg="white").pack(anchor="nw", padx=10, pady=5)

    tk.Label(janela_remover, text="Selecione um aluno para remover:", bg="#ffffff").pack(pady=10)
    lista_box_remover = tk.Listbox(janela_remover, width=50)
    lista_box_remover.pack(padx=10, pady=10)

    alunos = get_all_alunos()
    for aluno in alunos:
        lista_box_remover.insert(tk.END, f"{aluno['nome']} | {aluno['cpf']} | {aluno['curso']}")

    tk.Button(janela_remover, text="Remover Selecionado", 
              command=lambda: remover_aluno(lista_box_remover, janela_remover, menu_janela),
              bg="#b22222", fg="white").pack(pady=5)

    janela_remover.protocol("WM_DELETE_WINDOW", 
                          lambda: voltar_para_menu(janela_remover, menu_janela)) 