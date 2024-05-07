import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Carregando a base de dados
vendas = pd.read_excel('/workspaces/exercicios_dnc/Arvore de decisão/vendas.xlsx')

# Dividindo a base em features (X) e target (y)
X = vendas[['media_rating', 'media_pedidos']]
y = vendas['cliente_comprou']

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de árvore de decisão
modelo = DecisionTreeClassifier()

# Treinando o modelo
modelo.fit(X_train, y_train)

plt.figure(figsize=(20,10))
tree.plot_tree(modelo, feature_names=X.columns, class_names=['Não Comprou', 'Comprou'], filled=True)
plt.savefig('/workspaces/exercicios_dnc/Arvore de decisão/arvore_decisao.png')


# Avaliando o modelo
score = modelo.score(X_test, y_test)
print(f'Acurácia do modelo: {score}')
