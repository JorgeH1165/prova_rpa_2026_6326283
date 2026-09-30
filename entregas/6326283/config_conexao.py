def main():
    """Ponto de entrada da Questao 1."""
    ENDPOINT_URL: str = "https://api.exemplo.com/v1"
    PORTA: int = 8080
    TAXA_AMOSTRAGEM: float = 1.5
    USA_HTTPS: bool = True

    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS,
    }

    print("--- Relatório de Validação de Parâmetros ---")
    for chave, valor in parametros.items():
        print(f"Parâmetro: {chave} | Valor: {valor} | Tipo: {type(valor)}")


if __name__ == "__main__":
    main()