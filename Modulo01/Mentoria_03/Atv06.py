"""
Crie um arquivo .py. Comece declarando uma variável numero com o valor 2 e uma variável
expoente, que receberá um valor numérico informado pelo usuário. O valor atribuído à
variável expoente deve ser usado para atualizar a variável numero, elevando-o a essa
potência. Utilize o operador de atribuição de potência (**=) para realizar essa operação.
Mostre o valor inicial de numero e o valor final na tela.
Obs:Utilize input() para capturar um número inteiro, convertendo-o para int(), use o
operador de atribuição de potência (**=) para atualizar a variável e, por fim, use print() para
exibir os valores inicial e final."
● variavel_decimal = float(input("Digite um valor: "))
"""

numero = 2
expoente = int(input("Digite o expoente: "))
numero_inicial = numero
numero **= expoente
print(f"Valor inicial de numero: {numero_inicial}")
print(f"Valor final de numero (após elevar a {expoente}): {numero}")
