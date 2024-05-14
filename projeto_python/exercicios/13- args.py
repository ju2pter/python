"""
Args é um parâmetro especial que permite que uma função aceite um número variável de argumentos posicionais. 
Ele coleta esses argumentos em uma tupla dentro da função, proporcionando flexibilidade na chamada da função,
e permitindo que ela lide dinamicamente com diferentes quantidades de argumentos.
 É útil para tornar as funções mais genéricas e reutilizáveis em uma variedade de situações.
"""

"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)


#EXERCÍCIOS
'''
Representação Genérica de Argumentos:
O termo "args" é frequentemente usado para representar uma lista de argumentos em uma função, independentemente de sua natureza ou tipo.

Passagem de Argumentos para Funções:
Ao chamar uma função, "args" pode ser usado para indicar os argumentos que estão sendo passados para ela, embora não seja uma sintaxe específica do Python.

Uso em Assinaturas de Funções:
Em documentação ou discussões de código, "args" pode ser usado para indicar que uma função aceita argumentos, mas não especifica o tipo ou a quantidade exata.

Manuseio de Argumentos em Métodos:
Em métodos de classes ou objetos, "args" pode ser usado para representar os argumentos passados ao método durante sua chamada.

Convenção de Nomenclatura:
Embora "args" não tenha um significado específico em Python, é uma convenção comum de nomenclatura para representar argumentos em discussões ou documentações de código.
'''








#RESPOSTAS




# Exemplo 1: Representação Genérica de Argumentos
def exemplo(*args):
    # args pode ser uma tupla contendo todos os argumentos passados para a função
    for arg in args:
        print("Argumento:", arg)

exemplo(1, "dois", True)

# Exemplo 2: Passagem de Argumentos para Funções
def soma(*args):
    # Soma todos os argumentos passados para a função
    return sum(args)

resultado = soma(1, 2, 3, 4, 5)
print("Resultado da soma:", resultado)

# Exemplo 3: Uso em Assinaturas de Funções
def funcao_qualquer(args):
    # Aqui "args" é apenas o nome do parâmetro, pode representar qualquer coisa
    print("Executando função com argumento:", args)

funcao_qualquer("algum argumento")

# Exemplo 4: Manuseio de Argumentos em Métodos
class Exemplo:
    def __init__(self, *args):
        # O método __init__ da classe Exemplo aceita qualquer número de argumentos
        self.args = args

    def mostrar_args(self):
        # Método para exibir os argumentos
        print("Argumentos:", self.args)

objeto = Exemplo(1, "dois", True)
objeto.mostrar_args()

# Exemplo 5: Convenção de Nomenclatura
def calcular_media(*args):
    # Nome da função sugere que ela calcula a média de uma lista de argumentos
    return sum(args) / len(args)

media = calcular_media(10, 20, 30, 40, 50)
print("Média dos números:", media)


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""