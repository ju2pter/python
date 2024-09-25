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
