import mysql.connector


conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345678",
    database = "cep"
)
cursor = conexao.cursor()
print("ta funcionando")
cursor.execute("describe endereco")
cursor.fetchall()

cursor.close()
conexao.close()
