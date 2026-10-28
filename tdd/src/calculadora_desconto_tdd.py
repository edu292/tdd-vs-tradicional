def calcular_valor_final(valor_items: float) -> float:
    valor_final = valor_items
    if valor_final > 500:
        valor_final *= 0.9

    return valor_final
