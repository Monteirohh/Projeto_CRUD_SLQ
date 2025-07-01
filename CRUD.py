import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lokinho130970*',
    database='dados',
)

cursor = conexao.cursor()


#CRUD

#CREATE
#nome_produtos = "Arroz"
#valor = 12
#comando = f'INSERT INTO vendas (nome_produtos, valor) VALUES ("{nome_produtos}", "{valor}" )'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall() #ler o banco de dados
#print(resultado)


#UPDATE
# nome_produtos = "todynho"
#valor = 6 
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produtos = "{nome_produtos}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#DELETE 
nome_produtos = "arroz"
comando = f'DELETE FROM vendas WHERE nome_produtos = "{nome_produtos}"'
cursor.execute(comando)
conexao.commit() #edita o banco de dados



cursor.close()
conexao.close()