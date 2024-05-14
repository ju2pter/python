"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('juliana')
saudacao('Maria')
saudacao('Helena')
saudacao()



#EXERCICIOS


'''
01- Definição de Função Simples:
A declaração def é usada para definir uma função em Python. Você pode criar uma função para realizar uma tarefa específica e reutilizá-la sempre que necessário.

02- Função com Parâmetros:
Você pode definir uma função com parâmetros, que são valores que podem ser passados para a função para personalizar seu comportamento.

03- Retorno de Valor:
Uma função pode retornar um valor usando a palavra-chave return. Isso permite que você obtenha um resultado específico do processamento realizado pela função.

04- Função com Argumentos Padrão:
Você pode definir argumentos padrão para uma função, que são usados caso nenhum valor seja fornecido durante a chamada da função.

05- Função com Documentação:
É uma boa prática incluir documentação para suas funções usando docstrings. Isso ajuda a entender o propósito da função e como usá-la.'''







#RESPOSTAS


# Exemplo 1: Definição de Função Simples
def saudacao():
    print("Olá, mundo!")

saudacao()

# Exemplo 2: Função com Parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")

saudacao_personalizada("Alice")

# Exemplo 3: Retorno de Valor
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print("Resultado da soma:", resultado)

# Exemplo 4: Função com Argumentos Padrão
def saudacao_hora(nome, hora="manhã"):
    print(f"Bom {hora}, {nome}!")

saudacao_hora("Pedro")
saudacao_hora("Maria", "tarde")

# Exemplo 5: Função com Documentação
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.

    Parâmetros:
        base (float): O comprimento da base do retângulo.
        altura (float): A altura do retângulo.

    Retorna:
        float: A área do retângulo.
    """
    return base * altura

area = area_retangulo(5, 3)
print("Área do retângulo:", area)


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""
