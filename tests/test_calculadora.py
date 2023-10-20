import pytest
def soma(a, b):
    return a + b

def divisao(dividendo, divisor):
    if divisor == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return dividendo / divisor

def test_soma():
    assert soma(2, 3) == 5  # Teste bem-sucedido
    assert soma(-1, 1) == 0  # Teste bem-sucedido
    assert soma(0, 0) == 0  # Teste bem-sucedido
    assert soma(5, -3) == 2  # Teste bem-sucedido

def test_divisao():
    assert divisao(6, 2) == 3  # Teste bem-sucedido
    assert divisao(10, 5) == 2  # Teste bem-sucedido

    # Teste para exceção
    with pytest.raises(ValueError) as e:
        divisao(8, 0)  # Espera-se que lance uma exceção
    assert str(e.value) == "Divisão por zero não é permitida."  # Teste bem-sucedido