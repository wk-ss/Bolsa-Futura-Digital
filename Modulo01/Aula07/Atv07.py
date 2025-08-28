"""Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados de produto Crie 'nome': 'Mouse Gamer', 'preço': 150.00, 'estoque': 50 em
um dicionário chamado de catalogo. Agora você deve adicionar um novo
produto dentro do dicionário catalogo, esse produto contém os seguintes
dados 'nome': 'Teclado Mecânico', 'preço': 450.00, 'estoque': 30. Após isso,
mostre os todos os valores e chaves do dicionário."""

catalogo = {"produto1": {"nome": "Mouse Gamer", "preço": 150.00, "estoque": 50}}
catalogo["produto2"] = {"nome": "Teclado Mecânico", "preço": 450.00, "estoque": 30}
print("Catálogo completo:\n")
for chave, valor in catalogo.items():
    print(chave, ":", valor)
