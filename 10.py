def palavras():
    texto = input('Digite uma frase para verificar quantas palavras possuem: ')

    return len(texto.split())

resultado = palavras()

print(f'Você digitou um total de {resultado} palavras')
