'''Crie um arquivo .py. Escreva um código que vai armazenar a sequência
'João', 'Maria', 'José' em uma lista chamada clientes e vai armazenar a
sequência 1500, 2500, 800 em uma lista chamada saldos. Você precisa
imprimir os nomes dos clientes e os saldos referentes a cada cliente, use o
enumerate() e zip() para conseguir o resultado esperado'''
clientes = ["João", "Maria", "José"]
saldos = [1500, 2500, 800]

for indice, (cliente, saldo) in enumerate(zip(clientes, saldos), start=1):
    print(f"{indice}. Cliente: {cliente} - Saldo: R${saldo:.2f}")
