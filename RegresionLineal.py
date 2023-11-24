import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carga el conjunto de datos desde un archivo CSV
datos = pd.read_csv('TransporteNL_Limpio.csv')
datos = datos.where(datos["TRANSPORTE"] == 'Sistema de Transporte Colectivo Metro')   
# Asegúrate de tener 'data' cargado desde tu archivo CSV


# Usa seaborn para crear un gráfico de dispersión con la línea de regresión
sns.lmplot(x='UNIDADES_OPERANDO', y='Pasajeros transportados', data=datos)
# Muestra el gráfico
plt.xlabel('Unidades operando')
plt.ylabel('Pasajeros transportados')
plt.title('Regresión Lineal: Unidades Operando vs Pasajeros')
plt.show()
plt.savefig('RegresionLineal.png')
plt.close()