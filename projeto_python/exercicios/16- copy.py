

#EXERCÍCIOS




"""
Exercício de Cópia de Dicionários:
Crie um dicionário chamado original com algumas chaves e valores. Faça uma cópia desse dicionário utilizando o método copy() e modifique a cópia. Verifique se as alterações na cópia afetam o dicionário original.

Exercício de Cópia de Listas:
Crie uma lista chamada lista_original com alguns elementos. Faça uma cópia dessa lista utilizando o método copy() e modifique a cópia. Verifique se as alterações na cópia afetam a lista original.

Exercício de Cópia Profunda de Dicionários:
Crie um dicionário chamado dic_original que contenha outro dicionário como valor de uma de suas chaves. Faça uma cópia profunda desse dicionário utilizando a função deepcopy() do módulo copy e modifique a cópia. Verifique se as alterações na cópia afetam o dicionário original.

Exercício de Cópia Profunda de Listas:
Crie uma lista chamada lista_principal que contenha outras listas como elementos. Faça uma cópia profunda dessa lista utilizando a função deepcopy() do módulo copy e modifique a cópia. Verifique se as alterações na cópia afetam a lista original.

Exercício de Cópia de Objetos:
Crie um objeto chamado objeto_original de uma classe customizada. Faça uma cópia desse objeto utilizando o método copy() e modifique a cópia. Verifique se as alterações na cópia afetam o objeto original."""




#RESPOSTAS




import copy

# Exercício 1: Cópia de Dicionários
# Criando um dicionário original
original = {"a": 1, "b": 2}

# Fazendo uma cópia do dicionário
copia = original.copy()

# Modificando a cópia
copia["c"] = 3

# Verificando se as alterações na cópia afetam o dicionário original
print("Dicionário Original:", original)
print("Cópia Modificada:", copia)

# Exercício 2: Cópia de Listas
# Criando uma lista original
lista_original = [1, 2, 3]

# Fazendo uma cópia da lista
copia_lista = lista_original.copy()

# Modificando a cópia
copia_lista.append(4)

# Verificando se as alterações na cópia afetam a lista original
print("Lista Original:", lista_original)
print("Cópia Modificada:", copia_lista)

# Exercício 3: Cópia Profunda de Dicionários
# Criando um dicionário com outro dicionário como valor
dic_original = {"a": {"x": 1, "y": 2}}

# Fazendo uma cópia profunda do dicionário
copia_profunda = copy.deepcopy(dic_original)

# Modificando a cópia
copia_profunda["a"]["z"] = 3

# Verificando se as alterações na cópia afetam o dicionário original
print("Dicionário Original:", dic_original)
print("Cópia Profunda Modificada:", copia_profunda)

# Exercício 4: Cópia Profunda de Listas
# Criando uma lista com outras listas como elementos
lista_principal = [[1, 2], [3, 4]]

# Fazendo uma cópia profunda da lista
copia_profunda_lista = copy.deepcopy(lista_principal)

# Modificando a cópia
copia_profunda_lista[0].append(5)

# Verificando se as alterações na cópia afetam a lista original
print("Lista Original:", lista_principal)
print("Cópia Profunda Modificada:", copia_profunda_lista)

# Exercício 5: Cópia de Objetos
# Definindo uma classe customizada
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Criando um objeto original
objeto_original = Pessoa("João")

# Fazendo uma cópia do objeto
copia_objeto = copy.copy(objeto_original)

# Modificando a cópia
copia_objeto.nome = "Maria"

# Verificando se as alterações na cópia afetam o objeto original
print("Objeto Original:", objeto_original.nome)
print("Cópia Modificada:", copia_objeto.nome)



"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""