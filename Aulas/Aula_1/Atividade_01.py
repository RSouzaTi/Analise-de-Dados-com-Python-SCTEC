import csv

with open('csv_aula.csv', 'r', newline='') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)