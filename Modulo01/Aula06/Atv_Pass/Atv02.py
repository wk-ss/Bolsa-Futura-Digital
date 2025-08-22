"""
Crie um arquivo .py. Defina uma lista
de números: numeros = [10, -5, 20, 0, -1, 30].
 Use um laço for para percorrer a lista. Se o
 número for zero ou negativo, use continue para
 pular o processamento e ir para o próximo e se
 o número for par, use o pass para preservar a
 lógica que ainda vai ser construída. Calcule a
 soma apenas dos números positivos."""

numeros = [10, -5, 20, 0, -1, 30]

soma = 0

for numero in numeros:
    if numero <= 0:
        continue

    if numero % 2 == 0:
        pass

    soma += numero

print("Soma dos números positivos:", soma)
