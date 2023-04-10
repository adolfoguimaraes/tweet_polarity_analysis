import pandas as pd
import csv
from analyser import Analyser

# Ler o arquivo CSV e criar um DataFrame
df = pd.read_csv('arquivo_de_entrada.csv')

# Extrair os IDs do Twitter da coluna 'id'
ids = df['id'].tolist()

# Analisar os IDs usando o método 'analyser_users' da classe 'Analyser'
results = analyser.analyser_users(ids)

print(results)
    

# Criar um novo arquivo CSV para armazenar os resultados
with open('resultado.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Escrever os cabeçalhos das colunas no arquivo CSV
    writer.writerow(['id', 'resultado'])

    # Escrever os resultados para cada ID no arquivo CSV
    for id, result in results.items():
        writer.writerow([id, result])