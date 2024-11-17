def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1. Sair")
        print("2. Adição")
        print("3. Subtração")
        print("4. Multiplicação")
        print("5. Divisão")

        operacao = input("Digite o número da operação desejada: ")

        if operacao == '1':
            print("Encerrando a calculadora. Até mais!")
            break

        # Verificar se a operação é válida
        if operacao not in ['2', '3', '4', '5']:
            print("Operação inválida. Tente novamente.")
            continue

        # Solicitar os números ao usuário
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        # Realizar a operação e exibir o resultado
        if operacao == '2':
            resultado = numero1 + numero2
            print(f"O resultado de {numero1} + {numero2} é: {resultado}")
        elif operacao == '3':
            resultado = numero1 - numero2
            print(f"O resultado de {numero1} - {numero2} é: {resultado}")
        elif operacao == '4':
            resultado = numero1 * numero2
            print(f"O resultado de {numero1} * {numero2} é: {resultado}")
        elif operacao == '5':
            if numero2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = numero1 / numero2
                print(f"O resultado de {numero1} / {numero2} é: {resultado}")

# Chamar a função para iniciar a calculadora
calculadora()
