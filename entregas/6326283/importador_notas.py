

import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("importacao.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def importar_notas(caminho: str) -> float:
    try:
        df = pd.read_csv(caminho)

        for _, linha in df.iterrows():
            logging.info(
                "Nota: %s | Cliente: %s | Valor: R$ %.2f",
                linha["nota"],
                linha["cliente"],
                linha["valor"],
            )

        total = float(df["valor"].sum())
        logging.info("Total faturado calculado com sucesso: R$ %.2f", total)
        return total

    except FileNotFoundError:
        logging.error("Arquivo não encontrado: %s", caminho)
        return 0.0

    except pd.errors.EmptyDataError:
        logging.error("O arquivo CSV está vazio: %s", caminho)
        return 0.0

    finally:
        logging.info("Tentativa de importação finalizada para o arquivo: %s", caminho)


if __name__ == "__main__":
    importar_notas("notas.csv")
    importar_notas("arquivo_inexistente.csv")