"""
Crie um arquivo .py. Defina uma lista de números 
inteiros: numeros = [10, 20, 30, 40, 50]. Use um 
laço while para calcular a soma de todos os elementos 
dessa lista e exiba o resultado na tela.

Obs: Lembre-se de usar uma variável de controle (geralmente 
um índice) para"""
numeros = [10, 20, 30, 40, 50]
cont=0
soma=0
while (cont<len(numeros)):
       soma+=numeros[cont]
       cont+=1
print(soma)