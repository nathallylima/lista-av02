def media(lista):
    return sum(lista)/len(lista)

while True:
    try:
        quantidade = int(input('Digite a quantidade de números que deseja adicionar na lista: '))
        numeros = []

        for _ in range(quantidade):
            n = float(input('Digite o número que deseja adicionar: '))
            numeros.append(n)

        resultado = media(numeros)
        print(f'A média dos números digitados é {resultado:.2}')
        break

    except (ValueError, ZeroDivisionError):
        print('Digite um número válido.')

    