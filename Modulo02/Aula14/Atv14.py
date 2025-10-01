"""Imagine que você está desenvolvendo o sistema de um jogo de RPG.
Cada personagem tem um nome e pontos de vida (HP).
Queremos garantir que o HP nunca seja negativo.
Regras
1. Crie a classe Personagem com:
○ Atributo _nome (string).
○ Atributo _hp (inteiro, inicia em 100).
2. Métodos:
○ get_nome() → retorna o nome.
○ set_nome(novo_nome) → altera o nome (sem validação).
○ get_hp() → retorna o HP.
○ sofrer_dano(valor) → diminui o HP, mas nunca pode ser menor que 0.
○ curar(valor) → aumenta o HP, mas nunca pode passar de 100.
3. Programa principal:
○ Crie um personagem chamado "Herói".
○ Faça ele sofrer 30 de dano e mostre o HP.
○ Depois cure 50 e mostre o HP.
○ Troque o nome para "João" e mostre.
Saída esperada:
Nome: Herói
HP inicial: 100
HP após dano: 70
HP após cura: 100
Novo nome: João"""


class Game:
    def __init__(self, nome, ataque, defesa, hp = 100):
        self._nome = nome
        self._hp = hp
        self._ataque = ataque
        self._defesa = defesa


    def get_nome(self):
        print(f"Nome: {self._nome}")

    def set_nome(self, novo_nome):
        self._nome = novo_nome
        print(f"Novo nome: {self._nome}")

    def get_hp(self):
        print(f"HP inicial: {self._hp}")

    def sofrer_dano(self, valor):
        if (self._defesa - valor) < 0:
            self._hp = self._hp + (self._defesa - valor)
            print(f"{self._nome} recebeu {self._defesa - valor} de dano ")
            print(f"HP após Dano: {self._hp}")
            self.status()
        else:
            print("Não recebeu Dano")

    def curar(self, valor):
        if (self._hp + valor) <= 100:
            self._hp = self._hp + valor
            print(f"HP após cura: {valor}")
        else:
            self._hp = 100
            print("A vida não pode ultrapasar de 100")
            print(f"HP após cura: {valor}")
    
    def status(self):
        if self._hp <= 0:
            print(f"O personagem {self._nome} moreu.")


p1 = Game("Herói", 10, 5)
p1.get_nome()
p1.get_hp()
p1.sofrer_dano(35)
p1.curar(30)
p1.set_nome("João")
print(5*("###"))
p2 = Game("Mago", 10, 5)
p2.get_nome()
p2.get_hp()
p2.sofrer_dano(5)
p2.sofrer_dano(105)
p2.curar(200)
p2.set_nome("lili")