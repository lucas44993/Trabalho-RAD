import tkinter as tk
from tkinter import messagebox
from utils.database import get_all_alunos

def fechar_relatorio(relatorio):
    relatorio.destroy()

def gerar_relatorio():
    alunos = get_all_alunos()
    if not alunos:
        messagebox.showinfo("Relatório", "Nenhum aluno cadastrado.")
        return

    relatorio = tk.Toplevel()
    relatorio.title("Relatório de Alunos")
    relatorio.geometry("500x400")
    relatorio.configure(bg="#ffffff")

    # Botão Voltar no topo
    tk.Button(relatorio, text="← Voltar",
              command=lambda: fechar_relatorio(relatorio),
              bg="#666666", fg="white").pack(anchor="nw", padx=10, pady=5)

    texto = tk.Text(relatorio, wrap=tk.WORD, bg="#f7f7f7", font=("Segoe UI", 10))
    texto.pack(expand=True, fill='both', padx=10, pady=10)

    texto.insert(tk.END, "=== Lista de Alunos Cadastrados ===\n\n")
    for idx, aluno in enumerate(alunos, 1):
        texto.insert(tk.END, f"{idx}. Nome: {aluno['nome']}\n")
        texto.insert(tk.END, f"    CPF: {aluno['cpf']}\n")
        texto.insert(tk.END, f"    Email: {aluno['email']}\n")
        texto.insert(tk.END, f"    Endereço: {aluno['endereco']}\n")
        texto.insert(tk.END, f"    Curso: {aluno['curso']}\n\n")

    texto.config(state='disabled')  # Torna o conteúdo não editável
    messagebox.showinfo("Relatório", "Relatório gerado com sucesso!") 