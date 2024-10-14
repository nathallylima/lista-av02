def fatorial(n):
        if n == 0:
            return 1
        else:
            return n * fatorial(n-1)
while True:
    try:
        n = int(input('Digite um número: '))
        if n < 0:
              print("Número inválido. Digite um número inteiro não negativo.")
        else:
            resultado = fatorial(n)
            print(f'O fatorial de {n} é {resultado}')
    except ValueError:
         print('Digite um número válido')