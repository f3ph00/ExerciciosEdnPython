'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''

Valor_em_reais = 100.00
Taxa_do_dolar = 5.20
Taxa_do_euro = 6.15
conversao_dolar = Valor_em_reais / Taxa_do_dolar
conversao_euro = Valor_em_reais / Taxa_do_euro

print(f"Valor em reais: R${Valor_em_reais:.2f}")
print(f"Taxa do dólar: R${Taxa_do_dolar:.2f}")
print(f"Taxa do euro: R${Taxa_do_euro:.2f}")
print(f"Convertido para dólar: ${conversao_dolar:.2f}")
print(f"Convertido para euro: €{conversao_euro:.2f}")
