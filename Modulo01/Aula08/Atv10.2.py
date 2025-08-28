'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que crie uma
variável e_par que armazene/receber uma função lambda. Esta função
lambda deve verificar se um número qualquer é par e retornar True se o
número for par, e False se for ímpar.
Exemplo de uso: e_par(4) deve retornar True'''

eh_par = lambda x: x % 2 == 0

print(eh_par(4))
print(eh_par(7))  
