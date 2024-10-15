def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Não é possivel dividir um número por zero"

print("\nCALCULADORA\n")

def calculadora():
    while True:
        operacao = int(input('\nEscolha uma operaçao: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n'))

        if operacao == 5:
            print("Encerrando o programa...")
            break
        elif operacao in [1, 2, 3, 4, 5]:
            a = int(input('Digite um número: '))
            b = int(input('Digite outro número: '))

        if operacao == 1:
            print(f'Soma: {soma(a, b)}')
        elif operacao == 2:
            print(f'Subtrcação: {sub(a, b)}')
        elif operacao == 3:
            print(f'Multiplicação: {mult(a, b)}')
        elif operacao == 4:
            print(f'Divisão: {div(a, b)}')
        else:
            print("Opção inválida, digite novamente.")

        if operacao == 5:
            print("Encerrando o programa...")
            break
        
calculadora()
