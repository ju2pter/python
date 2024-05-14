"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')



#EXERCICIOS


'''
01- Divisão por Zero:
Este bloco try/except captura uma exceção que ocorre quando tentamos dividir um número por zero.

02- Conversão de Tipo de Dados:
Este bloco try/except captura uma exceção que ocorre ao tentar converter um valor para um tipo de dados inválido.

03- Acesso a Índices Inválidos:
Este bloco try/except captura uma exceção que ocorre ao tentar acessar um índice inválido em uma lista ou outro objeto indexável.

04- Leitura de Arquivo Inexistente:
Este bloco try/except captura uma exceção que ocorre ao tentar abrir ou ler um arquivo que não existe.

05- Execução de Código Suscetível a Erros:
Este bloco try/except envolve a execução de um código que pode gerar diferentes tipos de exceções, permitindo que o programa continue mesmo se ocorrer um erro.'''








#RESPOSTA


# Exemplo 1: Divisão por Zero
try:
    resultado = 10 / 0  # Tentativa de divisão por zero
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# Exemplo 2: Conversão de Tipo de Dados
try:
    numero = int("abc")  # Tentativa de converter uma string não numérica para inteiro
except ValueError:
    print("Erro: Não é possível converter uma string não numérica para inteiro.")

# Exemplo 3: Acesso a Índices Inválidos
try:
    lista = [1, 2, 3]
    elemento = lista[3]  # Tentativa de acessar um índice que não existe na lista
except IndexError:
    print("Erro: Índice fora do intervalo.")

# Exemplo 4: Leitura de Arquivo Inexistente
try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()  # Tentativa de ler um arquivo que não existe
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")

# Exemplo 5: Execução de Código Suscetível a Erros
try:
    operacao = 10 / 0  # Tentativa de divisão por zero
    print("Resultado:", operacao)  # Essa linha não será executada se ocorrer um erro na linha anterior
except Exception as e:
    print("Ocorreu um erro:", e)


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""