'''
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
'''

idade = int(input("Digite a sua idade: "))
if idade <= 12:
    print(f"Sua idade é {idade}, você é uma criança!")
elif idade > 12 and idade <= 17:
    print(f"Sua idade é {idade}, você é um adolescente!")
elif idade >= 18 and idade <= 59:
     print(f"Sua idade é {idade}, você é um adulto!")
else:
    print(f"Sua idade é {idade}, você é um idoso!")