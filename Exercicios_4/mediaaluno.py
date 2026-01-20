'''
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''

i = 0
numero_notas = int(input('Quantas notas você irá adicionar? '))
notas = []
while numero_notas > i:
    notas.append(float(input("Digite a nota do aluno: ")))
    i += 1
media = (sum(notas)) / numero_notas
print(f"A média da turma com {numero_notas} alunos é {media:.2f}")
