import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('TransporteNL_Limpio.csv')

transportes = ['Sistema de Transporte Colectivo Metro', 'Metrorrey', 'Red de Transporte de Pasajeros', 'Tren Ligero', 'Trolebús', 'Cablebús', 'Tren Eléctrico', 'Metrobús', 'Transmetro', 'Tren Suburbano', 'Macrobús Servicio Troncal', 'Macrobús Servicio Alimentador', 'Sistema Integral del Tren Ligero', 'Qrobús', 'Tuzobús Servicio Troncal', 'Tuzobús Servicio Alimentador', 'Ecovía', 'Vivebús', 'Mexicable', 'Mexibús', 'Mi Transporte Eléctrico', 'Red Urbana de Transporte Articulado', 'Optibús', 'MI Macro Periférico Alimentador','Mi Macro Periférico Troncal']
indice = 6 #Elegir trnasporte: Revisar final de codigo para elegir el transporte
df = df.where(df['TRANSPORTE'] == transportes[indice])

#df_agrupado = df.groupby('TRANSPORTE').agg({'Pasajeros transportados': 'sum', 'UNIDADES_OPERANDO': 'sum'}).reset_index()

#df = df.head(1000) #Definir tamaño de muestra

df = df.dropna()

X = df['UNIDADES_OPERANDO']
y = df['Pasajeros transportados']


X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
results = model.summary()

print(results)

sns.regplot(x='UNIDADES_OPERANDO', y='Pasajeros transportados', data=df, ci=99)
plt.title('Regresión Lineal con Intervalo de Confianza para ' + transportes[indice])
plt.xlabel('UNIDADES_OPERANDO')
plt.ylabel('Pasajeros transportados')
plt.savefig('Forecast_'+transportes[indice]+'.png')
plt.show()

#0      Sistema de Transporte Colectivo Metro
#1      Metrorrey
#2      Red de Transporte de Pasajeros
#3      Tren Ligero
#4      Trolebús
#5      Cablebús
#6      Sistema de Transporte Colectivo Metrorrey
#7      Tren Eléctrico
#8      Metrobús
#9      Transmetro
#10     Tren Suburbano
#11     Macrobús Servicio Troncal
#12     Macrobús Servicio Alimentador
#13     Sistema Integral del Tren Ligero
#14     Qrobús
#15     Tuzobús Servicio Troncal
#16     Tuzobús Servicio Alimentador
#17     Ecovía
#18     Vivebús
#19     Mexicable
#20     Mexibús
#21     Mi Transporte Eléctrico
#22     Red Urbana de Transporte Articulado
#23     Optibús
#24     MI Macro Periférico Alimentador
#25     Mi Macro Periférico Troncal