import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes2.csv', sep=',', header=0)

# passando colunas qualitativas para quantitativas:
gender_maping = {
    "Male":0.0,
    "Female":1.0,
    "Other":2.0
}

smoking_history_maping = {
    "never":0.0,
    "ever":1.0,
    "No Info":2.0,
    "current":3.0,
    "not current":4.0,
    "former":5.0
}

data['gender'] = data['gender'].map(gender_maping)
data['smoking_history'] = data['smoking_history'].map(smoking_history_maping)

X = data.iloc[:, :8]
y = data.iloc[:, 8]

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

# Escalonando treino e teste:
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Descobrindo o melhor K na forca bruta:
k_values = [i for i in range (1,30)]
scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn, X, y, cv=5)
    scores.append(np.mean(score))

# Plot k_value X score
sns.lineplot(x = k_values, y = scores, marker = 'o')
plt.xlabel("K Values")
plt.ylabel("Accuracy Score")

# separando o melhor K:
best_index = np.argmax(scores)
best_k = k_values[best_index]

# classificando de acordo com o melhor K:
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

# Achando os valores significativos:
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

plt.show()