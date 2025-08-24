"""
Dada a lista dados = [42, 3.14, "Python", True, [1, 2]], percorra cada elemento
e imprima seu tipo.
Sa´ıda Esperada:
<class ’int ’>
<class ’float ’>
<class ’str ’>
<class ’bool ’>
<class ’list ’>"""

dados = [42, 3.14, "Python", True, [1, 2]]

for item in dados:
    print(type(item))
