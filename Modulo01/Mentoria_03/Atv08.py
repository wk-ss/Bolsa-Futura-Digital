"""
Crie um arquivo .py. Comece declarando uma variável saldo_bancario com o valor 1000.
Peça ao usuário para inserir três valores: um valor de depósito, um valor de saque e um
fator de juros.
● Utilize o operador de atribuição de adição (+=) para adicionar o depósito ao
saldo_bancario.
● Utilize o operador de atribuição de subtração (-=) para subtrair o saque do
saldo_bancario.
● Utilize o operador de atribuição de multiplicação (*=) para aplicar o fator de juros ao
saldo_bancario.
●
Utilize input() para capturar dados numéricos decimais do usuário, convertendo-os para
float(), e use print() para exibir os resultados na tela.
● variavel_decimal = float(input("Digite um valor: "))"""

saldo_bancario= 1000
deposito = float(input("um valor de depósito: "))
saldo_bancario+=deposito
print(saldo_bancario)
saque = float(input("um valor do soque: "))
saldo_bancario-=saque
print(saldo_bancario)
juros = float(input("um valor do juros "))
saldo_bancario*=juros
print(saldo_bancario)