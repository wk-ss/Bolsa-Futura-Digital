"""Faça um programa em Python e salve o arquivo na extensão .py que simule
uma pequena calculadora:
- O programa deve pedir dois números ao usuário.
- Depois, deve pedir a operação desejada (+, -, *, /).
- As operações devem ser implementadas em funções (ex: funcao soma, subtracao,
multiplicacao e divisao).
- Trate os seguintes casos usando try/except/else/finally:
1. Se o usuário digitar algo que não seja número → mostrar "Erro: valor inválido".
2. Se o usuário escolher "/" e o denominador for zero → mostrar "Erro: divisão por zero".
3. Se o usuário escolher uma operação inválida → mostrar "Erro: operação inválida".
4. Caso contrário → mostrar o resultado chamando a função correspondente.
- No final, use o bloco finally para exibir a mensagem "Fim do programa"."""


def soma(num1: float, num2: float) -> float:
    return num1 + num2


def sub(num1: float, num2: float) -> float:
    return num1 - num2


def mult(num1: float, num2: float) -> float:
    return num1 * num2


def div(num1: float, num2: float) -> float:
    return num1 / num2


def calculadora():
    repeticao = True
    while repeticao:
        try:
            num1 = int(input("Digite o número 1: "))
            num2 = int(input("Digite o número 2: "))

            print(5 * ("---"))
            print("   MENU   ")
            print(" (1) Soma  ")
            print(" (2) Subtração  ")
            print(" (3) Multiplicação  ")
            print(" (4) Divisão  ")
            print(" (0) Sair  ")

            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                print(f"A soma foi = {soma(num1, num2)}")

            elif opcao == 2:
                print(f"A subtração foi = {sub(num1, num2)}")

            elif opcao == 3:
                print(f"A multiplicação foi = {mult(num1, num2)}")

            elif opcao == 4:
                try:
                    print(f"A divisão foi = {div(num1, num2):.2f}")
                except ZeroDivisionError:
                    print("Erro: divisão por zero")

            elif opcao == 0:
                print("O código foi encerrado.")
                repeticao = False

            else:
                print("Erro: operação inválida")

        except ValueError:
            print("Erro: valor inválido")

        else:
            print("Operação realizada com sucesso.")

        finally:
            print("Fim do programa\n")


calculadora()
