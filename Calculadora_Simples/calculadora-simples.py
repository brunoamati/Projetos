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
            d = s_n('Deseja calcular o primeiro valor menos o segundo? (s/n) Caso não será calculado o inverso: ')
            if d == True:
                return a - b
            else:
                return b - a
    elif op == '*':
        return a * b
    elif op == '/':
            try:
                if a == 0 and b == 0:
                    return "Indefinido! Divisão de 0 por 0."
                elif a//b == 0:
                    return 0
                else:
                    d= s_n('Deseja calcular o primeiro valor dividido pelo segundo? (s/n) Caso não será calculado o inverso: ')
                    if d == True:
                            resto = s_n('Deseja saber o resto da divisão?(s/n):')
                            if resto == True:
                                return (f'Divisão: {a // b}\n Resto: {a % b}')
                            else:
                                return a // b
                    else:
                        resto = s_n('Deseja saber o resto da divisão também? (s/n): ')
                        if resto == True:
                            return (f'Divisão: {b // a}\n Resto: {b % a}')
                        else:
                            return b//a
            except ZeroDivisionError:
                return 0      
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
    print("Calculadora Simples".center(30, '-'))
    print("Somente serão realizados cálculos com números inteiros.")
    print("Escolha uma operação para realizar:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    while True:
        op = input("Escolha uma operação (digite o símbolo): ").strip()
        if op in ['+', '-', '*', '/']:
            a = pegarNumero("Digite o primeiro número: ")
            b = pegarNumero("Digite o segundo número: ")
            resultado = calculadora(a, b, op)
            print(f"Resultado: {resultado}")
            break
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")

    if not s_n('\nDeseja realizar outra operação?(s/n):'):
        print('Até mais! Obrigado por usar minha calculadora!')
        break