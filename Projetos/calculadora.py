def pegarNumero(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calculadora(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        while True:
            d = input('Deseja calcular o primeiro valor menos o segundo? (s/n) Caso não será calculado o inverso: ').strip().lower()
            if d == 's':
                return a - b
            elif d == 'n':
                return b - a
            else:
                print("Opção inválida. Por favor, digite 's' ou 'n'.")
    elif op == '*':
        return a * b
    elif op == '/':
        d= input('Deseja calcular o primeiro valor dividido pelo segundo? (s/n) Caso não será calculado o inverso: ').strip().lower()
        if b == 0 and a == 0:
            return "Indefinido! Divisão por 0."
        elif d == 's' and b!=0:
            return 0
        elif d == 'n' and a != 0:
            return 0
        while True:
            if d == 's':
                resto = 
            elif d == 'n':
                resto = 
            else:
                print("Opção inválida. Por favor, digite 's' ou 'n'.")
        