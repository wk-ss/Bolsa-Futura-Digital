"""Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados 'Ana', 'Pedro', 'Maria' em um conjunto chamado clientes ativos e
depois crie armazene os seguintes dados 'João', 'Maria', 'Lucas' em uma lista
chamada novos clientes. Você precisa adicionar os novos clientes ao
conjunto de clientes ativos, garantindo que não haja dados duplicados no
conjunto."""

clientes_ativos = {"Ana", "Pedro", "Maria"}

novos_clientes = ["João", "Maria", "Lucas"]

clientes_ativos.update(novos_clientes)

print("Clientes ativos atualizados:", clientes_ativos)
