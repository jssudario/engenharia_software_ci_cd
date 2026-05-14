
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
    
    def exponencia(self, a, b):
        """Realiza a exponenciação de um número por outro"""
        return a ** b

    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular raiz quadrada de número negativo")
        return a ** 0.5

### doc: https://docs.pytest.org/en/7.1.x/how-to/assert.html