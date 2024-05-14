
"""
Retorno de valores das funções (return)
A função return em Python serve para produzir um resultado a partir da execução de uma função e retorná-lo para quem a chamou. 
Ela também encerra a execução da função. O return pode ser usado para retornar valores simples ou múltiplos, 
e é frequentemente combinado com instruções condicionais para determinar o valor a ser retornado com base em determinadas condições. Em essência,
 o return é essencial para permitir que as funções em Python forneçam resultados úteis que podem ser utilizados em outras partes do programa.
"""


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))





#EXERCICIOS
'''
01- Retorno de Valor Simples:
A instrução return é usada para retornar um valor de uma função. Isso permite que a função produza um resultado que pode ser usado em outras partes do programa.

02- Função sem Valor de Retorno:
Se uma função não especificar um valor de retorno, ela retornará None implicitamente. Isso indica que a função não produz um resultado específico.

03- Múltiplos Valores de Retorno:
Você pode retornar múltiplos valores de uma função separando-os por vírgula. Isso é útil quando você precisa retornar várias informações de uma vez.

04- Uso de Condição para Retorno:
Voce pode usar a instrução return com uma condição para retornar um valor com base em uma expressão condicional.

05- Encerramento Antecipado da Função:
O uso de return pode ser combinado com outras estruturas de controle, como if, para encerrar prematuramente a execução de uma função se uma condição específica for atendida.'''








#RESPOSTAS



# Exemplo 1: Retorno de Valor Simples
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print("Resultado da soma:", resultado)

# Exemplo 2: Função sem Valor de Retorno
def imprimir_mensagem():
    print("Esta é uma mensagem de exemplo.")

retorno = imprimir_mensagem()
print("Retorno da função:", retorno)

# Exemplo 3: Múltiplos Valores de Retorno
def quadrado_e_cubo(numero):
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo

resultados = quadrado_e_cubo(4)
print("Quadrado:", resultados[0])
print("Cubo:", resultados[1])

# Exemplo 4: Uso de Condição para Retorno
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

resultado = par_ou_impar(7)
print("O número é", resultado)

# Exemplo 5: Encerramento Antecipado da Função
def verificar_positivo(numero):
    if numero > 0:
        return "positivo"
    return "não positivo"  # Retorna implicitamente None se a condição não for atendida

resultado = verificar_positivo(-5)
print("O número é", resultado)


"""lembre-se de comentar os blocos de código que você não for executar primeiro,
pois se não todos vão ser executados de uma vez"""