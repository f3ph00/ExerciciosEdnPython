'''
2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
'''

import os

def criar_arquivo_tabular():
    pessoas = [
        ["Ana Silva", "25", "São Paulo"],
        ["João Souza", "30", "Rio de Janeiro"],
        ["Maria Oliveira", "22", "Belo Horizonte"],
        ["Carlos Lima", "28", "Curitiba"]
    ]

    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: dados.txt): ")

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            cabecalho = f"{'Nome':<20} | {'Idade':<5} | {'Cidade':<15}\n"
            divisoria = "-" * 45 + "\n"
            
            arquivo.write(cabecalho)
            arquivo.write(divisoria)

            for p in pessoas:
                linha = f"{p[0]:<20} | {p[1]:<5} | {p[2]:<15}\n"
                arquivo.write(linha)
        
        print(f"\n Sucesso! O arquivo '{nome_arquivo}' foi salvo corretamente.")
        print(f"Localização: {os.path.abspath(nome_arquivo)}")

    except Exception as e:
        print(f"\n Falha ao salvar o arquivo.")
        print(f"Erro detalhado: {e}")

if __name__ == "__main__":
    criar_arquivo_tabular()