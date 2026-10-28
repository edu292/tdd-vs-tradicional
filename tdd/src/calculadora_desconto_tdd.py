from dataclasses import dataclass
from enum import IntEnum, auto


class Categoria(IntEnum):
    PADRAO = auto()
    VIP = auto()


@dataclass
class Cliente:
    categoria: Categoria = Categoria.PADRAO


def calcular_valor_final(cliente: Cliente, valor_items: float) -> float:
    valor_final = valor_items
    if valor_final > 1000:
        valor_final *= 0.8
    elif valor_final > 500:
        valor_final *= 0.9

    if cliente.categoria == Categoria.VIP:
        valor_final *= 0.95

    return valor_final
