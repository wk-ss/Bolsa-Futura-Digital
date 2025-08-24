"""
Crie um dicion´ario estoque com:
• "ma¸c~a": 10
• "banana": 5
• "laranja": 8
Fa¸ca o seguinte:
• Adicione "pera" com quantidade 12
• Remova "banana"
• Imprima apenas os nomes dos itens (chaves)
Sa´ıda Esperada:
dict_keys ([ ’ m a ’, ’laranja ’, ’pera ’])

"""

estoque = {"maçã": 10, "banana": 5, "laranja": 8}
estoque["pera"] = 12
estoque.pop("banana")
print(estoque.keys())
