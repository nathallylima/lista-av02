##Crie uma função que receba uma lista de números e retorne a soma de todos
##os elementos da lista.

def soma():
    while True:
        try:
            quantidade = int(input("Digite quantos números deseja adicionar na lista para serem somados: "))
            lista = []
            
            for _ in range(quantidade):
                n = float(input("Digite o número que deseja adicionar: "))
                lista.append(n)

            return sum(lista)

        except ValueError:
            print('Digite um número válido.')

resultado = soma()
print(f'A soma de todos os números digitados é: {resultado}')
