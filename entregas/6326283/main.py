from mod_estoque import (
    cadastrar_item,
    calcular_valor_estoque,
    listar_itens_em_falta,
)


def main():
    """Ponto de entrada da Questao 3."""
    item1 = cadastrar_item("Teclado Mecânico", 15, 250.0)
    item2 = cadastrar_item("Mouse Óptico", 3, 80.0)
    item3 = cadastrar_item("Monitor 24'", 2, 900.0)

    estoque = [item1, item2, item3]

    valor_total = calcular_valor_estoque(estoque)
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    minimo = 5
    itens_baixos = listar_itens_em_falta(estoque, minimo)

    print(f"\nItens em falta (abaixo de {minimo} unidades):")
    for item in itens_baixos:
        print(f"- {item['nome']}: {item['quantidade']} unidade(s)")


if __name__ == "__main__":
    main()