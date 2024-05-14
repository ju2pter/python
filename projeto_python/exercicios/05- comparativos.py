"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')

#OPERADORES LÓGICOS

# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)


# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

'''
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
    '''




#EXERCICIOS

'''
01- Igualdade (==):
Este operador verifica se dois valores são iguais. Retorna True se forem iguais e False caso contrário.

02- Diferença (!=):
Este operador verifica se dois valores são diferentes. Retorna True se forem diferentes e False caso contrário.

03- Maior que (>):
Este operador verifica se o valor à esquerda é maior que o valor à direita. Retorna True se for maior e False caso contrário.

04- Menor que (<):
Este operador verifica se o valor à esquerda é menor que o valor à direita. Retorna True se for menor e False caso contrário.

05- Maior ou igual (>=) e Menor ou igual (<=):
Estes operadores verificam se o valor à esquerda é maior ou igual, ou menor ou igual, respectivamente, ao valor à direita. 
Retornam True se a condição for atendida e False caso contrário.'''








#RESPOSTAS

# Exemplo 1: Igualdade (==)
a = 5
b = 5
if a == b:
    print("a é igual a b")
else:
    print("a não é igual a b")

# Exemplo 2: Diferença (!=)
x = 10
y = 20
if x != y:
    print("x é diferente de y")
else:
    print("x é igual a y")

# Exemplo 3: Maior que (>)
saldo = 1000
limite = 500
if saldo > limite:
    print("Você excedeu o limite de saldo")
else:
    print("Saldo dentro do limite")

# Exemplo 4: Menor que (<)
idade = 18
if idade < 21:
    print("Você é menor de idade nos EUA")
else:
    print("Você é maior de idade nos EUA")

# Exemplo 5: Maior ou igual (>=) e Menor ou igual (<=)
nota = 8
if nota >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

peso = 70
limite_peso = 80
if peso <= limite_peso:
    print("Dentro do limite de peso")
else:
    print("Excedeu o limite de peso")

