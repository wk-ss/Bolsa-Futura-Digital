""" 
Crie um arquivo .py utilizando o vscode e Replique o código do programa abaixo, rode
ele no seu vscode e verifique onde está o erro, ao encontrar o erro, conserto-o.
Obs: Lembre-se das regras de nomenclatura dos nomes das variáveis e de como é utilizada a função input().

Código:

import datetime

hora atual = datetime.datetime.now()
!nome_usuario. = input(Digite o seu nome: )

print(f'Olá, {!nome_usuario.}! Agora são {hora atual.strftime("%H:%M")} horas.')

Exemplo de saída esperada:
Olá, Bruno! Agora são 10:00 horas.
"""
import datetime

hora_atual = datetime.datetime.now()
nome_usuario = input("Digite o seu nome: ")

print(f'Olá, {nome_usuario}! Agora são {hora_atual.strftime("%H:%M")} horas.')