def primo(n):
    if n <= 1:
        return False 
    for i in range(2, n): 
        if n % i == 0:
            return False 
    return True 

while True:
    try:
        n = int(input("Digite um número para verificar se ele é primo: "))

        resultado = primo(n)

        print(resultado)
    except ValueError:
        print("Digite um número válido")
    