class Pessoa:
    olhos = 2 # atributo de classe

    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'Olá {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nomes_e_attr_de_classe(cls):
        return f'{cls} olhos {cls.olhos}'
class Homen(Pessoa):    #herança
    def comprimentar(self):
        comprimentar_da_classe = super().comprimentar()
        return f'{comprimentar_da_classe}. Aperto de mãos.'


if __name__ == '__main__':
    j = Pessoa(nome = 'Jhonathas', idade = 23)
    c = Homen(j, nome = 'César', idade = 51)
    
    print(j.nome)
    print(c.nome)
    for filho in c.filhos:
        print(f' FILHO: {filho.nome}')

    print(Pessoa.metodo_estatico(), j.metodo_estatico())
    print(Pessoa.nomes_e_attr_de_classe(), j.nomes_e_attr_de_classe())

    print(c.comprimentar())
