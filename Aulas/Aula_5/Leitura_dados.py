from pathlib import Path
import pandas as pd

pasta = Path(__file__).resolve().parent

dado1 = pd.read_csv(pasta / "dados1.csv")
dado2 = pd.read_csv(pasta / "dados2.csv")

print("Dados do primeiro arquivo:")
print(dado1.head())

print("\nDados do segundo arquivo:")
print(dado2.head())