"""
Crie um arquivo .py utilizando o vscode e construa um código que peça um número ao usuário e então mostre a
 mensagem “O número informado foi [ número ].”. Armazene o valor passado pelo usuário em uma váriavel.
Obs: Utilize a função print() para mostrar a mensagem na tela, faça isso utilizando a F-STRING que é uma das
 formas de formatar um texto na linguagem python. Neste momento não é preciso realizar a conversão do valor 
 retornado pela função input() ⇒ int(input()).

Ex de f-string:
print(f“Texto qualquer { variável }”)

Saída esperada:
O número informado foi [ número ].
"""
num = int(input("Digite um numero : "))
print(f"O número informado foi {num}.")
#O número informado foi 3.