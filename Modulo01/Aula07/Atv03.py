'''Crie um arquivo .py .Escreva um código que vai armazenar a sequência 1200,
1500, 1100, 2000, 2500, 1800, 1300 de vendas de cada dia da semana em
uma estrutura de dados do tipo lista chamada vendas semana. Pense no
seguinte cenário, você precisa saber o valor total de vendas durante a
semana e além disso, você precisa descobrir qual dia da semana com o
menor valor de venda.'''

vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]

total_vendas = sum(vendas_semana)


menor_venda = min(vendas_semana)

print("Valor total de vendas :", total_vendas)
print(f"Menor venda foi {(vendas_semana.index(menor_venda)+1)} no dia  ")
