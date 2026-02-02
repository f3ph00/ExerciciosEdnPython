'''
4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
'''

import json
import os

def gerenciar_dados_json():
    dados_pessoais = {
        "pessoas": [
            {"nome": "Ana Silva", "idade": 25, "cidade": "São Paulo"},
            {"nome": "João Souza", "idade": 30, "cidade": "Rio de Janeiro"},
            {"nome": "Maria Oliveira", "idade": 22, "cidade": "Belo Horizonte"}
        ]
    }

    nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_pessoais, arquivo, indent=4, ensure_ascii=False)
        print(f"\n Dados salvos com sucesso em '{nome_arquivo}'!")

    except Exception as e:
        print(f"\n Falha ao salvar o arquivo.")
        print(f"Erro: {e}")
        return

    print(f"\nLendo dados do arquivo '{nome_arquivo}'...")
    try:
        if not os.path.exists(nome_arquivo):
            raise FileNotFoundError

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_carregados = json.load(arquivo)
            
            print("\n--- Dados Carregados do JSON ---")
            for pessoa in dados_carregados["pessoas"]:
                print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Cidade: {pessoa['cidade']}")
            print("-" * 32)

    except FileNotFoundError:
        print(f"\n Falha: O arquivo '{nome_arquivo}' não existe para leitura.")
    except json.JSONDecodeError:
        print(f"\n Falha: O arquivo existe, mas não está em um formato JSON válido.")
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado na leitura.")
        print(f"Erro: {e}")

if __name__ == "__main__":
    gerenciar_dados_json()