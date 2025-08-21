"""
Dada a string "programa¸c~ao":
• Inverta a string
• Verifique se a string original ´e igual `a string invertida
Sa´ıda Esperada:
o a m a r g o r p
False"""

texto = "programacao"
invertida = texto[::-1]
print(" ".join(invertida))
print(texto == invertida)
