"""Crie um arquivo .py. Dentro do seu arquivo, construa um código
que define uma função calcular_media que aceite qualquer quantidade
de notas (*args) e retorne a média delas.
Exemplo de uso: calcular_media(8.5, 9.0, 7.5) deve retornar 8.33."""


def calcular_media(*num: float) -> float:
    soma_total = sum(num) / len(num)
    return soma_total


print(f"{calcular_media(8.5, 9.0, 7.5):.2f}")
