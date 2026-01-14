'''
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''
temperatura = float(input("Digite a temperatura: "))
origem = int(input("Qual é a unidade de origem: 1 - Celsius, 2 - Fahrenheit, 3 - Kelvin"))
converter = int(input("Para qual unidade você quer converter: 1 - Celsius, 2 - Fahrenheit, 3 - Kelvin"))
if origem == 1 and converter == 2:
    FahCel = (temperatura * 1.8) + 32
    print(f"A conversão de {temperatura}C° para Fahrenheit fica {FahCel}F°")
if origem == 1 and converter == 3:
    KelCel = temperatura + 273.15
    print(f"A conversão de {temperatura}C° para Kelvin fica {KelCel}K°")
if origem == 1 and converter == 1:
    print(f"{temperatura}C°")
if origem == 2 and converter == 1:
    CelFah = (temperatura - 32) / 1.8
    print(f"A conversão de {temperatura}F° para Celsius fica {CelFah:.2f}C°")
if origem == 2 and converter == 3:
    KelFah = ((temperatura - 32) / 1.8) + 273.15
    print(f"A conversão de {temperatura}F° para Kelvin fica {KelFah:.2f}K°")
if origem == 2 and converter == 2:
    print(f"{temperatura}F°")
if origem == 3 and converter == 1:
    CelKel = temperatura - 273.15
    print(f"A conversão de {temperatura}K° para Celsius fica {CelKel:.2f}C°")
if origem == 3 and converter == 2:
    FahKel = ((temperatura - 273.15) * 1.8) + 32
    print(f"A conversão de {temperatura}K° para Fahrenheit fica {FahKel:.2f}F°")
if origem == 3 and converter == 3:
    print(f"{temperatura}K°")