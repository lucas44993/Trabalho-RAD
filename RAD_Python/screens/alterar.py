import tkinter as tk
from tkinter import messagebox
from utils.database import get_all_alunos, update_aluno, get_aluno_by_id

def voltar_para_menu(janela_alterar, menu_janela):
    janela_alterar.destroy()
    menu_janela.deiconify()

def editar_aluno(lista_box_alterar, janela_alterar, menu_janela):
    sel = lista_box_alterar.curselection()
    if not sel:
        messagebox.showwarning("Erro", "Selecione um aluno.")
        return

    idx = sel[0]
    alunos = get_all_alunos()
    aluno = alunos[idx]

    for widget in janela_alterar.winfo_children():
        widget.destroy()

    # Botão Voltar no topo
    tk.Button(janela_alterar, text="← Voltar",
              command=lambda: voltar_para_menu(janela_alterar, menu_janela),
              bg="#666666", fg="white").pack(anchor="nw", padx=10, pady=5)

    campo_ed_nome = tk.Entry(janela_alterar, width=40)
    campo_ed_cpf = tk.Entry(janela_alterar, width=40)
    campo_ed_email = tk.Entry(janela_alterar, width=40)
    campo_ed_endereco = tk.Entry(janela_alterar, width=40)
    campo_ed_curso = tk.Entry(janela_alterar, width=40)

    def salvar_alteracao():
        novo = {
            "nome": campo_ed_nome.get(),
            "cpf": campo_ed_cpf.get(),
            "email": campo_ed_email.get(),
            "endereco": campo_ed_endereco.get(),
            "curso": campo_ed_curso.get()
        }
        if all(novo.values()):
            if update_aluno(aluno['id'], novo['nome'], novo['cpf'], 
                          novo['email'], novo['endereco'], novo['curso']):
                messagebox.showinfo("Sucesso", "Aluno alterado com sucesso!")
                voltar_para_menu(janela_alterar, menu_janela)
            else:
                messagebox.showwarning("Erro", "CPF já cadastrado para outro aluno.")
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")

    tk.Label(janela_alterar, text="Editar Nome:", bg="#ffffff").pack()
    campo_ed_nome.pack()
    campo_ed_nome.insert(0, aluno['nome'])

    tk.Label(janela_alterar, text="Editar CPF:", bg="#ffffff").pack()
    campo_ed_cpf.pack()
    campo_ed_cpf.insert(0, aluno['cpf'])

    tk.Label(janela_alterar, text="Editar Email:", bg="#ffffff").pack()
    campo_ed_email.pack()
    campo_ed_email.insert(0, aluno['email'])

    tk.Label(janela_alterar, text="Editar Endereço:", bg="#ffffff").pack()
    campo_ed_endereco.pack()
    campo_ed_endereco.insert(0, aluno['endereco'])

    tk.Label(janela_alterar, text="Editar Curso:", bg="#ffffff").pack()
    campo_ed_curso.pack()
    campo_ed_curso.insert(0, aluno['curso'])

    tk.Button(janela_alterar, text="Salvar", command=salvar_alteracao,
              bg="#006400", fg="white").pack(pady=10)

def abrir_tela_alterar(menu_janela):
    menu_janela.withdraw()

    janela_alterar = tk.Toplevel()
    janela_alterar.title("Alterar Aluno")
    janela_alterar.geometry("400x350")
    janela_alterar.configure(bg="#FFFFFF")

    # Botão Voltar no topo
    tk.Button(janela_alterar, text="← Voltar",
              command=lambda: voltar_para_menu(janela_alterar, menu_janela),
              bg="#666666", fg="white").pack(anchor="nw", padx=10, pady=5)

    tk.Label(janela_alterar, text="Selecione um aluno para alterar:", bg="#ffffff").pack(pady=10)
    lista_box_alterar = tk.Listbox(janela_alterar, width=50)
    lista_box_alterar.pack(padx=10, pady=10)

    alunos = get_all_alunos()
    for aluno in alunos:
        lista_box_alterar.insert(tk.END, f"{aluno['nome']} | {aluno['cpf']} | {aluno['curso']}")

    tk.Button(janela_alterar, text="Alterar Selecionado", 
              command=lambda: editar_aluno(lista_box_alterar, janela_alterar, menu_janela),
              bg="#006400", fg="white").pack(pady=5)

    janela_alterar.protocol("WM_DELETE_WINDOW", 
                          lambda: voltar_para_menu(janela_alterar, menu_janela)) 