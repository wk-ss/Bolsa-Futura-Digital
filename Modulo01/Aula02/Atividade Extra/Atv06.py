""" Crie um arquivo .py utilizando o vscode e construa um código que peça para 
o usuário inserir 4 palavras, que vão ser armazenadas em 4 variáveis diferentes
palavra 1, palavra 2, palavra 3 e palavra 4 e após isso mostre para o usuário 
uma frase construída com as palavras passadas pelo usuário.
Obs:  mostre o valor utilizando uma única função print(), use o formato abaixo 
para mostrar os valores para o usuário:

print(palavra 1,palavra 2, palavra 3,palavra 4)

Além disso, utilize as regras de nomenclatura dos identificadores de variáveis,
para nomear as variáveis.

Exemplo da saída esperada:
Choveu a noite inteira
"""
palavras = []
for i in range(4):
    palavra = input(f"Digite a palavra {i+1}: ")
    palavras.append(palavra)
for o in range(4):
    print (palavras[o], end=" ")


# ['choveu', 'a', 'noite', 'inteira']
#choveu a noite inteira 