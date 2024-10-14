import re

def verificador(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

email = input('Digite seu e-mail: ')
resultado = verificador(email)

if resultado:
    print('O e-mail é válido.')
else:
    print('O e-mail não é válido.')