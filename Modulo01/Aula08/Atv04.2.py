"""Crie um arquivo .py. Dentro do seu arquivo, construa 
um código que define uma função que receba um número 
variável de strings (*args). A função deve concatená-las, 
mesclá-las em um único valor de texto string e retorná-la.
Exemplo de uso: juntar_strings("Olá", " ", "mundo", "!") 
deve retornar "Olá mundo!"."""

def mescla(*palvras:str)->str:
    mensagem=[]
    for i in palvras:
        mensagem.append(i)
    return mensagem

print(mescla("a", "casa", "caiu"))