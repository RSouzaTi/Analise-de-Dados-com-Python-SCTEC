import pandas as pd
from rich.console import Console
from rich.panel import Panel

CAMINHO_CSV = "dados_csv.csv"


def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype={})
    return df


if __name__ == "__main__":
    df = carregar_dados()
    console = Console()
    console.print(Panel(df.head().to_string()))