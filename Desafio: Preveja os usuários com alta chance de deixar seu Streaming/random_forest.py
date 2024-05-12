# random_forest.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Carregar o dataframe do arquivo pickle
df = pd.read_pickle('dataframe_prepared.pkl')

# Definir variáveis X e y
X = df[['Age', 'Gender', 'Time_on_platform', 'Devices_connected', 'Subscription_type', 'Num_streaming_services', 'Num_active_profiles', 'Avg_rating']]
y = df['Churned']

# Dividir em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo de Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
