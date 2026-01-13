'''
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
'''


Distancia_percorrida = 300
Combustivel_gasto =  25
Consumo = Distancia_percorrida / Combustivel_gasto
print(f"Distância percorrida: {Distancia_percorrida} km")
print(f"Combustível gasto: {Combustivel_gasto} litros")
print(f"Consumo médio: {Consumo:.2f} km/l")

