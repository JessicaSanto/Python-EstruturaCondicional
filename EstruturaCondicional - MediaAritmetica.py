# Ler as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcular a média aritmética
media = (nota1 + nota2) / 2

# Verificar se o aluno foi aprovado
if media >= 7:
    print(f"O aluno foi aprovado! Média: {media}")
else:
    print(f"O aluno foi reprovado. Média: {media}")