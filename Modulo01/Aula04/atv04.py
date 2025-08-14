"""Crie um arquivo .py, crie um programa que vai conter
variável idade_usuario que vai receber um valor que vai
ser passado para o usuário é uma constante IDADE_MINIMA
com o valor 18. Use os operadores "maior ou igual a" [ >= ]
e  "menor" [ < ] para verificar se o usuário é maior de idade
e exiba o resultado na tela seguindo a seguinte estrutura "O
usuário é maior de idade? resultado" e "O usuário é menor de idade".

Obs: Utilize os operadores de maior ou igual [ >= ] e menor que
[ < ], print() para mostrar o texto na tela e input() para receber
os dados do usuário."""

IDADE_MINIMA = 18
idade_usuario = int(input("Digite a sua idade : "))
if idade_usuario >= IDADE_MINIMA:
    {print("O usuário é maior de idade")}
else:
    {print("O usuário é menor de idade")}
