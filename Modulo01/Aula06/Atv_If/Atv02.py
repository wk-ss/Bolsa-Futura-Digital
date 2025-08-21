"""
Crie um arquivo Python (.py) e defina a constante NOTA_MINIMA 
com o valor 7.0. Em seguida, peça ao usuário que digite a sua 
nota final, armazenando-a na variável nota_final. Use uma estrutura 
condicional if para comparar a nota do aluno com a constante e exibir 
a mensagem "Aprovado!".

Obs: Utilize a função input() para solicitar a nota ao usuário e 
lembre-se de fazer a conversão do valor recebido para o tipo numérico 
(float), use a função print() para mostrar na tela a mensagem final e 
utilize a condicional IF para criar o primeiro fluxo do programa, comparando 
a nota_final com a NOTA_MINIMA."""
verificador = False
NOTA_MINIMA = 7.0
nota_usuario = float(input("Digite a sua nota: "))
if nota_usuario >= NOTA_MINIMA:
    verificador = True
print(f" voce foi aprovado? : {verificador} ,pois a sua nota foi {nota_usuario}")