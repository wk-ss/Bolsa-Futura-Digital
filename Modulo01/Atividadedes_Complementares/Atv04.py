"""
Crie um dicion´ario chamado aluno com:
• "nome": ”Maria”
• "idade": 22
• "curso": ”Engenharia”
Depois:
• Adicione uma nova chave "notas" com a lista [8.5, 7.0, 9.2]
• Imprima apenas o valor da chave "curso"
"""

aluno = {"nome": "Maria", "idade": 22, "curso": "Engenharia"}


aluno["notas"] = [8.5, 7.0, 9.2]
print(aluno)

print(aluno["curso"])
