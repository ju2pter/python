"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'juliana',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))





#EXERCICIOS

'''
01- Conversão de Sequência para Lista:
A função list() pode ser usada para converter uma sequência (como uma string, tupla ou conjunto) em uma lista. Isso permite que você acesse os elementos da sequência individualmente e os manipule conforme necessário.

02- Criação de uma Lista Vazia:
Se você chamar list() sem argumentos, ela retornará uma lista vazia. Isso é útil quando você precisa criar uma lista para armazenar valores posteriormente.

03- Cópia de Outra Lista:
Você pode usar list() para criar uma cópia de outra lista. Isso é útil quando você precisa modificar uma lista sem alterar a original.

04- Separação de Strings:
Ao passar uma string para list(), ela será convertida em uma lista de caracteres, onde cada caractere da string se torna um elemento da lista.

05- Conversão de Objeto Iterável:
list() pode ser usado para converter um objeto iterável em uma lista. Isso é útil quando você precisa trabalhar com os elementos do objeto de forma mais flexível.'''









#RESPOSTA




# Exemplo 1: Conversão de Sequência para Lista
# Convertendo uma string em uma lista de caracteres
string = "Python"
lista_caracteres = list(string)
print(lista_caracteres)

# Exemplo 2: Criação de uma Lista Vazia
lista_vazia = list()
print(lista_vazia)

# Exemplo 3: Cópia de Outra Lista
lista_original = [1, 2, 3, 4, 5]
copia_lista = list(lista_original)
print(copia_lista)

# Exemplo 4: Separação de Strings
# Convertendo uma frase em uma lista de palavras
frase = "Python é uma linguagem de programação"
lista_palavras = list(frase.split())
print(lista_palavras)

# Exemplo 5: Conversão de Objeto Iterável
# Convertendo uma tupla em uma lista
tupla = (1, 2, 3, 4, 5)
lista_tupla = list(tupla)
print(lista_tupla)


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""

