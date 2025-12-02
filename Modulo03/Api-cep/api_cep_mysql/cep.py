import requests
from teste_banco import *


cep = input("digite o seu cep:")

cep = cep.replace("-", "").replace(".", "").replace(" ", "")
link = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(link)
dados = requisicao.json()

for coluna, descricao in dados.items():
    print(f"{coluna}: {descricao}")

cep = dados["cep"]
logradouro = dados["logradouro"]
bairro = dados["bairro"]
localidade = dados["localidade"]
uf = dados["uf"]

criar_banco()

inserir_valor(cep,logradouro,bairro,localidade,uf)

ver_banco()
