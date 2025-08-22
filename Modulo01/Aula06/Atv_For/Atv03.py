"""
Crie um arquivo .py. Peça ao usuário para inserir 
um número inteiro. Em seguida, use um laço for para 
exibir a tabuada de multiplicação desse número, 
de 1 a 10."""

num = int(input("digite o numero: "))
for i in range(10):
    print(f"{num} x {i} = {(i*num)}")