import pandas as pd
from rich.panel import Panel

from carrega_dados import carregar_dados
from formatacao import console, numero_br


def mostrar_resumo(df):
    total_registros = len(df)
    total_votos = pd.to_numeric(df["votos"], errors="coerce").sum()
    total_cidades = df["cidade"].nunique()
    total_candidatos = df["candidato"].nunique()

    texto = (
        f"[bold]Registros:[/] {numero_br(total_registros)}    "
        f"[bold]Votos:[/] {numero_br(total_votos)}    "
        f"[bold]Cidades:[/] {numero_br(total_cidades)}    "
        f"[bold]Candidatos:[/] {numero_br(total_candidatos)}"
    )
    console.print(Panel(texto, title="Eleições 2024 (dados fictícios)", expand=False))


if __name__ == "__main__":
    df = carregar_dados()
    mostrar_resumo(df)