import random
import string

def gerador(j):
    h = ''
    modulosenha = string.ascii_letters + string.digits + string.punctuation

    for i in range(j):
       h += random.choice(modulosenha)
    return h

loop = 1
while loop == 1:
    print("Bem vindo ao gerador de senha!".center(40, '-'))

    while True:
        try:
            tam = int(input('Digite o tamanho da senha: '))
            if tam <= 0:
                print(f'Digite um numero maior que 0')
                continue
            senha = gerador(tam)
            print(f'Sua senha gerada é: {senha}')
            break
        except ValueError:
            print('ERRO: Digite apenas numeros inteiros!')
        
    while True:
        cont = input('Deseja gerar outra senha?(s/n): ').strip().lower()
        if cont == 'n':
            loop = 0
            print("Obrigado por usar meu gerador!")
            break
        elif cont == 's':
            loop = 1
            print(f'Retornando ao inicio!')
            break
        else:
            print("Opção inválida. Por favor, digite 's' ou 'n'.")
    
    