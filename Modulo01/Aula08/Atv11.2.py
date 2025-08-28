"""Crie um arquivo .py. Escreva um código que vai armazenar a sequência
'João', 'Maria', 'Pedro', 'Ana' em uma lista chamada vendedores. Você precisa
imprimir a posição e o valor de cada elemento da lista, faça isso utilizando o
enumerate(), comece a contagem do número 1.
"""

vendedores = ["João", "Maria", "Pedro", "Ana"]


for posicao, nome in enumerate(vendedores, start=1):
    print(f"Posição {posicao}: {nome}")
