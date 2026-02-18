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

def gerador(j, letras, num, simb):
    prefs = "" 
    if letras: prefs += string.ascii_letters
    if num: prefs += string.digits
    if simb: prefs += string.punctuation
    if not prefs: return None

    senha = ''
    for i in range(j):
       senha += random.choice(prefs)
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
    letras = s_n("Deseja incluir letras?(s/n): ")
    numeros = s_n("Deseja incluir numeros?(s/n): ")
    simbolos = s_n("Deseja incluir simbolos?(s/n): ")
    senha = gerador(tam,letras,numeros,simbolos)
    
    if senha:
        print(f"Senha gerada: {senha}")
    else:
        print('\nERRO: Nenhuma senha gerada, precisa escolher ao menos 1 tipo de caractere!')
    
    if not s_n("Deseja gerar outra senha? (s/n): "):
        print("Até a próxima!")
        break
    
    