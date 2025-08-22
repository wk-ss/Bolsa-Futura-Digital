"""
Crie um arquivo .py. Comece com uma variável tarefas com o valor 20 e crie uma variável
chamada numero_pessoas que receberá um número informado pelo usuário. Utilize o
operador de atribuição de divisão inteira (//=) para dividir as tarefas igualmente entre as
pessoas e atualizar a variável tarefas. Mostre o número de tarefas que cada pessoa
recebeu na tela.
Obs: Utilize o operador de atribuição de divisão inteira [ //= ], input() e print() para exibir os
valores na tela do usuário e siga a estrutura abaixo para receber os dados do usuário:
● variavel_inteira = int(input("Digite um valor: "))
● variavel_inteira = int(input("Digite outro valor: "))
"""
numero = 2
tarefas = int(input("Digite o tarefas: "))
numero_pessoas = numero
numero //= tarefas
print(f"Valor inicial de numero: {numero_pessoas}")
print(f"Valor final de numero (após elevar a {tarefas}): {numero}")
