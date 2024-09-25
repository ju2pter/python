
import math  # Importa o módulo math, que contém funções matemáticas como seno e cosseno

# Função que implementa uma calculadora com várias operações, incluindo operações aritméticas e trigonométricas
def calculadora():
    # Exibe as opções de operação disponíveis para o usuário
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Seno")
    print("6. Cosseno")

    # Solicita ao usuário que escolha uma operação
    escolha = input("Digite o número da operação desejada (1/2/3/4/5/6): ")

    # Caso o usuário escolha seno (5) ou cosseno (6), a operação será feita sobre um único número
    if escolha in ['5', '6']:
        num = float(input("Digite o número: "))  # Solicita um número para calcular seno ou cosseno
        if escolha == '5':
            print(f"Seno de {num} é {math.sin(num)}")  # Calcula e exibe o seno do número
        else:
            print(f"Cosseno de {num} é {math.cos(num)}")  # Calcula e exibe o cosseno do número
    else:
        # Para operações aritméticas, solicita dois números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação escolhida e exibe o resultado
        if escolha == '1':
            print(f"{num1} + {num2} = {num1 + num2}")  # Soma
        elif escolha == '2':
            print(f"{num1} - {num2} = {num1 - num2}")  # Subtração
        elif escolha == '3':
            print(f"{num1} * {num2} = {num1 * num2}")  # Multiplicação
        elif escolha == '4':
            if num2 != 0:  # Verifica se o divisor não é zero
                print(f"{num1} / {num2} = {num1 / num2}")  # Divisão
            else:
                print("Erro: divisão por zero não é permitida.")  # Exibe erro se o divisor for zero

# Chama a função calculadora para que o usuário possa interagir
calculadora()
1