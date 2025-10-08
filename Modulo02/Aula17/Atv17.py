from abc import ABC, abstractmethod

class Biblioteca(ABC):
    def __init__(self):
        self.acervo = []

    @abstractmethod
    def gerenciar_acervo(self):
        pass

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.livros_emprestados = []
        self.atrasados = False  

    def autenticar_usuario(self):
        print(f"Usuário {self.nome} autenticado com sucesso!")

    def notificar_atraso(self):
        print(f"Aviso: {self.nome} possui livros atrasados!")

    def pegar_emprestado(self, biblioteca, livro):
        
        self.autenticar_usuario()

        if self.atrasados:
            self.notificar_atraso()

        if livro in biblioteca.acervo:
            biblioteca.acervo.remove(livro)
            self.livros_emprestados.append(livro)
            print(f"{self.nome} emprestou o livro '{livro}'.")
        else:
            print(f"O livro '{livro}' não está disponível.")

    def devolver(self, biblioteca, livro, sistema_pagamento):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            biblioteca.acervo.append(livro)
            multa = self.calcular_multa()

            if multa > 0:
                sistema_pagamento.processar_pagamento(self, multa)
            print(f"{self.nome} devolveu o livro '{livro}'.")
        else:
            print(f"{self.nome} não possui esse livro.")

    def calcular_multa(self):
        
        multa = 10 if self.atrasados else 0
        if multa > 0:
            print(f"Multa calculada: R${multa}")
        return multa

class Bibliotecario(Biblioteca):
    def __init__(self, nome):
        self.nome = nome

    def gerenciar_acervo(self):
        print(f"Bibliotecário {self.nome} está gerenciando o acervo.")

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro}' adicionado ao acervo.")


class SistemaPagamento:
    def processar_pagamento(self, usuario, valor):
        print(f"Pagamento de R${valor} processado para {usuario.nome}.")
