"""
Para realizar este exercício, crie um arquivo Python (.py)
onde o programa irá solicitar ao usuário uma nota de 1 a 5.
Em seguida, utilize a estrutura de controle de fluxo match
case para comparar a nota fornecida com cada caso possível,
exibindo um feedback correspondente. Se a nota estiver fora do
intervalo de 1 a 5, o caso padrão (_) deverá ser usado para
exibir uma mensagem de erro.

Obs: Utilize a função input() para receber a nota do usuário e a
função print() para exibir a mensagem final. Não se esqueça de
converter o valor recebido para um tipo numérico (geralmente int)."""

nota = int(input("Digite uma nota de 1 a 5: "))

match nota:
    case 1:
        print("Nota 1 - Muito ruim! 😞")
    case 2:
        print("Nota 2 - Ruim, precisa melhorar.")
    case 3:
        print("Nota 3 - Regular, está na média.")
    case 4:
        print("Nota 4 - Bom, continue assim! 👍")
    case 5:
        print("Nota 5 - Excelente, parabéns! 🎉")
    case _:
        print("Erro: digite um número entre 1 e 5.")
