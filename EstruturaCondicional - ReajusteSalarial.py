# Leitura do salário do funcionário
salario = float(input("Digite o salário do funcionário: "))

# Verificação do reajuste com base nas condições
if salario < 500:
    reajuste = salario * 0.15
elif 500 <= salario <= 1000:
    reajuste = salario * 0.10
elif 1000 < salario <= 2000:
    reajuste = salario * 0.05
else:
    reajuste = salario * 0.025

# Cálculo do novo salário
novo_salario = salario + reajuste

# Exibição do resultado
print("O novo salário é:", novo_salario)