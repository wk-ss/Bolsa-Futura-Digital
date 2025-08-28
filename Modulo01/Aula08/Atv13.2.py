"""Crie um arquivo .py. Dentro do seu arquivo, construa um código que crie uma
variável chamada usuarios que vai armazenar a seguinte lista dentro de si
[{'nome': 'Carlos', 'idade': 30}, {'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno',
'idade': 40}] e após isso crie uma variável usuarios_ordenados que armazena
o resultado de uma operação com sorted e uma lambda. A lambda deve
ordenar uma lista usuarios (com chaves 'nome' e 'idade') em ordem
alfabética pelo nome."""

usuarios = [
    {"nome": "Carlos", "idade": 30},
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 40},
]
usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario["nome"])

print("Usuários ordenados por nome:")
for usuario in usuarios_ordenados:
    print(usuario)
