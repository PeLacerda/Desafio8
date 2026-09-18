from Teste2.app import validar_inscricao


def test_inscricao_valida():
    resultado = validar_inscricao("Ana", 18, 2)
    assert resultado == True


def test_nome_vazio():
    resultado = validar_inscricao("", 18, 2)
    assert resultado == False


def test_idade_abaixo_do_permitido():
    resultado = validar_inscricao("Ana", 15, 2)
    assert resultado == False


def test_idade_minima_permitida():
    resultado = validar_inscricao("Ana", 16, 2)
    assert resultado == True


def test_quantidade_zero():
    resultado = validar_inscricao("Ana", 18, 0)
    assert resultado == False


def test_quantidade_negativa():
    resultado = validar_inscricao("Ana", 18, -1)
    assert resultado == False


def test_quantidade_acima_do_limite():
    resultado = validar_inscricao("Ana", 18, 5)
    assert resultado == False


def test_quantidade_limite_permitido():
    resultado = validar_inscricao("Ana", 18, 4)
    assert resultado == True
