def autenticar(login, senha):
    usuarios = [
    {
    "username": "teste",
    "password": "admin"
    },
    {
    "username": "teste2",
    "password": "admin2"
    },
    {
    "username": "teste3",
    "password": "admin3"
    },
    {
    "username": "teste4",
    "password": "admin4"
    },
    ]

    autenticado = False

    for usuario in usuarios:
        if usuario["username"] == login and usuario["password"] == senha:
            print('Usuário autenticado com sucesso.')
            autenticado = True
            break

    if autenticado == False:
        print('Usuário ou senha incorreto.')