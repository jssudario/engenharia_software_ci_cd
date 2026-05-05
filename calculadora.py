
class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por 0") 
        return a / b

### doc: https://docs.pytest.org/en/7.1.x/how-to/assert.html