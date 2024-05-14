"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')




#EXERCICIOS

'''
1- Execução de um Loop até uma Condição ser Satisfeita:
O loop while executa um bloco de código repetidamente enquanto uma condição especificada for verdadeira. 
O break é usado para sair do loop antes que a condição se torne falsa.

02- Loop Infinito com Condição de Saída:
Um loop while pode ser usado para criar um loop infinito, que só é interrompido quando uma condição específica é atendida dentro do loop.

03- Contagem Regressiva:
O loop while pode ser usado para criar uma contagem regressiva a partir de um número especificado até zero.

04- Processamento de Entrada do Usuário:
Um loop while pode ser usado para continuar solicitando entrada do usuário até que uma condição específica seja atendida.

05- Loop com Controle de Erros:
Um loop while pode ser usado para continuar executando um bloco de código até que uma entrada do usuário seja válida 
ou até que um erro específico ocorra.'''






#RESPOSTAS




# Exemplo 1: Execução de um Loop até uma Condição ser Satisfeita
contador = 0
while True:
    print("Contador:", contador)
    contador += 1
    if contador >= 5:
        break

# Exemplo 2: Loop Infinito com Condição de Saída
numero = 1
while True:
    print("Número:", numero)
    numero += 1
    if numero > 10:
        break

# Exemplo 3: Contagem Regressiva
contador = 10
while contador >= 0:
    print("Contagem regressiva:", contador)
    contador -= 1

# Exemplo 4: Processamento de Entrada do Usuário
while True:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() == 'n':
        print("Saindo do programa...")
        break
    elif resposta.lower() == 's':
        print("Continuando...")
    else:
        print("Resposta inválida. Por favor, responda 's' para sim ou 'n' para não.")

# Exemplo 5: Loop com Controle de Erros
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print("Número digitado:", numero)
        break  # Saia do loop se a entrada for válida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")



"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""