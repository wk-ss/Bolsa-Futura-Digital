"""
Crie um arquivo .py. Defina uma lista de
números: numeros = [10, -5, 20, 0, -1, 30].
Use um laço for para percorrer a lista. Se o
número for zero ou negativo, use continue para
pular o processamento e ir para o próximo. Calcule
a soma apenas dos números positivos."""

numeros = [10, -5, 20, 0, -1, 30]

soma = 0

for numero in numeros:
    if numero <= 0:
        continue
    soma += numero

print("Soma dos números positivos:", soma)
