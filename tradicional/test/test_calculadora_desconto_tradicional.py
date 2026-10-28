import pytest

from tradicional.src.calculadora_desconto_tradicional import (
    Categoria,
    Cliente,
    calcular_valor_final,
)


@pytest.mark.parametrize("valor_invalido", [0.0, -0.01, -100.0])
def test_deve_lancar_excecao_para_valor_itens_zerado_ou_negativo(valor_invalido):
    cliente = Cliente(categoria=Categoria.PADRAO)
    with pytest.raises(ValueError):
        calcular_valor_final(cliente, valor_invalido)


def test_deve_cobrar_frete_quando_valor_final_menor_que_100():
    cliente = Cliente(categoria=Categoria.PADRAO)
    assert calcular_valor_final(cliente, 80.0) == pytest.approx(95.0)


def test_nao_deve_cobrar_frete_quando_valor_final_exatamente_100():
    cliente = Cliente(categoria=Categoria.PADRAO)
    assert calcular_valor_final(cliente, 100.0) == pytest.approx(100.0)


def test_nao_deve_aplicar_desconto_ate_500():
    cliente = Cliente(categoria=Categoria.PADRAO)
    assert calcular_valor_final(cliente, 500.0) == pytest.approx(500.0)


def test_deve_aplicar_desconto_10_porcento_acima_de_500():
    cliente = Cliente(categoria=Categoria.PADRAO)
    assert calcular_valor_final(cliente, 600.0) == pytest.approx(540.0)


def test_deve_aplicar_desconto_10_porcento_na_fronteira_de_1000():
    cliente = Cliente(categoria=Categoria.PADRAO)
    assert calcular_valor_final(cliente, 1000.0) == pytest.approx(900.0)


def test_deve_aplicar_desconto_20_porcento_acima_de_1000():
    cliente = Cliente(categoria=Categoria.PADRAO)
    assert calcular_valor_final(cliente, 1200.0) == pytest.approx(960.0)


def test_cliente_vip_sem_desconto_por_faixa():
    cliente = Cliente(categoria=Categoria.VIP)
    assert calcular_valor_final(cliente, 200.0) == pytest.approx(190.0)


def test_cliente_vip_com_desconto_10_porcento():
    cliente = Cliente(categoria=Categoria.VIP)
    assert calcular_valor_final(cliente, 600.0) == pytest.approx(513.0)


def test_cliente_vip_com_desconto_20_porcento():
    cliente = Cliente(categoria=Categoria.VIP)
    assert calcular_valor_final(cliente, 1200.0) == pytest.approx(912.0)


def test_desconto_vip_leva_pedido_abaixo_de_100_e_aplica_frete():
    cliente = Cliente(categoria=Categoria.VIP)
    assert calcular_valor_final(cliente, 102.0) == pytest.approx(111.90)
