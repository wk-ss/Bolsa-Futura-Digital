"""
Crie um arquivo .py. Crie uma variável senha com o valor "Python123". 
Crie uma variável senha_valida e atribua a ela o resultado de uma 
expressão que verifique as seguintes condições (usando os operadores lógicos):

A senha não é vazia.
A senha tem mais de 8 caracteres.
A senha é exatamente igual a "Python123".
A senha é diferente de "123456".
Combine todas as condições com os operadores and e not e exiba o resultado final na tela."""

senha = "Python123"

def verificador(key):
    return key != "" and len(key) <= 9 and key == "Python123" and key != "123456"

print(f"A SENHA É VÁLIDA? {verificador(senha)}")
