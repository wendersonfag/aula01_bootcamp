
CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o seu salário: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o seu bônus: "))
# 4) Calcule o valor do bônus final
resultado_bonus = CONSTANTE_BONUS + salario * bonus
# 5) Imprima cálculo do KPI para o usuário
print(resultado_bonus)
# 6) I'mprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome_usuario}, o seu bônus foi de {resultado_bonus}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?