"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


#EXERCÍCIOS

"""
01-Exercício de Contador:
Escreva uma função contador que retorna uma função interna. Essa função interna deve manter o estado de uma contagem e incrementar esse estado a cada chamada.

02- Exercício de Cache de Resultados:
Escreva uma função memoization que recebe uma função como argumento e retorna uma versão memoizada dessa função. A função memoizada deve armazenar os resultados computados anteriormente em um dicionário e retornar o resultado armazenado caso os mesmos argumentos sejam fornecidos novamente.

03- Exercício de Configuração Dinâmica:
Escreva uma função criar_calculadora que recebe uma string representando uma operação matemática ("soma", "subtracao", "multiplicacao" ou "divisao") e retorna uma função que realiza a operação especificada com dois números.

04- Exercício de Função Geradora:
Escreva uma função criar_contador que recebe um número inicial como argumento e retorna uma função interna. Essa função interna deve retornar o próximo número na sequência a cada chamada."""






#RESPOSTAS




# Exercício 1: Incremento Dinâmico
def criar_incrementador(incremento):
    def incrementar(numero):
        return numero + incremento
    return incrementar

# Exercício 2: Contador
def contador():
    contagem = 0
    def incrementar_contador():
        nonlocal contagem
        contagem += 1
        return contagem
    return incrementar_contador

# Exercício 3: Cache de Resultados
def memoization(funcao):
    cache = {}
    def memoizada(*args):
        if args not in cache:
            cache[args] = funcao(*args)
        return cache[args]
    return memoizada

# Exercício 4: Configuração Dinâmica
def criar_calculadora(operacao):
    def calcular(a, b):
        if operacao == "soma":
            return a + b
        elif operacao == "subtracao":
            return a - b
        elif operacao == "multiplicacao":
            return a * b
        elif operacao == "divisao":
            return a / b
    return calcular

# Exercício 5: Função Geradora
def criar_contador(inicio):
    contagem = inicio
    def proximo_numero():
        nonlocal contagem
        contagem += 1
        return contagem
    return proximo_numero


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""