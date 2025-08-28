"""Crie um arquivo .py. Dentro do seu arquivo, construa um código que crie uma
variável chamada nomes que vai armazenar a seguinte lista dentro de si
['João', 'Maria', 'Pedro']e crie uma variavel chamada sobrenomes que vai
armazenar a seguinte lista dentro de si ['Silva', 'Santos', 'Rocha'] e após isso
crie uma variável nomes_completos que armazene o resultado de uma
operação com map e uma lambda. A lambda deve combinar duas listas
(uma de nomes e outra de sobrenomes) em uma única lista de nomes
completos."""

nomes = ['João', 'Maria', 'Pedro']
sobrenomes = ['Silva', 'Santos', 'Rocha']

nomes_completos = list(map(lambda n, s: f"{n} {s}", nomes, sobrenomes))

print("Nomes completos:", nomes_completos)
