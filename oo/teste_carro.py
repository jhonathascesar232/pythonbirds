from unittest import TestCase

from carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(0, motor.velocidade, 'Teste da velocidade')
if __name__=='__main__':
    teste = CarroTestCase()
    teste.teste_velocidade_inicial()
    teste.teste_acelerar()