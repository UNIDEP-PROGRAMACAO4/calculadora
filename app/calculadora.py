class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        return self.numero1 + self.numero2

    def subtracao(self):
        return  self.numero1 - self.numero2

    def multiplicacao(self):
        return self.numero1 * self.numero2

    def divisao(self):
        return self.numero1 / self.numero2


if __name__ == '__main__':
    assert Calculadora(1, 1).soma() == 2
    assert Calculadora(1, 2).soma() == 3
    assert Calculadora(2, 2).subtracao() == 0
    assert Calculadora(5, 2.5).subtracao() == 2.5
    assert Calculadora(2, 2).multiplicacao() == 4
    assert Calculadora(3, 7).multiplicacao() == 21
    assert Calculadora(4, 2).divisao() == 2

    print('Os testes passaram!')

