# data_preparation.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Carregar o dataframe do arquivo pickle
df = pd.read_pickle('dataframe.pkl')

# Substituir valores NaN por 0
cols_to_fillna = ['Time_on_platform', 'Num_streaming_services', 'Churned', 'Avg_rating', 'Devices_connected']
df[cols_to_fillna] = df[cols_to_fillna].fillna(0)

# Dropar linhas nulas
cols_to_dropna = ['Gender', 'Subscription_type', 'Age']
df = df.dropna(subset=cols_to_dropna)

# Transformar valores churned
df['Churned'] = df['Churned'].replace({0: 'No', 1: 'Yes'})

# Transformar valores floats em inteiros
cols_to_convert = ['Time_on_platform', 'Num_streaming_services', 'Avg_rating', 'Devices_connected']
df[cols_to_convert] = df[cols_to_convert].astype(int)

# LabelEncoder para as variáveis categóricas
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Subscription_type'] = le.fit_transform(df['Subscription_type'])

# MinMaxScaler para normalizar as variáveis numéricas
scaler = MinMaxScaler()
cols_to_scale = ['Age', 'Time_on_platform', 'Num_streaming_services', 'Num_active_profiles', 'Avg_rating', 'Devices_connected']
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

# Salvar o dataframe modificado em um novo arquivo pickle
df.to_pickle('dataframe_prepared.pkl')
