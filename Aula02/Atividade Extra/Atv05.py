""" Crie um arquivo .py utilizando o vscode e construa um código que peça para o usuário
 inserir o nome e gênero de um filme e armazene essa informação em duas variáveis de nomes
   nome_filme e gênero_filme e após isso mostre os valores que foram passados pelo usuário.
Obs:  mostre o valor utilizando uma única função print(), faça isso utilizando a F-STRING
 que é uma das formas de formatar um texto na linguagem python. Ex:

print(f“Texto qualquer { variável } ”)

Além disso, utilize a função input() para capturar as informações do usuário.

Exemplo da saída esperada:
filme: Homem-Aranha; gênero: Ação; 
"""
nome_filme = input("Digite o nome do filme : ")
gênero_filme = input("Digite o genero do filme : ")

print(f"Filme: {nome_filme}; genero: {gênero_filme}; ")
#filme: Homem-Aranha; gênero: Ação; python nome_do_arquivo.py > saida.txt
