import pytest

from tdd.src.calculadora_desconto_tdd import calcular_valor_final


def test_deve_manter_valor_integral_quando_compra_for_ate_500():
    assert calcular_valor_final(500.0) == 500.0
    assert calcular_valor_final(300.0) == 300.0


def test_deve_aplicar_10_porcento_desconto_quando_compra_acima_de_500():
    assert calcular_valor_final(600.0) == pytest.approx(540.0)
    assert calcular_valor_final(500.01) == pytest.approx(450.009)


def test_deve_manter_10_porcento_quando_compra_exatamente_1000():
    assert calcular_valor_final(1000.0) == pytest.approx(900.0)


def test_deve_aplicar_20_porcento_desconto_quando_compra_acima_de_1000():
    assert calcular_valor_final(1200.0) == pytest.approx(960.0)
    assert calcular_valor_final(1000.01) == pytest.approx(800.008)
