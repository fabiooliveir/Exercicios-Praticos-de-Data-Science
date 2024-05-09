import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Carregar o dataset
data = pd.read_excel('/workspaces/exercicios_dnc/Redes Neurais/churn.xlsx')

# Selecionar as features e a variável target
X = data[['tenure', 'PhoneService', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']]
y = data['Churn']

# Converter variáveis categóricas em variáveis dummy
X = pd.get_dummies(X)

# Dividir o dataset em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de Regressão Logística
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Prever os valores para o conjunto de teste
y_pred_lr = lr_model.predict(X_test)

# Calcular a acurácia do modelo de Regressão Logística
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print("Acurácia da Regressão Logística:", accuracy_lr)

# Treinar o modelo de Rede Neural
nn_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000)
nn_model.fit(X_train, y_train)

# Prever os valores para o conjunto de teste
y_pred_nn = nn_model.predict(X_test)

# Calcular a acurácia da Rede Neural
accuracy_nn = accuracy_score(y_test, y_pred_nn)
print("Acurácia da Rede Neural:", accuracy_nn)
