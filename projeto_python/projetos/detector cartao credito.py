"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar os dados
dados = pd.read_csv('creditcard.csv')

# Separar características e rótulos
X = dados.drop('Class', axis=1)
y = dados['Class']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Treinar modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Prever
y_pred = modelo.predict(X_test)

# Avaliar
precisao = accuracy_score(y_test, y_pred)
print(f"Precisão: {precisao}")
"""


import pandas as pd
from sklearn.model_selection import train_test_split

# Carregar os dados do arquivo CSV
dados = pd.read_csv('creditcard.csv')

# Exibir as primeiras linhas do dataframe
print(dados.head())
