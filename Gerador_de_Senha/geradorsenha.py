import random
import string

def gerador(j):
    h = ''
    modulosenha = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    for i in range(j):
       h += random.choice(modulosenha)
    return("sua senha gerada é: " + h)

while True:
    print("Bem vindo ao gerador de senha!".center(30,'-'))
    print(gerador(10))
    break
    
    