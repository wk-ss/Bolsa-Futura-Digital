"""
Crie um arquivo .py e peça para o usuário inserir dois valores inteiros. Armazene-os nas
variáveis num1 e num2. Crie uma variável POTENCIA e atribua a ela o valor de num1
elevado à potência de num2. Em seguida, crie uma variável DIVISAO_INTEIRA e atribua a
ela o resultado da divisão inteira de num1 por num2. Mostre ambos os resultados na tela no
formato "num1 ** num2 = potencia"; "num1 // num2 = divisao_inteira".
Obs: Utilize o operador de módulo [ % ], use a função input() para capturar os dados, print()
para exibir e siga a estrutura abaixo para receber os dados do usuário:
● variavel_inteira = int(input("Digite um valor: "))
● variavel_inteira = int(input("Digite outro valor: "))
"""

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
potencia = num1**num2
divisao_inteira = num1 // num2
print(f"{num1} ** {num2} = {potencia}")
print(f"{num1} // {num2} = {divisao_inteira}")
