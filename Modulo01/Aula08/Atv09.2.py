"""Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função chamada buscar_livro que aceite um título obrigatório e kwargs
como filtros de busca (por exemplo, autor="Machado de Assis", ano=1899).
Imprima o título e todos os filtros aplicados."""


def buscar_livro(titulo: str, **kwargs: int):
    print(f"Título do livro: {titulo}")
    if kwargs:
        print("Filtros aplicados:")
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")


buscar_livro("Dom Casmurro", autor="Machado de Assis", ano=1899)
