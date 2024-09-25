import requests

def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    resposta = requests.get(url).json()
    return resposta['rates'][moeda_destino]

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    return valor * taxa

valor = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (ex: USD): ").upper()
moeda_destino = input("Digite a moeda de destino (ex: EUR): ").upper()

resultado = converter_moeda(valor, moeda_origem, moeda_destino)
print(f"{valor} {moeda_origem} equivale a {resultado} {moeda_destino}")



import requests  # Importa o módulo requests para fazer requisições HTTP, que são usadas para obter dados de uma API

# Função que obtém a taxa de câmbio entre duas moedas usando uma API de taxas de câmbio
def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    # Cria a URL da API com base na moeda de origem
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    
    # Faz uma requisição GET para a API e transforma a resposta em um dicionário JSON
    resposta = requests.get(url).json()
    
    # Retorna a taxa de câmbio da moeda de destino a partir da resposta da API
    return resposta['rates'][moeda_destino]

# Função que converte um valor de uma moeda para outra
def converter_moeda(valor, moeda_origem, moeda_destino):
    # Obtém a taxa de câmbio entre a moeda de origem e a moeda de destino
    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    
    # Retorna o valor convertido multiplicando o valor original pela taxa de câmbio
    return valor * taxa

# Solicita ao usuário que insira o valor que deseja converter
valor = float(input("Digite o valor a ser convertido: "))

# Solicita ao usuário que insira a moeda de origem e transforma o código em maiúsculas para consistência
moeda_origem = input("Digite a moeda de origem (ex: USD): ").upper()

# Solicita ao usuário que insira a moeda de destino e também transforma o código em maiúsculas
moeda_destino = input("Digite a moeda de destino (ex: EUR): ").upper()

# Converte o valor da moeda de origem para a moeda de destino
resultado = converter_moeda(valor, moeda_origem, moeda_destino)

# Exibe o resultado da conversão
print(f"{valor} {moeda_origem} equivale a {resultado} {moeda_destino}")
