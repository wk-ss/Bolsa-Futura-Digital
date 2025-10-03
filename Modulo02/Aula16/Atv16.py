"""Atividade: Sistema de Contas Bancárias em Python
Objetivo:
Nesta atividade, você vai criar um sistema de gestão de contas bancárias utilizando classes abstratas. O
sistema deve seguir a estrutura definida pela classe abstrata ContaBancaria e implementar diferentes tipos de
contas, como Conta Corrente e Conta Poupança, com comportamentos distintos.
Passos para a atividade:
OBS: Para ter as saídas podem usar valores genéricos
1. Criar a classe abstrata ContaBancaria:
○ Defina a classe ContaBancaria como uma classe abstrata.
○ A classe deve ter:
■ Um método abstrato depositar(valor), que será implementado pelas
subclasses.
■ Um método abstrato sacar(valor), que também será implementado pelas
subclasses.
■ A propriedade saldo que será utilizada para armazenar e validar o saldo da conta
(não pode ser negativo).
2. Criar a subclasse ContaCorrente:
○ A ContaCorrente deve herdar de ContaBancaria e implementar:
■ O método depositar(valor) para adicionar o valor ao saldo.
■ O método sacar(valor) para subtrair o valor do saldo.
■ A taxa de manutenção mensal deve ser subtraída do saldo automaticamente após
cada saque.
3. Criar a subclasse ContaPoupanca:
○ A ContaPoupanca deve herdar de ContaBancaria e implementar:
■ O método depositar(valor) para adicionar o valor ao saldo.
■ O método sacar(valor) para subtrair o valor do saldo.
■ O método aplicar_juros() que aplica um rendimento no saldo (um percentual
sobre o saldo) após o depósito.
4. Testar o código:
○ Crie instâncias de ContaCorrente e ContaPoupanca.
○ Realize operações de depósito, saque e aplicação de juros.
○ Exiba os saldos finais das contas após as operações."""

from abc import ABC, abstractmethod


class ContaBancaria(ABC):
    def __new__(cls, *args, **kwargs):
        print(5 * ("-_-_"))
        print("Bem-vindo ao banco!")
        print(5 * ("-_-_"))
        return super().__new__(cls)

    def __init__(self, saldo=0):
        self._saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def get_saldo(self):
        print(f"O seu saldo é {self._saldo}")
        return self._saldo


class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        self._saldo += valor
        print(f"vc depositou o valor de {valor}")

    def sacar(self, valor):
        self._saldo -= valor
        print(f"vc sacou o valor de {valor}")


class ContaPoupanca(ContaBancaria):
    def depositar(self, valor):
        self._saldo += valor
        print(f"vc depositou o valor de {valor}")

    def sacar(self, valor):
        self._saldo -= valor
        print(f"vc sacou o valor de {valor}")

    def aplicar_juros(self):
        self._saldo *= 1.06


cc = ContaCorrente(100)
cc.get_saldo()
cc.depositar(50)
cc.get_saldo()
cc.sacar(30)
cc.get_saldo()

cp = ContaPoupanca(200)
cp.get_saldo()
cp.depositar(100)
cp.get_saldo()
cp.aplicar_juros()
cp.get_saldo()
