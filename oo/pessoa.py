class Pessoa:
    def __init__(self, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Jhonathas', 23)

    print(Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())
    print(p.nome)
    p.nome = 'Silva'
    print(p.nome)