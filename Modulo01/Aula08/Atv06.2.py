"""Crie um arquivo .py. Dentro do seu arquivo, construa
um código que define uma função que receba um texto qualquer
como argumento. A função deve retornar a quantidade de vogais
(a, e, i, o, u) do valor informado e esse resultado deve ser
mostrado na tela.
"""


def ContadorVogais(palavra: str) -> int:
    vogais = "aeiou"
    contador = 0

    for letras in palavra:
        if letras in vogais:
            contador += 1
    return contador


print(ContadorVogais("casa"))
