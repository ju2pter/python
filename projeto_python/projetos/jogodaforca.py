# Importa o módulo 'random' para realizar a escolha aleatória de uma palavra
import random

# Define uma função chamada 'jogar_forca'
def jogar_forca():
    # Lista de palavras que podem ser escolhidas para o jogo
    palavras = ['python', 'programacao', 'ciencia', 'computador']
    
    # Seleciona aleatoriamente uma palavra da lista
    palavra = random.choice(palavras)
    
    # Cria uma lista de underscores ('_') representando as letras que ainda não foram adivinhadas
    letras_certas = ['_'] * len(palavra)
    
    # Define o número inicial de tentativas (erros permitidos)
    tentativas = 6

    # Loop que continua enquanto houver tentativas e ainda existirem letras para adivinhar
    while tentativas > 0 and '_' in letras_certas:
        # Exibe as letras corretas adivinhadas até o momento, separadas por espaço
        print(' '.join(letras_certas))
        
        # Solicita que o jogador insira uma letra e converte para minúscula
        letra = input('Digite uma letra: ').lower()

        # Verifica se a letra está na palavra sorteada
        if letra in palavra:
            # Se a letra estiver na palavra, percorre cada posição para revelá-la
            for index, char in enumerate(palavra):
                if char == letra:
                    letras_certas[index] = letra
        else:
            # Se a letra não estiver na palavra, reduz o número de tentativas
            tentativas -= 1
            # Informa ao jogador quantas tentativas restam
            print(f'Você errou! Restam {tentativas} tentativas.')

    # Se todas as letras forem descobertas, o jogador vence
    if '_' not in letras_certas:
        print(f'Parabéns! Você acertou: {palavra}')
    else:
        # Caso o número de tentativas se esgote, o jogador perde e a palavra é revelada
        print(f'Você perdeu! A palavra era: {palavra}')

# Chama a função 'jogar_forca' para iniciar o jogo
jogar_forca()
