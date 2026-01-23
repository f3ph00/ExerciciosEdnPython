'''
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''

def precofinal(valor_original:float,porcentagem:int):
    return valor_original - (valor_original * porcentagem) / 100

print(precofinal(1500,10))
valor = float(input("Digite o valor do produto: "))
desconto = int(input("Digite a porcentagem do desconto: "))
if 0 <= desconto <= 100:
    print(f"O valor R${valor} com o desconto de {desconto}% fica no total de R${precofinal(valor,desconto):.2f}")
else:
    print("Porcentagem inválida. Digite um valor entre 0 e 100.")