""" "
Crie um arquivo .py. Defina uma senha correta, por exemplo, "python123".
Peça ao usuário para digitar uma senha. Use um laço while que continue
pedindo a senha enquanto ela for diferente da senha correta. Quando a senha
estiver certa, exiba uma mensagem de sucesso.

Obs: Utilize input() para capturar a senha e print() para exibir as mensagens."""

key = "python123"

tentativa = True
while tentativa:
    senha = input("digite a senha :")
    if senha == key:
        tentativa = False
        print("senha correta")
    else:
        print("senha falsa , digite novamente .")
