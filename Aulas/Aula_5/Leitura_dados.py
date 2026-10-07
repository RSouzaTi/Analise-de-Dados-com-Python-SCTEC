import pandas as pd 


dado1 = pd.read_csv("dados1.csv")
dado2 = pd.read_csv("dados2.csv")

print("Dados do primeiro arquivo:")
print(dado1.head())

print("\nDados do segundo arquivo:")
print(dado2.head())