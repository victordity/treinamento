class Animal:
    wild = False

class Tigre(Animal):
    wild = True

    def __init__(self, cor, barulho):
        self.cor = cor
        self.barulho = barulho


class Gato(Animal):
    def __init__(self, cor, barulho):
        self.cor = cor
        self.barulho = barulho

def check(permitions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(permitions)
            if args[0].wild and "selvagem" in permitions:
                return func(*args, **kwargs)
            elif args[0].wild and "domestico" in permitions:
                return func(*args, **kwargs)
            print("Sem permissao")
            return False

        return wrapper
    return decorator

gato = Gato("preto","miado")
tigre = Tigre("branco","rugido")

@check(["selvagem"])
def go_forest(animal):
    print("Foi pro mato")

@check(["domestico"])
def go_city(animal):
    print("Foi pra cidade")


go_forest(gato)
go_forest(tigre)

go_city(gato)
go_city(tigre)