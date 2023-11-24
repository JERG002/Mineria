import pandas as pd
import matplotlib.pyplot as plt


#
datos = pd.read_csv('TransporteNL_Limpio.csv').groupby('TRANSPORTE')['UNIDADES_OPERANDO'].sum().reset_index()

#
datos.plot(kind="bar", x='TRANSPORTE', y='UNIDADES_OPERANDO')
plt.xlabel("Transporte")
plt.ylabel("Total Unidades Operando")
plt.title("Transportes con más unidades")
plt.savefig('Transportes_Con_Mas_unidades.png')
plt.close()

datos = pd.read_csv('TransporteNL_Limpio.csv').groupby('TRANSPORTE')['Pasajeros transportados'].sum().reset_index()
datos.plot(kind="bar", x='TRANSPORTE', y='Pasajeros transportados')
plt.xlabel("Transporte")
plt.ylabel("Total Pasajeros")
plt.title("Transportes con más uso")
plt.savefig('Transportes_Mas_Utilizado_Pais.png')
plt.close()

datosNL = pd.read_csv('TransporteNL_Limpio.csv').query('ID_ENTIDAD == 19')
datos = datosNL.groupby(['TRANSPORTE'])['Pasajeros transportados'].sum().reset_index()
plt.pie(datos['Pasajeros transportados'], labels=datos['TRANSPORTE'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Transportes mas usados en NL")
plt.savefig('Transportes_Mas_Utilizado_NL.png')

datosCDMX = pd.read_csv('TransporteNL_Limpio.csv').query('ID_ENTIDAD == 9')
datos = datosCDMX.groupby(['TRANSPORTE'])['Pasajeros transportados'].sum().reset_index()
plt.pie(datos['Pasajeros transportados'], labels=datos['TRANSPORTE'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Transportes mas usados en CDMX")
plt.savefig('Transportes_Mas_Utilizado_CDMX.png')


datosNormales = pd.read_csv('TransporteNL_Limpio.csv')

datosNormales['FECHA'] = pd.to_datetime(datosNormales.FECHA, format='%Y-%m-%d %H:%M:%S')
datosNormales['ANIO'] = datosNormales['FECHA'].dt.year

datosActuales = datosNormales.query('ANIO == 2023')
datos = datosActuales.groupby('ID_ENTIDAD')['TRANSPORTE'].count().reset_index()
datos.plot(kind="bar", x='ID_ENTIDAD', y='TRANSPORTE')
plt.xlabel("Entidad")
plt.ylabel("Cantidad Transportes")
plt.title("Total Transportes por estado")
plt.savefig('Total_Transportes_Estado.png')
plt.close()