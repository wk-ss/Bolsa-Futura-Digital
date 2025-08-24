"""
Listas Aninhadas
Dada a lista matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
• Acesse e imprima o n´umero 5
• Substitua o n´umero 8 por 10
Lista Modificada Esperada:
[[1 , 2 , 3] , [4 , 5 , 6] , [7 , 10 , 9]]"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz[1][1])
matriz[2][1] = 10
print(matriz)
