leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]


def monitorar(lista):
  
    soma_validas = 0.0
    qtd_validas = 0
    interrompido = False

    for leitura in lista:
        if leitura > 80.0:
            print(f"[DESCARTE] Leitura de {leitura}°C fora da faixa: ignorada.")
            continue

        if leitura == -999.0:
            print(f"[FALHA] Sensor corrompido ({leitura}). Interrompendo monitoramento...")
            interrompido = True
            break

        print(f"[OK] Leitura de {leitura}°C registrada.")
        soma_validas += leitura
        qtd_validas += 1

    if not interrompido:
        print(f"\nQuantidade de leituras válidas: {qtd_validas}")
        if qtd_validas > 0:
            media = soma_validas / qtd_validas
            print(f"Média das leituras: {media:.2f}°C")
        else:
            print("Média das leituras: 0.00°C")


if __name__ == "__main__":
    monitorar(leituras)