"""
Crie um arquivo .py e peça para o usuário inserir dois valores inteiros. Armazene-os nas
variáveis dividendo e divisor. Crie uma variável RESTO e atribua a ela o valor do resto da
divisão de dividendo por divisor. Mostre o resultado na tela no formato "divisor / dividendo =
resultado | resto = resto".
Obs: Utilize o operador de módulo [ % ], use a função input() para capturar os dados, print()
para exibir e siga a estrutura abaixo para receber os dados do usuário:
● variavel_inteira = int(input("Digite um valor: "))
● variavel_inteira = int(input("Digite outro valor: "))"""

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))


resultado = dividendo // divisor
resto = dividendo % divisor

print(f"{dividendo} / {divisor} = {resultado} | resto = {resto}")
