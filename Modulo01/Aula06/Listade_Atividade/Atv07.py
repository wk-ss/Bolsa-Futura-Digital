"""
Crie um arquivo Python (.py) para um programa que simule o
rastreamento do status de um pedido online. O programa deve
solicitar ao usuário que digite o status atual do pedido (como
"recebido", "em_preparação", "em_entrega" ou "entregue"). Em
seguida, utilize a estrutura match case para verificar o texto
inserido e exibir uma mensagem correspondente ao status do pedido.
Caso o usuário digite um status não previsto, o programa deve exibir
uma mensagem informando que o status não foi identificado.

Obs: Utilize a função input() para receber o texto do status do usuário,
e a função print() para exibir a mensagem final."""

status = input(
    "digite o status da entrega com : recebido,em_preparação,em_entrega,entregue ::"
)
match status:
    case "recebido":
        print("recebido")
    case "em_preparação":
        print("em_preparação")
    case "em_entrega":
        print("em_entrega")
    case "entregue":
        print("entregue")
    case _:
        print("comando invalido")
