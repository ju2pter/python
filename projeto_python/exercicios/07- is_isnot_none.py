"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')




#EXERCICIOS




'''
01- Verificação de Identidade (is):
O operador is verifica se dois objetos têm a mesma identidade. Em outras palavras, ele verifica se ambos os objetos referenciam o mesmo local na memória.

02- Verificação de Não-Identidade (is not):
O operador is not verifica se dois objetos não têm a mesma identidade.

03- Teste de Nulo (None):
Em Python, None é um tipo de dado especial que representa a ausência de valor. É comumente usado para inicializar variáveis ou
para indicar que uma função não retorna nenhum valor.'''














#RESPOSTAS


# Exemplo 1: Verificação de Identidade (is)
a = [1, 2, 3]
b = [1, 2, 3]
if a is b:
    print("a e b têm a mesma identidade")
else:
    print("a e b não têm a mesma identidade")

# Exemplo 2: Verificação de Não-Identidade (is not)
x = [4, 5, 6]
y = [4, 5, 6]
if x is not y:
    print("x e y não têm a mesma identidade")
else:
    print("x e y têm a mesma identidade")

# Exemplo 3: Teste de Nulo (None)
valor = None
if valor is None:
    print("A variável valor não possui valor atribuído")
else:
    print("A variável valor possui um valor atribuído")

# Exemplo 4: Teste de Igualdade com None
nome = None
if nome is None:
    print("O nome não foi especificado")
else:
    print("O nome é:", nome)

# Exemplo 5: Verificação de Tipo de Dados com None
def saudacao(nome=None):
    if nome is not None:
        print("Olá,", nome)
    else:
        print("Olá, visitante")

saudacao("João")
saudacao()



"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""