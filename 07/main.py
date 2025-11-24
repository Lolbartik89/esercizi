import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Caricamento dataset
url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
data = pd.read_csv(url)

# 2. Rimozione colonna categorica
data = data.drop("ocean_proximity", axis=1)

# 3. Sostituzione di valori NaN con la media della colonna
data = data.fillna(data.mean(numeric_only=True))

# 4. Preparazione dati
X = data.drop("median_house_value", axis=1)
y = data["median_house_value"]

# 5. Suddivisione in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Modello
modello = LinearRegression()
modello.fit(X_train, y_train)

# 7. Predizione e valutazione
y_pred = modello.predict(X_test)
errore = mean_absolute_error(y_test, y_pred)

print("Errore medio assoluto:", errore)
