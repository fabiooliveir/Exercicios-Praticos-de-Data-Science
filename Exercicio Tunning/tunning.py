import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Carregar os dados
data = pd.read_excel('/workspaces/exercicios_dnc/Exercicio Tunning/Bank_Personal_Loan_Modelling.xlsx')

# Definir as features (X) e o target (y)
X = data[["Age", "Experience", "Income", "Family", "CCAvg", "Education", "Mortgage", "CreditCard", "Securities_Account", "CD_Account", "Online"]]
y = data["Personal_Loan"]

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar pipelines para padronização e modelo
pipe_dt = Pipeline([('scaler', StandardScaler()), ('dt', DecisionTreeRegressor())])
pipe_rf = Pipeline([('scaler', StandardScaler()), ('rf', RandomForestClassifier())])

# Definir os parâmetros para GridSearch
param_grid_dt = {'dt__max_depth': [3, 5, 7, 9, None]}
param_grid_rf = {'rf__n_estimators': [50, 100, 150], 'rf__max_depth': [3, 5, 7, 9, None]}

# Executar GridSearch para DecisionTreeRegressor
grid_dt = GridSearchCV(pipe_dt, param_grid_dt, cv=5, n_jobs=-1)
grid_dt.fit(X_train, y_train)

# Executar GridSearch para RandomForestClassifier
grid_rf = GridSearchCV(pipe_rf, param_grid_rf, cv=5, n_jobs=-1)
grid_rf.fit(X_train, y_train)

# Avaliar os modelos
print("DecisionTreeRegressor:")
print("Melhores hiperparâmetros:", grid_dt.best_params_)
print("Acurácia no conjunto de teste:", grid_dt.score(X_test, y_test))

print("\nRandomForestClassifier:")
print("Melhores hiperparâmetros:", grid_rf.best_params_)
print("Acurácia no conjunto de teste:", grid_rf.score(X_test, y_test))
