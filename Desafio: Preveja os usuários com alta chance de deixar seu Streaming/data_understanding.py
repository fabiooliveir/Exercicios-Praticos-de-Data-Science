# data_understanding.py
import pandas as pd

# Carregar a base de dados
df = pd.read_csv('/workspaces/exercicios_dnc/Desafio: Preveja os usuários com alta chance de deixar seu Streaming/streaming_data.csv')

# Descrição estatística dos dados
print(df.describe())

# Verificar os tipos de dados
print(df.info())

# Verificar a quantidade de valores faltantes
print(df.isna().sum())

# Salvar o dataframe em um arquivo pickle
df.to_pickle('dataframe.pkl')

