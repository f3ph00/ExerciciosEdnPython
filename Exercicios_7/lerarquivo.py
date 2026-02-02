'''
3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.
'''

def ler_arquivo_usuario():
    nome_arquivo = input("Digite o nome do arquivo que deseja ler (ex: dados.txt): ")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"\n--- Conteúdo de '{nome_arquivo}' ---\n")
            
            for linha in arquivo:
                print(linha.strip())
            
            print("\n" + "-" * 30)
            print("Leitura concluída com sucesso.")

    except FileNotFoundError:
        print(f"\n Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Verifique se o nome está correto ou se o arquivo está na mesma pasta do programa.")
    
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado ao ler o arquivo.")
        print(f"Detalhes: {e}")

if __name__ == "__main__":
    ler_arquivo_usuario()