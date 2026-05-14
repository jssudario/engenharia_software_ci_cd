import pytest
from calculadora import Calculadora

def test_soma():
    # arrange
    calc = Calculadora()
    # act
    res_positivo = calc.soma(2, 3)
    res_negativo = calc.soma(-7, 4)
    res_float = calc.soma(0.1, 0.2)
    # assert
    assert res_positivo == 5
    assert res_negativo == -3
    assert res_float == 0.30000000000000004 # ou round(res_float, 2) == 0.3

def test_subtracao():
    # arrange
    calc = Calculadora()
    # act e assert
    assert calc.subtracao(39, 9) == 30

def test_multiplicacao():
    # arrange
    calc = Calculadora()
    # act e assert
    assert calc.multiplicacao(3, 7) == 21

def test_divisao():
    # arrange
    calc = Calculadora()
    # act e assert
    assert calc.divisao(20, 4) == 5
    assert calc.divisao(0, 5) == 0

def test_varias_operacoes():
    # arrange
    calc = Calculadora()
    # act
    res_soma = calc.soma(10.5, 4.5) # 15.0
    res_sub = calc.subtracao(res_soma, 3) # 12.0
    res_soma2 = calc.soma(res_sub, -2) # 10.0
    res_final = calc.multiplicacao(res_soma2, 2) # 20.0
    # assert
    assert res_final == 20.0

def test_divisao_por_zero():
    calc = Calculadora()
    # esperando ValueError
    with pytest.raises(ValueError, match="Não é possível dividir por 0"):
        calc.divisao(10, 0)

def test_exponenciacao():
    calc = Calculadora()
    assert calc.exponencia(2, 3) == 8
    assert calc.exponencia(5, 0) == 1
    assert calc.exponencia(3, 4) == 81
    
def test_raiz_quadrada():
    # arrange
    calc = Calculadora()
    # act e assert
    assert calc.raiz_quadrada(9) == 3.0
    assert calc.raiz_quadrada(0) == 0.0
    assert round(calc.raiz_quadrada(2), 4) == 1.4142
    # esperando ValueError
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-1)

### doc: https://docs.pytest.org/en/7.1.x/how-to/assert.html