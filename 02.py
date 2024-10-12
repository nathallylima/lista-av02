##Escreva uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

numero = int(input("Digite um número inteiro: "))

def digitos(numero):
   return len(str(abs(numero)))

print(f"O numero {numero} possui {digitos(numero)} digitos")
