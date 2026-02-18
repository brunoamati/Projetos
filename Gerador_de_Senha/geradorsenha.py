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
    senha = ''

    modulosenha = string.ascii_letters + string.digits + string.punctuation

    for i in range(j):
       senha += random.choice(modulosenha)
    return senha

def s_n(msg):
   while True:
        resp = input(msg).strip().lower()
        if resp == 's': return True
        if resp == 'n': return False
        print("Responda apenas com 's' ou 'n'.")
 
loop = 1
while loop == 1:
    print("Bem vindo ao gerador de senha!".center(40, '-'))
    tam = tamanho("Digite o tamanho da senha: ")
    senha = gerador(tam)
    print(f"Senha gerada: {senha}")
    if not s_n("Deseja gerar outra senha? (s/n): "):
        print("Até a próxima!")
        break
    
    