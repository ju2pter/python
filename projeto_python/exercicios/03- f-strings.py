# Exemplo de string (str) usando f-string
nome = "rafaela"  
mensagem = f"Olá, {nome}!"  # Aqui usamos uma f-string para incluir a variável 'nome' na mensagem
print(mensagem)  # Usamos a função print() para exibir a mensagem na tela

# Exemplo de inteiro (int) usando f-string
idade = 30  
mensagem_idade = f"Eu tenho {idade} anos."  # Usamos uma f-string para incluir a variável 'idade' na mensagem
print(mensagem_idade)  # Usamos a função print() para exibir a idade na tela

# Exemplo de ponto flutuante (float) usando f-string
altura = 1.75  
mensagem_altura = f"Minha altura é {altura} metros."  # Usamos uma f-string para incluir a variável 'altura' na mensagem
print(mensagem_altura)  # Usamos a função print() para exibir a altura na tela

# Exemplo de booleano (bool) usando f-string
tem_cachorro = True  
mensagem_cachorro = f"Eu tenho cachorro? {tem_cachorro}"  # Usamos uma f-string para incluir a variável 'tem_cachorro' na mensagem
print(mensagem_cachorro)  # Usamos a função print() para exibir se tem cachorro na tela

# Exemplo de operação matemática em uma f-string
numero1 = 10
numero2 = 5
soma = numero1 + numero2
mensagem_soma = f"A soma de {numero1} e {numero2} é {soma}."  # Aqui usamos uma f-string para incluir o resultado da soma de 'numero1' e 'numero2' na mensagem
print(mensagem_soma)  # Usamos a função print() para exibir a soma na tela



"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])


"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'juliana'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))





#EXERCICIOS 

'''
01- Mensagem de Boas-Vindas:
Solicite ao usuário que insira seu nome e exiba uma mensagem de boas-vindas personalizada utilizando uma f-string.

02- Calculadora de Média:
Solicite ao usuário que insira duas notas e calcule a média entre elas. Em seguida, exiba o resultado utilizando uma f-string.

03- Conversor de Temperatura:
Solicite ao usuário que insira uma temperatura em Celsius e converta-a para Fahrenheit utilizando a fórmula adequada. Exiba o resultado formatado com uma f-string.

04- Informações de Produto:
Defina o nome, o preço unitário e a quantidade de um produto. Em seguida, exiba uma mensagem que inclua todas essas informações e o total de vendas utilizando uma f-string.

05- Tabela de Multiplicação:
Peça ao usuário que insira um número e, em seguida, exiba a sua tabuada de multiplicação até 10 utilizando f-strings para formatar cada linha da tabela.'''











#RESPOSTAS

# nome = input('Qual o seu nome? ') O INPUT É USADO PRA COLETAR DADOS DO USUÁRIO
# print(f'O seu nome é {nome}')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')


# Exercício 1: Mensagem de Boas-Vindas
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao nosso programa.")

# Exercício 2: Calculadora de Média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média das notas é: {media:.2f}")

# Exercício 3: Conversor de Temperatura
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

# Exercício 4: Informações de Produto
produto = "Camiseta"
preco = 29.99
quantidade = 3
print(f"Produto: {produto}, Preço unitário: R${preco:.2f}, Quantidade: {quantidade}, Total: R${preco * quantidade:.2f}")

# Exercício 5: Tabela de Multiplicação
numero = int(input("Digite um número: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""

"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)