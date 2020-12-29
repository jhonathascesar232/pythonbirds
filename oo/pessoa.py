class Pessoa:
    olhos = 2 # atributo de classe

    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    j = Pessoa(nome = 'Jhonathas', idade = 23)
    c = Pessoa(j, nome = 'César', idade = 51)
    
    print(j.nome)
    print(c.nome)
    for filho in c.filhos:
        print(f' FILHO: {filho.nome}')