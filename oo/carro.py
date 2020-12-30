"""
>>> motor = Motor()
>>> direcao = Direcao()
>>> carro = Carro(motor = motor, direcao = direcao)
>>> carro.start()
"""
class Motor:
    def __init__(self, velocidade = 0):
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade += 1
        print(self.velocidade)
    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
        print(self.velocidade)

class Direcao:
    def __init__(self, direcao = 'n'):
        self.direita = 1
        self.esquerda = 1
        self.valor = direcao.upper()
        self.direcao_possivel = ['n','l','s','o']
    def girar_a_direita(self):
        posicao = self.direcao_possivel.index(self.valor.lower()) + self.direita
        if posicao > len(self.direcao_possivel):
            posicao = 0
        self.valor = self.direcao_possivel[posicao]
        print(f'{self.valor.upper()}')
    def girar_a_esquerda(self):
        posicao = self.direcao_possivel.index(self.valor) - self.direita
        self.valor = self.direcao_possivel[posicao]
        print(f'{self.valor.upper()}')
         
class Carro:
    def __init__(self, motor = None, direcao = None):
        self.motor = motor
        self.direcao = direcao
    def calcula_velocidade(self):
        self.velocidade = self.motor.velocidade
        print(self.velocidade)
    def calcula_direcao(self):
        self.direcao = self.direcao.valor
        print(self.direcao)
    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
    

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
        
