"""Crie um arquivo .py. Dentro do seu arquivo, construa um código que crie uma
variável precos que vai armazenar a seguinte lista dentro de si 85, 120, 50,
250, 99 e após isso crie uma variável chamada produtos_filtrados que vai
armazenar o resultado de uma operação com filter e uma lambda. A lambda
deve filtrar uma lista de preços, mantendo apenas aqueles que são maiores
que 100.
"""

precos = [85, 120, 50, 250, 99]

produtos_filtrados = list(filter(lambda x: x > 100, precos))

print("Preços filtrados (maiores que 100):", produtos_filtrados)
