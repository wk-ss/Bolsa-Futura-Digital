'''Crie um arquivo .py . Escreva um código que vai conter uma variável que vai
armazenar alguma frase qualquer. Seu objetivo é contar o número de
palavras únicas na frase fornecida.
Obs: Você pode utilizar os conceitos de lista e conjunto para concluir esse
objetivo. Além disso, você pode utilizar a função split() para dividir uma
string em frases.
'''
frase = "Python é uma linguagem poderosa e Python é divertido"

palavras = frase.split()

palavras_unicas = set(palavras)

quantidade_unicas = len(palavras_unicas)

print("Frase:", frase)
print("Palavras únicas:", palavras_unicas)
print("Quantidade de palavras únicas:", quantidade_unicas)
