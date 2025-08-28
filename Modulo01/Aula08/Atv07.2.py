"""Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função cadastrar_usuario que aceite nome e email como argumentos
obrigatórios e qualquer outra informação como kwargs. Imprima todos os
dados recebidos.
Exemplo de uso: cadastrar_usuario(nome="Ana", email="ana@email.com",
idade=30, cidade="Salvador")"""


def cadastrar_usuario(nome: str, email: str, **kwargs: str) -> str:
    print("Dados obrigatórios:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")

    if kwargs:
        print("Outras informações:")
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")


cadastrar_usuario(nome="Ana", email="ana@email.com", idade=30, cidade="Salvador")
