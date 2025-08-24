"""Dada a string "Python ´e incr´ıvel!", fa¸ca o seguinte:
• Conte quantos caracteres ela possui (incluindo espa¸cos)
• Converta toda a string para mai´usculas
• Substitua a palavra ”incr´ıvel”por ”poderoso”
Sa´ıda Esperada:
18
PYTHON I N C R V E L !
Python poderoso !
"""

var = "Python e incrivel!"
print(len(var))
print(var.upper())
print(var.replace("incrivel", "poderoso"))
