import pytest

from tdd.src.calculadora_desconto_tdd import Categoria, Cliente, calcular_valor_final


@pytest.fixture
def cliente_padrao():
    return Cliente(categoria=Categoria.PADRAO)


@pytest.fixture
def cliente_vip():
    return Cliente(categoria=Categoria.VIP)


def test_deve_manter_valor_integral_quando_compra_for_ate_500(cliente_padrao):
    assert calcular_valor_final(cliente_padrao, 500.0) == 500.0
    assert calcular_valor_final(cliente_padrao, 300.0) == 300.0


def test_deve_aplicar_10_porcento_desconto_quando_compra_acima_de_500(cliente_padrao):
    assert calcular_valor_final(cliente_padrao, 600.0) == pytest.approx(540.0)
    assert calcular_valor_final(cliente_padrao, 500.01) == pytest.approx(450.009)


def test_deve_manter_10_porcento_quando_compra_exatamente_1000(cliente_padrao):
    assert calcular_valor_final(cliente_padrao, 1000.0) == pytest.approx(900.0)


def test_deve_aplicar_20_porcento_desconto_quando_compra_acima_de_1000(cliente_padrao):
    assert calcular_valor_final(cliente_padrao, 1200.0) == pytest.approx(960.0)
    assert calcular_valor_final(cliente_padrao, 1000.01) == pytest.approx(800.008)


def test_cliente_vip_sem_desconto_base_recebe_apenas_5_porcento(cliente_vip):
    assert calcular_valor_final(cliente_vip, 400.0) == pytest.approx(380.0)


def test_cliente_vip_intersecao_faixa_10_porcento(cliente_vip):
    assert calcular_valor_final(cliente_vip, 600.0) == pytest.approx(513.0)


def test_cliente_vip_intersecao_faixa_20_porcento(cliente_vip):
    assert calcular_valor_final(cliente_vip, 1200.0) == pytest.approx(912.0)


def test_deve_cobrar_frete_quando_valor_final_menor_que_100(cliente_padrao):
    assert calcular_valor_final(cliente_padrao, 80.0) == 95.0


def test_nao_deve_cobrar_frete_quando_valor_final_exatamente_100(cliente_padrao):
    assert calcular_valor_final(cliente_padrao, 100.0) == 100.0


def test_intersecao_desconto_vip_empurrando_pedido_para_abaixo_de_100(cliente_vip):
    assert calcular_valor_final(cliente_vip, 102.0) == pytest.approx(111.90)
