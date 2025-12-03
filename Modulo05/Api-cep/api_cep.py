import requests
import mysql.connector


conexao = mysql.connector.connect(
    host="localhost", user="root", password="12345678", database="cep"
)
if conexao.is_connected():
    print("Finalmente conectou")
cursor = conexao.cursor()

cep = input("digite o seu cep:")

cep = cep.replace("-", "").replace(".", "").replace(" ", "")
link = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(link)
dados = requisicao.json()

"""for coluna,descricao in dados.items():
    print(f"{coluna}: {descricao}")

    OU

print(f"CEP: {dados['cep']}")
print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Localidade: {dados['localidade']}")
print(f"UF: {dados['uf']}")
"""

sql = """
INSERT INTO endereco (cep, logradouro, bairro, localidade, uf)
VALUES (%s, %s, %s, %s, %s)
"""
valores = (
    dados["cep"],
    dados["logradouro"],
    dados["bairro"],
    dados["localidade"],
    dados["uf"],
)

cursor.execute(sql, valores)
conexao.commit()


cursor.execute("SELECT * FROM endereco")
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

cursor.close()
conexao.close()
