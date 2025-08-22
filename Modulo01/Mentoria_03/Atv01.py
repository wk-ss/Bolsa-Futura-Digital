"""
Crie um arquivo .py e peça para o usuário inserir dois valores inteiros. Armazene-os nas
variáveis num1 e num2. Crie uma variável SOMA e atribua a ela o valor da soma de num1
por num2, além disso crie uma variável SUBTRACAO e atribua a ela o valor da subtração
de num1 por num2. Mostre os resultados na tela no formato "num1 + num2 = resultado" e
"num1 - num2 = resultado".
Obs: Utilize os operadores de aritméticos de SOMA e SUBTRAÇÃO, use a função input()
para capturar os dados, print() para exibir e siga a estrutura abaixo para receber os dados
do usuário:
● variavel_inteira = int(input("Digite um valor: "))
● variavel_inteira = int(input("Digite outro valor: "))
"""

num1 = int(input("digite o numero1: "))
num2 = int(input("digite o numero2: "))
soma = num1 + num2
subtracao = num1 - num2
print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {subtracao}")
