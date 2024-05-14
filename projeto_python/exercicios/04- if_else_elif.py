
# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')




#EXERCICIOS


'''
01- Verificação de Condição Simples:
Este bloco if/else verifica se uma condição é verdadeira e executa um bloco de código se a condição for verdadeira, e outro bloco de código se a condição for falsa.

02- Verificação de Condição com Elif:
Este bloco if/elif/else verifica várias condições em sequência e executa o bloco de código correspondente à primeira condição verdadeira encontrada.

03- Verificação de Valor de Variável:
Este bloco if/else verifica se o valor de uma variável atende a uma determinada condição e executa o bloco de código correspondente.

04- Verificação de Tamanho de Lista:
Este bloco if/else verifica se o tamanho de uma lista é maior que um determinado valor e executa um bloco de código se a condição for verdadeira, e outro bloco de código se a condição for falsa.

05- Verificação de Tipo de Dados:
Este bloco if/else verifica o tipo de dado de uma variável e executa um bloco de código correspondente com base no tipo de dado.'''








#RESPOSTA

# Exemplo 1: Verificação de Condição Simples
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo 2: Verificação de Condição com Elif
nota = 75
if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
elif nota >= 60:
    print("Nota: D")
else:
    print("Nota: F")

# Exemplo 3: Verificação de Valor de Variável
numero = 10
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Exemplo 4: Verificação de Tamanho de Lista
lista = [1, 2, 3, 4, 5]
if len(lista) > 3:
    print("A lista tem mais de 3 elementos.")
else:
    print("A lista tem 3 elementos ou menos.")

# Exemplo 5: Verificação de Tipo de Dados
valor = 10
if isinstance(valor, int):
    print("O valor é do tipo inteiro.")
elif isinstance(valor, float):
    print("O valor é do tipo float.")
else:
    print("O valor não é um número.")




"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""