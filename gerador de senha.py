import random
import string
import sqlite3
import hashlib

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))

senha = gerar_senha(tamanho_senha)

senha_hash = hashlib.sha256(senha.encode()).hexdigest()

conexao = sqlite3.connect('senhas.db')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS senhas (id INTEGER PRIMARY KEY AUTOINCREMENT, senha_hash TEXT)")
cursor.execute("INSERT INTO senhas (senha_hash) VALUES (?)", (senha_hash,))
conexao.commit()

print("Senha gerada:", senha)
