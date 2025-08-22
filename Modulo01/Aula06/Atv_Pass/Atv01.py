"""
Crie um arquivo .py. Use um laço for 
para iterar de 1 a 10. Se o número 
atual for par, use o continue para 
pular a impressão desse número e se 
o número atual for par e menor que 5, 
use o pass para preservar a lógica que 
ainda vai ser construída. Exiba apenas 
os números ímpares na tela."""


for numero in range(1, 11):
    if numero % 2 == 0: 
        if numero < 5:
            pass  
        continue  
    print(numero) 
