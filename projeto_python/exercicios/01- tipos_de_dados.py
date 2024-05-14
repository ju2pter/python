# Exemplo de string (str)
mensagem = "Olá, mundo!"  # Aqui estamos atribuindo uma string à variável 'mensagem'
print(mensagem)           # Usamos a função print() para exibir a mensagem na tela
                          # strings são apenas textos entre as aspas, podendo ser a simples '' ou dupla "", e tudo dentro delas se torna texto 

# Exemplo de inteiro (int)
idade = 25                # Aqui estamos atribuindo um valor inteiro à variável 'idade'
print("Minha idade é", idade)  # Usamos a função print() para exibir a idade na tela
                               # Os dados inteiros são apenas números inteiros

# Exemplo de ponto flutuante (float)
peso = 75.5               # Aqui estamos atribuindo um valor de ponto flutuante à variável 'peso'
print("Meu peso é", peso)     # Usamos a função print() para exibir o peso na tela
                              # Os dados do tipo float são apenas números fracionados

# Exemplo de booleano (bool)
# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))


tem_filhos = False        # Aqui estamos atribuindo um valor booleano à variável 'tem_filhos'
if tem_filhos:            # Usamos uma estrutura condicional para verificar se tem_filhos é True
    print("Tenho filhos")  # Dados booleanos são apenas dados verdadeiro ou falso
else:
    print("Não tenho filhos")


#para converte-los usamos o seguinte parametro: ex: print(int('1')) 

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')





#VARIAVEIS

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

# nome_completo = 'Luiz Otávio Miranda'
# soma_dois_mais_dois = 2 + 2
# int_um = bool('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois)

nome = 'juliana'
idade = 17
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)


#EXERCÍCIOS

#TENTE FAZÊ-LOS ANTES DE VER A RESPOSTA
'''
01- Mensagem de Saudação:
Peça ao usuário para inserir seu nome e, em seguida, exiba uma mensagem de saudação usando uma f-string.

02- Calculadora Simples:
Peça ao usuário para inserir dois números e, em seguida, exiba a soma, a subtração, a multiplicação e a divisão desses números.

03- Verdadeiro ou Falso:
Crie uma variável booleana representando se o dia está ensolarado ou não. Em seguida, exiba uma mensagem indicando se é verdadeiro ou falso que o dia está ensolarado.

04- Conversor de Temperatura:
Peça ao usuário para inserir uma temperatura em Celsius e, em seguida, converta-a para Fahrenheit usando a fórmula: Fahrenheit = (Celsius × 9/5) + 32. Exiba o resultado.

05- Calculadora de IMC (Índice de Massa Corporal):
Peça ao usuário para inserir sua altura (em metros) e seu peso (em quilogramas). Em seguida, calcule o IMC usando a fórmula: IMC = peso / altura² e exiba o resultado.
'''



#RESPOSTAS ABAIXO

# Exercício 1: Mensagem de Saudação
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo!")

# Exercício 2: Calculadora Simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

# Exercício 3: Verdadeiro ou Falso
ensolarado = True
print(f"O dia está ensolarado? {ensolarado}")

# Exercício 4: Conversor de Temperatura
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

# Exercício 5: Calculadora de IMC (Índice de Massa Corporal)
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")



"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""