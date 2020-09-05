import sqlite3

conn = sqlite3.connect("estudo.db")

cursor = conn.cursor()

p1 = input('Nome:\n')

cursor.execute("""
SELECT * FROM TMP;""")
for linha in cursor.fetchall():
        print(linha)
cursor.execute("""
INSERT INTO TMP (nome) 
values ('cleber');""")
for linha in cursor.fetchall():
        print(linha)
# cursor.execute("""
# INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
# VALUES (?,?,?,?,?,?,?,?)
# """, (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))

conn.commit()
print('Dados Aplicado')

conn.close()

