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

def gerador(j, letras, num, simb, ruim = False):
    prefs = "" 
    if letras: prefs += string.ascii_letters
    if num: prefs += string.digits
    if simb: prefs += string.punctuation
    if not prefs: return None

    if ruim:
        ruins = "0O1lI|2Z5Ss6G8B`'\""
        for char in ruins:
            prefs = prefs.replace(char, "")

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

def complex(len, let, num, simb):
    pontos = 0
    if len > 12: pontos +=1
    if let and num: pontos += 1
    if simb: pontos += 1
    if pontos == 3:
        return 'Essa é uma senha forte!'
    elif pontos == 2:
        return 'Essa é uma senha mediana!'
    else:
        return 'Essa é uma senha fraca!'

while True:
    print("Bem vindo ao gerador de senha!".center(40, '-'))
    tam = tamanho("Digite o tamanho da senha: ")
    letras = s_n("Deseja incluir letras?(s/n): ")
    numeros = s_n("Deseja incluir numeros?(s/n): ")
    simbolos = s_n("Deseja incluir simbolos?(s/n): ")
    bad_char= s_n("Deseja remover os caracteres ambiguos?(s/n): ")
    senha = gerador(tam,letras,numeros,simbolos,bad_char)
    complexidade = complex(tam,letras,numeros,simbolos)
    
    if senha:
        print(f"Senha gerada: {senha}")
        print(complexidade)
    else:
        print('\nERRO: Nenhuma senha gerada, precisa escolher ao menos 1 tipo de caractere!')
    
    if not s_n("Deseja gerar outra senha? (s/n): "):
        print("Até a próxima!")
        break