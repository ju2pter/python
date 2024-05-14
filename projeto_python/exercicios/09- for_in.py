
'''O comando for em Python é uma estrutura de controle que permite iterar sobre uma sequência de elementos, como:
 listas, tuplas, strings, dicionários e conjuntos. 
Ele é especialmente útil quando precisamos percorrer cada elemento de uma coleção e realizar alguma operação para cada um deles. '''


# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')





#EXERCICIOS

'''
01- Iteração sobre uma Lista:
O for ... in é frequentemente usado para iterar sobre os elementos de uma lista, permitindo que você execute uma determinada ação para cada elemento.

02- Iteração sobre uma String:
Você pode usar o for ... in para iterar sobre os caracteres de uma string, permitindo que você processe cada caractere individualmente.

03- Iteração sobre um Dicionário:
O for ... in também pode ser usado para iterar sobre os itens de um dicionário, permitindo que você acesse tanto as chaves quanto os valores.

04- Iteração sobre um Intervalo de Números:
O comando range() pode ser combinado com o for ... in para iterar sobre uma sequência de números, facilitando a execução de uma determinada operação um número específico de vezes.

05- Iteração sobre um Conjunto:
O for ... in pode ser usado para iterar sobre os elementos de um conjunto, garantindo que cada elemento seja acessado apenas uma vez.'''












#RESPOSTAS

# Exemplo 1: Iteração sobre uma Lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Exemplo 2: Iteração sobre uma String
palavra = "Python"
for letra in palavra:
    print(letra)

# Exemplo 3: Iteração sobre um Dicionário
dicionario = {"a": 1, "b": 2, "c": 3}
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

# Exemplo 4: Iteração sobre um Intervalo de Números
for i in range(5):
    print(i)

# Exemplo 5: Iteração sobre um Conjunto
conjunto = {1, 2, 3, 4, 5}
for elemento in conjunto:
    print(elemento)

"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""