import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

data = pd.read_csv('TransporteNL_Limpio.csv')

label_encoder = LabelEncoder()
data['TRANSPORTE'] = label_encoder.fit_transform(data['TRANSPORTE'])
X = data[['Pasajeros transportados', 'UNIDADES_OPERANDO']]
y = data['TRANSPORTE']

# Conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

#Predicciones
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Precisión del modelo: {accuracy:.2f}')

plt.figure(figsize=(10, 6))
for i in range(len(label_encoder.classes_)):
    plt.scatter(X_test[y_pred == i]['Pasajeros transportados'],
                X_test[y_pred == i]['UNIDADES_OPERANDO'],
                label=label_encoder.inverse_transform([i])[0])

plt.xlabel('Pasajeros transportados')
plt.ylabel('Unidades operando')
plt.legend(title='Transporte', bbox_to_anchor=(1, 1), loc='upper left')
plt.title('Resultados del algoritmo KNN')
plt.show()
plt.savefig('KNN.png')
