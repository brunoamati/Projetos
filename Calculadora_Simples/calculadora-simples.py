import os


def pegarNumero(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


def calculadora(a, b, op):

    if op == '+':
        return f'Soma dos valores: {a + b}'
    elif op == '-':
        d = s_n('Deseja calcular o primeiro valor menos o segundo? (s/n) Caso não será calculado o inverso: ')
        if not d:
            a, b = b, a
        return f'Subtração dos valores: {a - b}'
    elif op == '*':
        return f'Multiplicação dos valores: {a * b}'
    elif op == '/':
        try:
            if a == 0 and b == 0:
                return "Indefinido! Divisão de 0 por 0."
            else:
                d = s_n('Deseja calcular o primeiro valor dividido pelo segundo? (s/n) Caso não será calculado o inverso: ')
                if not d:
                    a, b = b, a
                return f'Divisão inteira: {a // b}\nDivisão real: {round(a/b, 2)}\nResto: {a % b}'
        except ZeroDivisionError:
            return 'ERRO! Divisão com 0, impossivel determinar o valor'
    elif op == '**':
        d = s_n('Deseja calcular o primeiro valor potencializado pelo o segundo? (s/n) Caso não será calculado o inverso: ')
        if not d:
            a, b = b, a
        return f'Potencialização dos valores: {a ** b}'
    else:
        return "Operação inválida. Por favor, escolha uma operação válida."


def s_n(msg):
    while True:
        resp = input(msg).strip().lower()
        if resp == 's':
            return True
        if resp == 'n':
            return False
        print("Responda apenas com 's' ou 'n'.")



while True:
    print("Escolha uma operação para realizar:\n1. Adição (+)\n2. Subtração (-)\n3. Multiplicação (*)\n4. Divisão (/)\n5. Potencialização(**)")

    while True:
        print("Calculadora Simples".center(30, '-'))
        print("Somente serão realizados cálculos com números inteiros.")
        op = input("Escolha uma operação (digite o símbolo): ").strip()
        if op in ['+', '-', '*', '/', '**']:
            a = pegarNumero("Digite o primeiro número: ")
            b = pegarNumero("Digite o segundo número: ")
            resultado = calculadora(a, b, op)
            print(f"Resultado: \n{resultado}")
            break
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")

    if not s_n('\nDeseja realizar outra operação?(s/n):'):
        print('Até mais! Obrigado por usar minha calculadora!')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')