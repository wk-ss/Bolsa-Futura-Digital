"""
Crie um arquivo .py. Use um laço for para iterar de 1 a 10.
Se o número atual for par e maior que 5, exiba uma mensagem
e interrompa o laço usando o break.
"""

for i in range(1, 10):
    print(i)
    if i % 2 == 0 and i > 5:
        print("loop acabou")
        break
