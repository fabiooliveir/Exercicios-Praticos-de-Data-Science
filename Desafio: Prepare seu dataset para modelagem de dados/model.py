import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('caminho/do/arquivo/Data - data (2).csv.csv', encoding='latin1')

# Verificar a distribuição dos dados
print(df.describe())

# Verificar valores nulos
nulos = df.isna().sum()
print(nulos)

# Remover linhas com valores nulos
df = df.dropna()
print(df.isna().sum())

# Filtrar DataFrame para conter apenas preços acima de zero
df = df.loc[df['UnitPrice'] > 0]

# Filtrar DataFrame para conter apenas quantidade acima de zero
df = df.loc[df['Quantity'] > 0]

# Remover linhas duplicadas
df = df.drop_duplicates()

# Corrigir o tipo de dado do CustomerID
df['CustomerID'] = df['CustomerID'].astype('int')

# Corrigir o tipo de dado da InvoiceDate
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Criar boxplot para as colunas 'Quantity' e 'UnitPrice'
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Quantity', 'UnitPrice']])
plt.title('Boxplot de Quantidade e Preço Unitário')
plt.show()

# Criar um gráfico de dispersão para visualizar os outliers
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Quantity', y='UnitPrice')
plt.title('Quantidade vs. Preço Unitário')
plt.show()

# Remover outliers
df = df[(df['Quantity'] <= 10000) & (df['UnitPrice'] <= 5000)]

# Criar a coluna adicional com o preço total da compra
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Calcular a data da última compra no dataset como um todo
ultima_compra = df['InvoiceDate'].max()

# Agrupar os dados por país e somar o total de vendas
vendas_por_pais = df.groupby('Country')['TotalPrice'].sum().reset_index()

# Ordenar os países pelo total de vendas em ordem decrescente
vendas_por_pais = vendas_por_pais.sort_values(by='TotalPrice', ascending=False)

# Selecionar os top 10 países com maior valor em vendas
top_10_paises = vendas_por_pais.head(10)

# Plotar o gráfico de barras com os top 10 países
plt.figure(figsize=(12, 6))
sns.barplot(x='TotalPrice', y='Country', data=top_10_paises, palette='viridis')
plt.xlabel('Total de Vendas')
plt.ylabel('País')
plt.title('Top 10 Países com Maior Valor em Vendas')
plt.show()

# Agrupar os dados por produto e somar a quantidade vendida
produtos_mais_vendidos = df.groupby('Description')['Quantity'].sum().reset_index()

# Ordenar os produtos pela quantidade vendida em ordem decrescente
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='Quantity', ascending=False)

# Selecionar os top 10 produtos mais vendidos
top_10_produtos = produtos_mais_vendidos.head(10)

# Plotar o gráfico de barras com os top 10 produtos mais vendidos
plt.figure(figsize=(12, 6))
sns.barplot(x='Quantity', y='Description', data=top_10_produtos, palette='viridis')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Produto')
plt.title('Top 10 Produtos Mais Vendidos')
plt.show()

# Calcular o valor de venda total por mês
vendas_por_mes = df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalPrice'].sum()

# Plotar o gráfico de barras com o valor de venda total por mês
plt.figure(figsize=(12, 6))
vendas_por_mes.plot(kind='bar', color='skyblue')
plt.xlabel('Mês')
plt.ylabel('Valor de Venda Total')
plt.title('Valor de Venda Total por Mês')
plt.xticks(rotation=45)
plt.show()

# Calcular o valor de venda total por mês e país
vendas_por_mes_pais = df.groupby(['Country', df['InvoiceDate'].dt.to_period('M')])['TotalPrice'].sum().reset_index()

# Filtrar os top 10 países em vendas
top_10_paises = vendas_por_pais.groupby('Country')['TotalPrice'].sum().nlargest(10).index
vendas_por_mes_pais_top_10 = vendas_por_mes_pais[vendas_por_mes_pais['Country'].isin(top_10_paises)]

# Converter a coluna 'InvoiceDate' para string
vendas_por_mes_pais_top_10['InvoiceDate'] = vendas_por_mes_pais_top_10['InvoiceDate'].dt.strftime('%Y-%m')

# Plotar o gráfico de linhas com o valor de venda total por mês e país
plt.figure(figsize=(12, 6))
sns.lineplot(x='InvoiceDate', y='TotalPrice', hue='Country', data=vendas_por_mes_pais_top_10, palette='viridis')
plt.xlabel('Mês')
plt.ylabel('Valor de Venda Total (Escala Logarítmica)')
plt.title('Valor de Venda Total por Mês e País (Top 10)')
plt.legend(title='País', loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.yscale('log')
plt.show()

# Agrupar os dados por cliente e pedido para obter a data e o preço total do pedido
df_agrupado = df.groupby(['CustomerID', 'InvoiceNo']).agg({
    'InvoiceDate': 'first',  # Data do primeiro pedido do cliente
    'TotalPrice': 'sum'        # Preço total do pedido
}).reset_index()

# Calcular a recência, frequência e ticket médio para cada cliente
recencia = df_agrupado.groupby('CustomerID')['InvoiceDate'].max().apply(lambda x: (ultima_compra - x).days)
frequencia = df_agrupado.groupby('CustomerID').size()
ticket_medio = df_agrupado.groupby('CustomerID')['TotalPrice'].mean()

# Criar um DataFrame com os valores de RFM
rfm = pd.DataFrame({
    'Recency': recencia,
    'Frequency': frequencia,
    'Monetary': ticket_medio
})

# Verificar os primeiros registros do DataFrame de RFM
print(rfm.head())

# Salvar o DataFrame de RFM em um arquivo CSV
rfm.to_csv('rfm_metrics.csv', index=True)

# Fazer o download do arquivo CSV
# files.download('rfm_metrics.csv')
