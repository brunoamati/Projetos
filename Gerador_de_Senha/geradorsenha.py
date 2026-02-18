import random
import string

def tamanho(tam):
    while True:
        try:
            valor = int(input(tam))
            if valor <= 0:
                print('Digite um numero maior que 0')
            else:
                    return valor
        except ValueError:
            print('ERRO: Digite apenas numeros inteiros!')

def gerador(j):
    h = ''
    modulosenha = string.ascii_letters + string.digits + string.punctuation

    for i in range(j):
       h += random.choice(modulosenha)
    return h

loop = 1
while loop == 1:
    print("Bem vindo ao gerador de senha!".center(40, '-'))
    tam = tamanho("Digite o tamanho da senha: ")
    senha = gerador(tam)
    print(f"Senha gerada: {senha}")
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
    
    