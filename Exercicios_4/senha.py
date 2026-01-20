'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''
senha = input('Digite uma senha: ')
numero = list(range(0,10))
numero = str(numero)
while len(senha) < 8:
    print('Senha muito curta')
    senha = input('Digite uma nova senha: ')

for i in senha:
    if i in numero:
        print(f"Obrigado sua senha é válida!")
        break
else:
    print('Senha Invalida!')