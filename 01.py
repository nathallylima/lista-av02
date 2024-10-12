##  Faça um programa, com uma função que necessite de um parâmetro “número”. A função retorna o valor de
## caractere ‘P’, se seu valor for positivo, e ‘N’, se seu valor for zero ou negativo.

numero = int(input("Digite um número:  "))

def verificar_numero(numero):
    if numero <= 0:
        print("N")
    else:
        print("P")

verificar_numero(numero)