"""Crie um arquivo .py,crie duas variáveis, tem_wifi com o valor False 
e tem_dados_moveis com o valor True. Use o operador OR para verificar 
se o celular pode se conectar à internet (se ele tem wifi OU dados móveis). 
Exiba o resultado na tela seguindo a seguinte estrutura a seguir “O celular 
pode se conectar a internet? [ resultado da operação lógica ]“."""
tem_wifi = False
tem_dados_moveis = True
pode_conectar = tem_wifi or tem_dados_moveis
print(f"O celular pode se conectar a internet? {pode_conectar}")