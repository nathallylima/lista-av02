def contagem(palavra):
    vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú']
    contagem_vogais = 0

    for letra in palavra.lower():
        if letra in vogais:
            contagem_vogais += 1
    
    return contagem_vogais



palavra = input('Digite uma palavra: ')
resultado = contagem(palavra)
print(f'O número de vogais na palavra {palavra} é {resultado}')