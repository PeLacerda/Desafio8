from app import validar_entrada


def test_entrada_valida():
    resultado = validar_entrada("ABC1D23", 3)
    assert resultado == True


def test_placa_vazia():
    resultado = validar_entrada("", 3)
    assert resultado == False


def test_quantidade_zero():
    resultado = validar_entrada("ABC1D23", 0)
    assert resultado == False


def test_quantidade_negativa():
    resultado = validar_entrada("ABC1D23", -2)
    assert resultado == False


def test_acima_do_limite():
    resultado = validar_entrada("ABC1D23", 13)
    assert resultado == False


def test_limite_permitido():
    resultado = validar_entrada("ABC1D23", 12)
    assert resultado == True
