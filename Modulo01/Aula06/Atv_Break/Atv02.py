"""
Crie um arquivo .py. Defina uma lista de nomes: 
nomes = ["Ana", "Pedro", "João", "Maria", "Carlos"]. 
Peça ao usuário para inserir um nome. Use um laço for 
para procurar o nome na lista. Se o nome for encontrado, 
exiba a mensagem "Nome encontrado!" e pare a busca 
imediatamente usando o break. Se o laço terminar sem 
encontrar o nome, exiba "Nome não encontrado."."""

nomes = ["Ana", "Pedro", "João", "Maria", "Carlos"]
key=input("digite o nome: ")
for i in nomes:
    if i == key:
        print("Nome encontrado!")
        break
else:
    
    print("Nome não encontrado.")