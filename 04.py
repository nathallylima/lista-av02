def calcular(numero1, numero2, operacao):
    if operacao == 1:
        return numero1 + numero2
    elif operacao == 2:
        return numero1 - numero2
    elif operacao == 3:
        return numero1 * numero2
    elif operacao == 4:
        try:
            return numero1 / numero2
        except ZeroDivisionError:
            return 'Não é possível dividir um número por zero'
        
print('\nCALCULADORA\n')

while True:
    operacao = int(input('\nEscolha uma operação: \n [1] Somar \n [2] Subtrair \n [3] Multiplicar \n [4] Dividir \n [5] Sair \n '))

    if operacao == 5:
        print('Encerrando o programa...')
        break

    if operacao not in [1, 2, 3, 4]:
        print('Operação inválida. Tente novamente')
        continue

    numero1 = float(input('\nDigite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    
    resultado = calcular(numero1, numero2, operacao)
    print(f'Resultado: {resultado}')
