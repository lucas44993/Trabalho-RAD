import sqlite3
import os

DB_FILE = "alunos.db"

def get_db_connection():
    """Cria uma conexão com o banco de dados"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn

def init_db():
    """Inicializa o banco de dados criando as tabelas necessárias"""
    if not os.path.exists(DB_FILE):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Criar tabela de usuários
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
        ''')
        
        # Criar tabela de alunos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL,
            curso TEXT NOT NULL
        )
        ''')
        
        conn.commit()
        conn.close()

# Funções para gerenciar usuários
def add_user(username, password):
    """Adiciona um novo usuário"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)',
                      (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def check_user(username, password):
    """Verifica as credenciais do usuário"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM usuarios WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result and result['password'] == password

# Funções para gerenciar alunos
def add_aluno(nome, cpf, email, endereco, curso):
    """Adiciona um novo aluno"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO alunos (nome, cpf, email, endereco, curso)
        VALUES (?, ?, ?, ?, ?)
        ''', (nome, cpf, email, endereco, curso))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_all_alunos():
    """Retorna todos os alunos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return [dict(aluno) for aluno in alunos]

def update_aluno(id, nome, cpf, email, endereco, curso):
    """Atualiza os dados de um aluno"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        UPDATE alunos
        SET nome = ?, cpf = ?, email = ?, endereco = ?, curso = ?
        WHERE id = ?
        ''', (nome, cpf, email, endereco, curso, id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_aluno(id):
    """Remove um aluno pelo ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_aluno_by_id(id):
    """Retorna um aluno pelo ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos WHERE id = ?', (id,))
    aluno = cursor.fetchone()
    conn.close()
    return dict(aluno) if aluno else None

# Inicializa o banco de dados ao importar o módulo
init_db() 