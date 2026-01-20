'''
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
'''
tabuada = int(input('Qual tabuada você quer? ex:1 '))
operacao = int(input('Operação [1] +, [2] -, [3] *, [4] /'))
numeros = list(range(1, 11))

if operacao == 1:
    print(f"Tabuada de adição do {tabuada}")
    for i in numeros:
        print(f"{tabuada} + {i} = {tabuada + i}")
elif operacao == 2:
    print(f"Tabuada de subtração do {tabuada}")
    for i in numeros:
        print(f"{tabuada} - {i} = {tabuada - i}")
elif operacao == 3:
    print(f"Tabuada de multiplicação do {tabuada}")
    for i in numeros:
        print(f"{tabuada} * {i} = {tabuada * i}")
elif operacao == 4:
    print(f"Tabuada de divisão do {tabuada}")
    for i in numeros:
        print(f"{tabuada} / {i} = {tabuada / i}")
else:
    print("Operação inválida. Escolha entre 1, 2, 3 ou 4.")