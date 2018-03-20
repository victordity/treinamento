import operator

class User:
    is_staff = False

    def __init__(self,name):
        self.name = name
        self.idade = 10
        self.cidade = 'BH'

    def __repr__(self):
        return 'Login do usuario'

    def enable_authorize(self):
        self.dado = 10

    def is_authorized(self):
        self.enable_authorize()
        return self.is_staff


usuario = User('Victor')
print(usuario.name)
print(usuario.idade)
print(usuario.is_authorized())
print('Testando variavel')









