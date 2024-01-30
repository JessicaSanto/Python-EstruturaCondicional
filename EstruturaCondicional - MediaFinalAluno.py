# Leitura das duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média aritmética
media = (nota1 + nota2) / 2

# Verificação das condições
if media >= 7:
    print(f"Aprovado! Média: {media}")
elif 5 <= media < 7:
    print(f"Exame! Média: {media}")
else:
    print(f"Reprovado! Média: {media}")
