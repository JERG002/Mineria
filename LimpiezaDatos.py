import pandas as pd
from datetime import datetime

datos = pd.read_csv('TransporteNL.csv')

Campos = ['Autobuses en operación de lunes a viernes', 'Autobuses en operación de sábado a domingo', 'Trenes en servicio', 'Unidades en operación', 'Cabinas en operación de lunes a viernes', 'Cabinas en operación de sábado a domingo', 'Kilómetros recorridos', 'Pasajeros transportados']

datos = datos[datos['VARIABLE'].isin(Campos)]

datos['FECHA'] = datos.apply(lambda row: datetime(row['ANIO'], row['ID_MES'], 1), axis=1)

lista = []

m = 1
f = 1

for i in range(len(datos)):
    f = f + 1

for i in range(len(datos)):
    x = datos.iloc[i]['TRANSPORTE']
    y = ''
    if i < 14481:
        y = datos.iloc[i+1]['TRANSPORTE']
        if x == y:
            lista.append(m)
        else:
            
            lista.append(m)
            m = m + 1
    else:
        break
while(len(lista) < len(datos['TRANSPORTE'])):
    lista.append(m)

datos['ID'] = lista

datos = datos.drop(columns=['ESTATUS', 'ANIO', 'ID_MES'])

datos = datos.pivot_table(index=['FECHA', 'TRANSPORTE', 'ID_ENTIDAD' , 'ID_MUNICIPIO'], columns='VARIABLE', values='VALOR').reset_index()


SumaColumnas = ['Autobuses en operación de lunes a viernes', 'Autobuses en operación de sábado a domingo', 'Trenes en servicio', 'Unidades en operación', 'Cabinas en operación de lunes a viernes', 'Cabinas en operación de sábado a domingo']



TotalSumas = []

for index, fila in datos.iterrows():
    suma_fila = fila[SumaColumnas].sum()
    TotalSumas.append(suma_fila)

datos['UNIDADES_OPERANDO'] = TotalSumas

datos = datos.drop(columns=SumaColumnas)

#print(datos)

datos.to_csv('TransporteNL_Limpio.csv', index=False)