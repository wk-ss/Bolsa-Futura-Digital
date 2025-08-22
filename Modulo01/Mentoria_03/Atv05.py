"""
Crie um arquivo .py. Comece declarando uma variável estoque com o valor 50 e uma
variável valor, que receberá um número informado pelo usuário. O valor atribuído à variável
valor deve ser usado para atualizar a variável estoque, aumentando a quantidade em
estoque. Utilize o operador de atribuição de adição (+=) para atualizar a quantidade em
estoque. Mostre o novo valor na tela seguindo a estrutura: "Estoque inicial: resultado" e
"Estoque final: resultado".
Obs: Utilize o operador de atribuição de multiplicação [ += ], input(), print() para exibir os
valores na tela do usuário e siga a estrutura abaixo para receber os dados do usuário:
● variavel_inteira = int(input("Digite um valor: "))
● variavel_inteira = int(input("Digite outro valor: "))"""

estoque = 50

valor = int(input("Digite a quantidade para adicionar ao estoque: "))

estoque_inicial = 50
estoque += valor
print(f"Estoque inicial: {estoque_inicial}")
print(f"Estoque final: {estoque}")
