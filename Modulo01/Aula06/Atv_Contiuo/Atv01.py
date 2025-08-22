"""
Crie um arquivo .py. Use um laço for para
iterar de 1 a 10. Se o número atual for par,
use o continue para pular a impressão desse
número. Exiba apenas os números ímpares na
tela."""

for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(numero)
