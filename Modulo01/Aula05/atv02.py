"""
Crie um arquivo .py. Crie duas variáveis: idade com o valor de 
sua preferência e possui_carteira com o valor True. Use o operador 
lógico and para verificar se a pessoa é maior de idade (idade >= 18) 
E possua carteira de motorista. Armazene o resultado em uma variável 
pode_dirigir e exiba-o na tela seguindo a estrutura a seguir “pode 
dirigir? resultado da operação lógica“.

Obs: Utilize os operadores lógicos para obter a resposta print() para 
mostrar o texto na tela"""
idade = 26
possui_carteira = True
pode_dirigir = (idade>=18) and possui_carteira

print(f"pode dirigir? {pode_dirigir}" )