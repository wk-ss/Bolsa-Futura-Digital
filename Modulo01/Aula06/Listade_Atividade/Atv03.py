'''
Crie um arquivo Python (.py) e solicite ao usuário que 
digite três números inteiros, armazenando-os em variáveis 
separadas. Em seguida, utilize estruturas condicionais para 
exibir os números na tela em ordem decrescente.

Obs: Utilize a função input() para solicitar os valores ao 
usuário e lembre-se de fazer a conversão do valor recebido 
para o tipo numérico (int), use a função print() para mostrar 
na tela uma mensagem final e utilize as condicionais para 
solucionar o problema em questão.'''
num1 = int(input("Digite o numero1: "))
num2 = int(input("Digite o numero2: "))
num3 = int(input("Digite o numero3: "))

if num1 >= num2:
    if num2 >=num3:
        print(f"{num1},{num2},{num3}")
    else:
        print(f"{num1},{num3},{num2}")
elif num2>=num3:
    if num3>=num1:
        print(f"{num2},{num3},{num1}")
    else:
        print(f"{num2},{num1},{num3}")
elif num3>=num2:
    if num2>=num1:
        print(f"{num3},{num2},{num1}")
    else:
        print(f"{num3},{num1},{num2}")