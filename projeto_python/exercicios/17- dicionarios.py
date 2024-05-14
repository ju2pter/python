# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)

#EXERCÍCIOS
"""
01- Exercício de Acesso e Modificação:
Crie um dicionário chamado pessoa que represente as informações de uma pessoa, incluindo chaves como "nome", "idade" e "cidade". Acesse e modifique os valores associados a essas chaves.

02- Exercício de Iteração:
Crie um dicionário chamado estoque que represente os itens disponíveis em uma loja, com chaves sendo os nomes dos produtos e valores sendo as quantidades disponíveis. Itere sobre o dicionário para imprimir os itens e suas respectivas quantidades.

03- Exercício de Mesclagem de Dicionários:
Crie dois dicionários, dic1 e dic2, com chaves e valores diferentes. Mescle os dois dicionários em um terceiro dicionário chamado dic_merged.

04- Exercício de Remoção de Chaves:
Crie um dicionário chamado notas que represente as notas dos alunos em uma disciplina, com chaves sendo os nomes dos alunos e valores sendo suas respectivas notas. Remova um aluno específico do dicionário.

05- Exercício de Verificação de Chave:
Crie um dicionário chamado agenda que represente os contatos de uma pessoa, com chaves sendo os nomes das pessoas e valores sendo seus números de telefone. Verifique se um determinado nome está presente no dicionário."""




#RESPOSTAS




# Exercício 1: Acesso e Modificação
# Definindo um dicionário com informações de uma pessoa
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando e modificando valores no dicionário
print("Nome:", pessoa["nome"])
pessoa["idade"] = 35
print("Idade atualizada:", pessoa["idade"])

# Exercício 2: Iteração
# Definindo um dicionário com estoque de uma loja
estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

# Iterando sobre o dicionário e imprimindo os itens e suas quantidades
for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} unidades")

# Exercício 3: Mesclagem de Dicionários
# Definindo dois dicionários para mesclar
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}

# Mesclando os dicionários em um terceiro dicionário
dic_merged = {**dic1, **dic2}
print("Dicionário Mesclado:", dic_merged)

# Exercício 4: Remoção de Chaves
# Definindo um dicionário com notas de alunos
notas = {"João": 8, "Maria": 7, "Carlos": 6}

# Removendo um aluno específico do dicionário
del notas["Maria"]
print("Notas após remoção:", notas)

# Exercício 5: Verificação de Chave
# Definindo um dicionário com contatos de uma agenda
agenda = {"João": "1234-5678", "Maria": "9876-5432", "Carlos": "8765-4321"}

# Verificando se um nome está presente no dicionário
nome = "Maria"
if nome in agenda:
    print(f"{nome} está na agenda.")
else:
    print(f"{nome} não está na agenda.")


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""