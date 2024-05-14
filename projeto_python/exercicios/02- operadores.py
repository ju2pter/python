adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10 #O * É usado para multiplicação
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float #O / é usado para divisão 
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)



#EXERCICIOS

'''
01- Calculadora de Média:
Peça ao usuário para inserir três notas e calcule a média aritmética dessas notas.

02- Calculadora de Área do Círculo:
Peça ao usuário para inserir o raio de um círculo e calcule a área usando a fórmula: área = π * raio². Use o valor de π como 3.14159.

03- Calculadora de Desconto:
Peça ao usuário para inserir o preço original de um produto e o percentual de desconto. Calcule o preço final após o desconto.

04- Conversor de Moeda:
Peça ao usuário para inserir um valor em reais (R$) e o valor do dólar (US$). Converta o valor de reais para dólares.

05- Calculadora de Juros Simples:
Peça ao usuário para inserir o valor do principal, a taxa de juros e o tempo em anos. 
Calcule o montante final usando a fórmula: montante = principal * (1 + taxa_de_juros * tempo).'''









#RESPOSTAS

# Exercício 1: Calculadora de Média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")

# Exercício 2: Calculadora de Área do Círculo
import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"A área do círculo é: {area:.2f}")

# Exercício 3: Calculadora de Desconto
preco_original = float(input("Digite o preço original do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
preco_final = preco_original - (preco_original * percentual_desconto / 100)
print(f"O preço final após o desconto é: R${preco_final:.2f}")

# Exercício 4: Conversor de Moeda
valor_reais = float(input("Digite o valor em reais (R$): "))
valor_dolar = float(input("Digite o valor do dólar (US$): "))
valor_convertido = valor_reais / valor_dolar
print(f"O valor convertido para dólares é: US${valor_convertido:.2f}")

# Exercício 5: Calculadora de Juros Simples
principal = float(input("Digite o valor do principal: "))
taxa_juros = float(input("Digite a taxa de juros (em decimal): "))
tempo_anos = float(input("Digite o tempo em anos: "))
montante = principal * (1 + taxa_juros * tempo_anos)
print(f"O montante final após juros simples é: R${montante:.2f}")

"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""