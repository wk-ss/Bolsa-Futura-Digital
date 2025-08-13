"""
Crie um arquivo .py utilizando o vscode e construa um código e replique o código do programa abaixo, rode ele no seu vscode e verifique onde está o erro, ao encontrar o erro, conserto-o.
Obs: Lembre-se de como os textos são formatados utilizando f-strings.

Código:

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))

print("O produto f{nome_produto} custa R$ f{preco_produto}.")

Exemplo de saída esperada:
O produto Coca-Cola custa R$ 12.50.
"""
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))

print(f"O produto {nome_produto} custa R$ {preco_produto}.")