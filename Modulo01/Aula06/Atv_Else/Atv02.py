"""
Utilize o arquivo Python (.py) modificado no exercício 02 de 
estrutura elif e adicione uma estrutura condicional else para 
comparar a nota do aluno com a constante e exibir a mensagem "Reprovado!".

Obs: Use a função print() para mostrar na tela a mensagem final 
e utilize as condicionais else e os operadores do python."""
NOTA_MINIMA = 7.0
nota_usuario = float(input("Digite a sua nota: "))
if nota_usuario >= NOTA_MINIMA:
    print(f" voce foi aprovado ,pois a sua nota foi {nota_usuario}")
else :
    print("Você não foi muito bem. Mas ainda consegue recuperar")