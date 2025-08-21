"""
Utilize o arquivo Python (.py) criado no exercício 01 
de estrutura if e adicione uma estrutura condicional 
elif para comparar a idade do usuário com a constante e 
exibir a mensagem "O usuário é menor e tem 16 ou 17 anos".

Obs:  Use a função print() para mostrar na tela a mensagem 
final e utilize as condicionais elif e os operadores do python."""
verificador = False
IDADE_MINIMA = 18
idade_usuario = int(input("Digite a sua idade: "))
if idade_usuario >= IDADE_MINIMA:
    verificador = True
    print(f" vode é maior de idade : {verificador} ,pois vc tem {idade_usuario}")
elif idade_usuario == 16 or 17: 
    print(f" vode é menor de idade ,pois vc tem {idade_usuario}")
else:
    print(f" vode é menor de idade ,pois vc tem {idade_usuario}")