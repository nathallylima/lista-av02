from autenticar.controlador_usuario import autenticar

login = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

autenticar(login, senha)