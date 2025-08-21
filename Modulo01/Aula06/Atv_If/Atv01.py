"""
Crie um arquivo Python (.py) e defina a constante IDADE_MINIMA
com o valor 18. Em seguida, peça ao usuário que digite sua idade,
armazenando-a na variável idade_usuario. Por fim, use uma estrutura
condicional if  para comparar a idade do usuário com a constante e exibir
a mensagem "O usuário é maior de idade.

Obs: Utilize a função input() para solicitar a idade ao usuário e lembre-se
de fazer a conversão do valor recebido para o tipo int(), use a função print()
para mostrar na tela a mensagem final e utilize as condicionais IF e os operadores
do python.
"""

verificador = False
IDADE_MINIMA = 18
idade_usuario = int(input("Digite a sua idade: "))
if idade_usuario >= IDADE_MINIMA:
    verificador = True
print(f" vode é maior de idade : {verificador} ,pois vc tem {idade_usuario}")
