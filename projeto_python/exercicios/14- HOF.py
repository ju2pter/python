"""
as Higher-Order Functions (HOFs) em Python são funções que tratam outras funções como argumentos e/ou retornam outras funções como resultados. 
Elas são úteis para tornar o código mais modular e reutilizável, encapsular comportamentos específicos, compor funções, 
e promover um estilo de programação declarativa. As HOFs são uma parte importante da programação funcional em Python, 
e são comumente usadas com funções como map(), filter(), reduce(), sorted(), entre outras. Elas ajudam a escrever código mais limpo, 
conciso e eficiente.
"""

"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)






#EXERCÍCIOS

"""
01- Exercício de Soma de Números:
Escreva uma função chamada soma que recebe dois números como argumentos e retorna a soma deles.

02- Exercício de Verificação de Paridade:
Escreva uma função chamada verificar_paridade que recebe um número como argumento e retorna "par" se o número for par e "ímpar" se o número for ímpar.

03- Exercício de Contagem de Vogais:
Escreva uma função chamada contar_vogais que recebe uma string como argumento e retorna o número de vogais na string.

04- Exercício de Inversão de String:
Escreva uma função chamada inverter_string que recebe uma string como argumento e retorna a string invertida.

05- Exercício de Verificação de Palíndromo:
Escreva uma função chamada verificar_palindromo que recebe uma string como argumento e retorna True se a string for um palíndromo (ou seja, se ela for igual quando lida de trás para frente), e False caso contrário.
"""






#RESPOSTAS





#Exercício de Soma de Números:

def soma(a, b):
    """
    Função para calcular a soma de dois números.

    Parâmetros:
        a (int ou float): O primeiro número.
        b (int ou float): O segundo número.

    Retorna:
        int ou float: A soma de a e b.
    """
    return a + b
#Exercício de Verificação de Paridade:

def verificar_paridade(numero):
    """
    Função para verificar a paridade de um número.

    Parâmetros:
        numero (int): O número a ser verificado.

    Retorna:
        str: "par" se o número for par, "ímpar" caso contrário.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
#Exercício de Contagem de Vogais:

def contar_vogais(texto):
    """
    Função para contar o número de vogais em uma string.

    Parâmetros:
        texto (str): A string a ser analisada.

    Retorna:
        int: O número de vogais na string.
    """
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador
#Exercício de Inversão de String:

def inverter_string(texto):
    """
    Função para inverter uma string.

    Parâmetros:
        texto (str): A string a ser invertida.

    Retorna:
        str: A string invertida.
    """
    return texto[::-1]
# Exercício de Verificação de Palíndromo:

def verificar_palindromo(texto):
    """
    Função para verificar se uma string é um palíndromo.

    Parâmetros:
        texto (str): A string a ser verificada.

    Retorna:
        bool: True se a string for um palíndromo, False caso contrário.
    """
    texto = texto.lower()
    texto = texto.replace(" ", "")  # Remover espaços
    return texto == texto[::-1]

"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""