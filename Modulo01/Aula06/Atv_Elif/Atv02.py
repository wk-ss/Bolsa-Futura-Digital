"""
Utilize o arquivo Python (.py) criado no exercício 02 
de estrutura if e adicione uma estrutura condicional 
elif para comparar a nota do aluno com a constante e 
exibir a mensagem "Você não foi muito bem. Mas ainda 
consegue recuperar".

Obs: Use a função print() para mostrar na tela a mensagem 
final e utilize as condicionais elif e os operadores do python."""

NOTA_MINIMA = 7.0
nota_usuario = float(input("Digite a sua nota: "))
if nota_usuario >= NOTA_MINIMA:
    print(f" voce foi aprovado ,pois a sua nota foi {nota_usuario}")
else :
    print("Você não foi muito bem. Mas ainda consegue recuperar")