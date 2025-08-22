"""
Crie um arquivo Python (.py) que funcione como uma calculadora.
O programa deve pedir ao usuário dois números inteiros e um operador
aritmético (+, -, *, /, //, %). Em seguida, utilize uma estrutura
condicional para verificar qual operador foi inserido e realizar a
operação matemática correspondente. Por fim, exiba o resultado na
tela de forma clara.

Obs: Utilize a função input() para solicitar os valores ao usuário
e lembre-se de fazer a conversão do valor recebido para o tipo numérico
(int), use a função print() para mostrar na tela uma mensagem final e
 utilize as condicionais para solucionar o problema em questão."""

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))


operador = input("Digite o operador (+, -, *, /, //, %): ")


if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
elif operador == "//":
    if num2 != 0:
        resultado = num1 // num2
    else:
        resultado = "Erro: divisão por zero!"
elif operador == "%":
    if num2 != 0:
        resultado = num1 % num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operador inválido!"


print(f"Resultado da operação {num1} {operador} {num2} = {resultado}")
