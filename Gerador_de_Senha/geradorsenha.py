import random
import string

def gerador(j):
    modulosenha = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    random.choice(modulosenha)

while True:
    print("Bem vindo ao gerador de senha:".center(30,'-'))
    print(gerador(10))
    
    