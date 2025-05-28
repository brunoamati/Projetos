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
            try:
                if a == 0 and b == 0:
                    return "Indefinido! Divisão de 0 por 0."
                elif a//b == 0:
                    return 0
                elif a//b != 0 and b//a != 0:
                    while True: 
                        d= input('Deseja calcular o primeiro valor dividido pelo segundo? (s/n) Caso não será calculado o inverso: ').strip().lower()
                        if d == 's':
                            resto = input('Deseja saber o resto da divisão também? (s/n): ').strip().lower()
                            while True:
                                    if resto == 's':
                                        return [a // b, a % b]
                                    elif resto == 'n':
                                        return a // b
                                    else:
                                        print("Opção inválida. Por favor, digite 's' ou 'n'.")
                        elif d == 'n':
                            resto = input('Deseja saber o resto da divisão também? (s/n): ').strip().lower()
                            while True:
                                if resto == 's':
                                    return [b // a, b % a]
                                elif resto == 'n':
                                    return b // a
                                else:
                                    print("Opção inválida. Por favor, digite 's' ou 'n'.")
                        else:
                            print("Opção inválida. Por favor, digite 's' ou 'n'.")
            except ZeroDivisionError:
                return 0      
    else:
        return "Operação inválida. Por favor, escolha uma operação válida."
    
loop = 1
while loop == 1:
    print("Calculadora Simples".center(30, '-'))
    print("Somente serão realizados cálculos com números inteiros.")
    print("Escolha uma operação para realizar:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    op = input("Escolha uma operação (digite o símbolo): ").strip()

    if op in ['+', '-', '*', '/']:
        a = pegarNumero("Digite o primeiro número: ")
        b = pegarNumero("Digite o segundo número: ")
        resultado = calculadora(a, b, op)
        print(f"Resultado: {resultado}")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

    while True:
        continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
        if continuar == 'n':
            loop = 0
            print("Obrigado por usar a calculadora!")
            break
        elif continuar == 's':
            loop = 1
            print("Reiniciando a calculadora...")
            break
        else:
            print("Opção inválida. Por favor, digite 's' ou 'n'.")
        