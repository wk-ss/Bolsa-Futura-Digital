"""Crie um arquivo .py. Dentro do seu arquivo,
construa um código que define uma função que
receba um texto qualquer como argumento. A
função deve retornar o valor informado porém
com a ordem inversa e esse valor deve ser
mostrado na tela."""


def inversao(palavra: str) -> str:
    palavra = palavra
    new_palavra = palavra[::-1]
    return new_palavra


print(inversao("casa"))
