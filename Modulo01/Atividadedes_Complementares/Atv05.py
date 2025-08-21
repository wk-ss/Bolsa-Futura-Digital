"""
Dada a tupla cores = ("vermelho", "verde", "azul", "verde"):
• Converta-a em um conjunto para remover duplicatas
• Adicione a cor "amarelo" ao conjunto
Sa´ıda Esperada:
{’vermelho ’, ’verde ’, ’azul ’, ’amarelo ’}"""

cores = ("vermelho", "verde", "azul", "verde")

conjunto_cores = set(cores)
print(conjunto_cores)

conjunto_cores.add("amarelo")

print(conjunto_cores)
