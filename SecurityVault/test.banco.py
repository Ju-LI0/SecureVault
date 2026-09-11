import sqlite3


conexao = sqlite3.connect("data/securevault.db")

registros = conexao.execute("""
    SELECT servico, usuario, senha
    FROM credenciais
""").fetchall()

for registro in registros:
    print("Serviço:", registro[0])
    print("Usuário:", registro[1])
    print("Senha armazenada:", registro[2])
    print("-" * 40)

conexao.close()