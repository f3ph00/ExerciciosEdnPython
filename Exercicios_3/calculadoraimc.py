'''
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
'''
peso = float(input("Digitre o seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
calculo = peso / (altura ** 2)
if calculo < 18.5:
    print(f"Seu IMC é {calculo:.2f}, você está abaixo do peso!")
elif calculo >= 18.5 and calculo <= 25:
    print(f"Seu IMC é {calculo:.2f}, você está com peso normal!")
elif calculo >= 25 and calculo <= 30:
    print(f"Seu IMC é {calculo:.2f}, você está com sobrepeso!")
else:
    (print(f"Seu IMC é {calculo:.2f}, você está Obeso!"))