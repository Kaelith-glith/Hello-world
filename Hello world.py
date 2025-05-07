def calculadora():
    print("=== CALCULADORA SIMPLES ===")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida.")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida, use apenas números.")
        return

    if escolha == '1':
        resultado = num1 + num2
        operacao = '+'
    elif escolha == '2':
        resultado = num1 - num2
        operacao = '-'
    elif escolha == '3':
        resultado = num1 * num2
        operacao = '*'
    elif escolha == '4':
        if num2 == 0:
            print("Erro: divisão por zero.")
            return
        resultado = num1 / num2
        operacao = '/'

    print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")

calculadora()
