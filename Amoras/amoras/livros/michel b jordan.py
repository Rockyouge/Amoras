import sqlite3
banco = sqlite3.connect("julia.db")
cursor = banco.cursor()
cursor.execute(''' Create table if not exists amigos(nome text, endereco text, telefone text)''')
nome = input("digite seu nome")
endereco = input("digite o endereco")
fone = input("digite o telefone")
cursor.execute(f'''insert into amigo values('{nome}','{endereco}','{fone}')''')
banco.commit()