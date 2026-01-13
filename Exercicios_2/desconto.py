'''
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''
Nome_do_produto = "Camiseta"
Preco_original = 50.00
Porcentagem_de_desconto = 20

valor_desconto = (Preco_original * Porcentagem_de_desconto) / 100
preco_final = Preco_original - valor_desconto

print(f"Produto: {Nome_do_produto}")
print(f"Preço original: R${Preco_original:.2f}")
print(f"Desconto: {Porcentagem_de_desconto}% (R${valor_desconto:.2f})")
print(f"Preço com desconto: R${preco_final:.2f}")

