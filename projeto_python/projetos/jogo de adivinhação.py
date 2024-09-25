# Importa o módulo 'random' para gerar números aleatórios
import random

# Define uma função chamada 'jogar_adivinhacao'
def jogar_adivinhacao():
    # Gera um número aleatório entre 1 e 100 e o armazena na variável 'numero'
    numero = random.randint(1, 100)
    
    # Inicializa o contador de tentativas com zero
    tentativas = 0

    # Cria um loop infinito para solicitar palpites do usuário até que ele acerte o número
    while True:
        # Solicita ao usuário que adivinhe o número e converte a entrada para um inteiro
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        
        # Incrementa o número de tentativas a cada palpite
        tentativas += 1

        # Verifica se o palpite é menor que o número sorteado
        if palpite < numero:
            # Informa ao usuário que o número sorteado é maior
            print("Mais alto!")
        # Verifica se o palpite é maior que o número sorteado
        elif palpite > numero:
            # Informa ao usuário que o número sorteado é menor
            print("Mais baixo!")
        # Caso o palpite esteja correto
        else:
            # Exibe uma mensagem de sucesso, informando quantas tentativas foram feitas
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            # Encerra o loop após o acerto
            break

# Chama a função 'jogar_adivinhacao' para iniciar o jogo
jogar_adivinhacao()
