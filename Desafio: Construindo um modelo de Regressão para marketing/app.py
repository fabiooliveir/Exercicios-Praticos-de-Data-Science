import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def carregar_dados(caminho):
    """Carrega os dados do arquivo CSV."""
    return pd.read_csv(caminho)

df = carregar_dados('./MKT.csv')

def adicionar_coluna_total_investment(df):
    """Adiciona uma nova coluna com o total de investimento."""
    df['total_investment'] = df[['youtube', 'facebook', 'newspaper']].sum(axis=1)
    return df

def criar_heatmap_corr(df):
    """Cria um heatmap da correlação entre as variáveis."""
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlação entre as Variáveis')
    plt.show()

def criar_pizza_proporcao_investimento(df):
    """Cria um gráfico de pizza com a proporção de investimento em cada plataforma."""
    totals = [df['youtube'].sum(), df['facebook'].sum(), df['newspaper'].sum()]
    labels = ['Youtube', 'Facebook', 'Newspaper']
    plt.figure(figsize=(8, 6))
    plt.pie(totals, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Proporção de Investimento em Cada Plataforma')
    plt.show()

# Outras funções para criar gráficos e análises...

def dividir_dados_treinamento_teste(df):
    """Divide o conjunto de dados em treinamento e teste."""
    X = df[['youtube', 'facebook', 'newspaper']]
    y = df['sales']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def treinar_modelo(X_train, y_train):
    """Cria e treina o modelo de regressão linear."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def avaliar_modelo(model, X_test, y_test):
    """Avalia o modelo de regressão linear."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Mean Squared Error:", mse)
    print("R^2 Score:", r2)

# Função principal
def main():
    adicionar_coluna_total_investment(df)
    criar_heatmap_corr(df)
    criar_pizza_proporcao_investimento(df)
    X_train, X_test, y_train, y_test = dividir_dados_treinamento_teste(df)
    model = treinar_modelo(X_train, y_train)
    avaliar_modelo(model, X_test, y_test)

if __name__ == "__main__":
    main()
