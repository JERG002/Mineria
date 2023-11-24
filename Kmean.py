import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('TransporteNL_Limpio.csv')
Columnas = df[['UNIDADES_OPERANDO', 'Pasajeros transportados']]

escalar = StandardScaler()
columnas_escaladas = escalar.fit_transform(Columnas)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(columnas_escaladas)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Método del Codo')
plt.xlabel('Número de Clusters')
plt.ylabel('WCSS (Inertia)')
plt.savefig('MetodoCodo.png')
plt.show()

num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(columnas_escaladas)


plt.figure(figsize=(8, 6))
for cluster in range(num_clusters):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['UNIDADES_OPERANDO'], cluster_data['Pasajeros transportados'], label=f'Grupo {cluster}', alpha=0.7)
plt.xlabel('UNIDADES_OPERANDO')
plt.ylabel('Pasajeros transportados')
plt.title('Clustering de Transporte')
plt.legend()
plt.savefig('KMeans.png')
plt.show()
