"""
Utilize o arquivo Python (.py) modificado 
no exercício 01 de estrutura elif e adicione 
uma estrutura condicional else para exibir a 
mensagem "O usuário é menor de idade".

Obs:  Use a função print() para mostrar na tela 
a mensagem final e utilize as condicionais else e 
os operadores do python."""

IDADE_MINIMA = 18
idade_usuario = int(input("Digite a sua idade: "))
if idade_usuario >= IDADE_MINIMA:
    print(f" vode é maior de idade ,pois vc tem {idade_usuario}")
else:
    print("O usuário é menor de idade")