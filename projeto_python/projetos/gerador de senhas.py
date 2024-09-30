"""
# Importa o módulo 'random' para gerar números e caracteres aleatórios
import random

# Importa o módulo 'string', que contém várias constantes de caracteres, como letras e dígitos
import string

# Define uma função chamada 'gerar_senha' que recebe um parâmetro 'tamanho'
def gerar_senha(tamanho):
    # Cria uma string que contém todas as letras (maiúsculas e minúsculas), dígitos e caracteres de pontuação
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera uma senha aleatória do tamanho especificado, escolhendo caracteres aleatórios da string 'caracteres'
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    # Retorna a senha gerada
    return senha

# Solicita ao usuário que insira o tamanho da senha e converte o valor digitado para um número inteiro
tamanho = int(input("Digite o tamanho da senha: "))

# Chama a função 'gerar_senha' passando o tamanho fornecido e armazena o resultado na variável 'senha'
senha = gerar_senha(tamanho)

# Exibe a senha gerada para o usuário
print(f"Senha gerada: {senha}")

"""

#PARA DIFULCULTAR UM POUCO O NÍVEL... CRIE UM GERADOR DE SENHAS ALEATÓRIAS QUE ALÉM DE GERAR AS SENHAS, ARMAZENE-AS EM 
#ALGUM LUGAR

# UM BOM EXEMPLO DE COMO FAZER ISSO É ARMAZENAR AS SENHAS CRIADAS EM UM ARQUIVO DE TEXTO .txt. FICARIA ASSIM:

import random  # importa biblioteca de números e letras aleatórias
import string  # importa caracteres e letras maiúsculas e minúsculas

# Função para gerar a senha aleatória
def gerador_senhas(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation  # adiciona letras, números e caracteres especiais
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))  # gera uma senha aleatória
    return senha  # retorna a senha gerada

# Função para armazenar a senha em um arquivo de texto
def armazenar_senha(senha):
    with open('senhas_geradas.txt', 'a') as arquivo:  # abre o arquivo em modo de adição ('a')
        arquivo.write(senha + '\n')  # escreve a senha no arquivo e adiciona uma nova linha
    print("Senha armazenada com sucesso!")

# Solicita o tamanho da senha ao usuário
tamanho = int(input("Digite o tamanho da sua senha: "))

# Gera a senha com base no tamanho informado
senha = gerador_senhas(tamanho)

# Exibe a senha gerada
print(f"Senha gerada: {senha}")

# Armazena a senha gerada em um arquivo de texto
armazenar_senha(senha)

