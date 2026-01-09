'''
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
'''

Nome_do_produto = "Cadeira Infantil"
Preço_unitário = 12.40
Quantidade = 3
preco_total = Preço_unitário * Quantidade
print(f"Na compra de {Quantidade} {Nome_do_produto} no valor de R${Preço_unitário:.2f} o valor total fica em R${preco_total:.2f}")