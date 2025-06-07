import re

def validar_cpf(cpf):
    """Valida um CPF"""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if len(cpf) != 11 or cpf == cpf[0] * 11:  # Checa se o CPF tem 11 números e não é um CPF inválido
        return False
    
    # Verificação do primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False
    
    # Verificação do segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        return False
    
    return True

def validar_email(email):
    """Valida um endereço de e-mail"""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None 

def validar_username(username):
    """Valida o nome de usuário"""
    # Verifica se tem pelo menos 3 caracteres
    if len(username) < 3:
        return False, "O usuário deve ter pelo menos 3 caracteres."
    
    # Verifica se não é composto apenas por números
    if username.isdigit():
        return False, "O usuário não pode conter apenas números."
    
    # Verifica se contém apenas caracteres alfanuméricos
    if not username.isalnum():
        return False, "O usuário deve conter apenas letras e números."
    
    return True, ""

def validar_senha(senha):
    """Valida a senha do usuário"""
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."
    
    # Verifica se tem pelo menos uma letra maiúscula
    if not any(c.isupper() for c in senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."
    
    # Verifica se tem pelo menos uma letra minúscula
    if not any(c.islower() for c in senha):
        return False, "A senha deve conter pelo menos uma letra minúscula."
    
    # Verifica se tem pelo menos um número
    if not any(c.isdigit() for c in senha):
        return False, "A senha deve conter pelo menos um número."
    
    # Verifica se tem pelo menos um caractere especial
    especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in especiais for c in senha):
        return False, "A senha deve conter pelo menos um caractere especial (!@#$%^&*()_+-=[]{}|;:,.<>?)"
    
    return True, "" 