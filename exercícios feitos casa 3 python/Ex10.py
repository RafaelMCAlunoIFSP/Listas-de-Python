while True:
    operacao = input("Digite uma operação (+, -, *, /) ou 'S' para sair: ")

    if (operacao == 'S'):
        print("Fim do programa.")
        break

    elif operacao in ['+', '-', '*', '/']:

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = a + b
        elif operacao == '-':
            resultado = a - b
        elif operacao == '*':
            resultado = a * b
        elif operacao == '/':
            if b != 0:
                resultado = a / b
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue
        
        print(f"O resultado de {a} {operacao} {b} é: {resultado}\n")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.\n")