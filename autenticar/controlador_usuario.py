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

 
    if usuarios["username"] == login and usuarios["password"] == senha:
        print('Usuário autenticado com sucesso.')
        autenticado = True
        

    if autenticado == False:
        print('Usuário ou senha incorreto.')