"""
Dada a lista numeros = [10, 20, 30, 40, 50], fa¸ca:
• Acesse e imprima o terceiro elemento
• Adicione o n´umero 60 no final da lista
• Remova o n´umero 20 da lista
Lista Final Esperada:
[10 , 30 , 40 , 50 , 60]"""

numeros = [10, 20, 30, 40, 50]
print(numeros[2])
numeros.append(60)
print(numeros)
numeros.pop(1)
print(numeros)
