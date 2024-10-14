##Crie uma função que receba uma string e retorne o número de palavras na
##string.

def palavras():
    texto = input('Digite uma frase para verificar quantas palavras possuem: ')

    return len(texto.split())

resultado = palavras()

print(f'Você digitou um total de {resultado} palavras')
