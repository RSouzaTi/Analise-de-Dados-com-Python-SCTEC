"""Etapa de formatação do meus dados que serao exibidos"""

from rich.console import Console

console = Console()

def numero_br (valor, casas_decimais=2):
   texto = f"{valor:,.{casas_decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")   
   texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
   return texto