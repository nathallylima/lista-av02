def conversao():
    print('\n CONVERSOR DE TEMPERATURAS \n')

    while True:
        try:
            temperatura = int(input('\nEscolha uma Opção: \n'
                                    '[1] para converter de Celsius para Fahrenheit, \n' 
                                    '[2] para converter de Fahrenheit para Celsius \n' 
                                    '[3] para sair do conversor de temperaturas \n'))

            if temperatura == 3:
                print('Encerrando o programa...')
                break

            if temperatura == 1:
                celsius = float(input('Digite a temperatura em Celsius: '))
                fahrenheit = (celsius * 1.8) + 32
                print(f'{celsius}°C é igual a {fahrenheit}°F')

            elif temperatura == 2:
                fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
                celsius = (fahrenheit - 32) / 1.8
                print(f'{fahrenheit}°F é igual a {celsius}°C')

            else:
                print('Digite uma opçao válida.')   
                    
        except ValueError:
            print('Digite um valor válido.')         


conversao()