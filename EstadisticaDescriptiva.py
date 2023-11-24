import pandas as pd

datos = pd.read_csv('TransporteNL_Limpio.csv')

datos['FECHA'] = pd.to_datetime(datos.FECHA, format='%Y-%m-%d %H:%M:%S')

datos['ANIO'] = datos['FECHA'].dt.year

datos = datos.where(datos["ID_ENTIDAD"] == 19)   

datosPasajeros = datos.groupby(['ANIO', 'TRANSPORTE']).agg({'Pasajeros transportados': ['sum', 'count', 'mean', 'min', 'max', 'std', 'var']})

datosPasajeros.columns = ['Total', 'Meses', 'Promedio', 'Minimo Pasajeros', 'Maximo Pasajeros', 'Estandar', 'Varianza']

datosDistancia = datos.groupby(['ANIO', 'TRANSPORTE']).agg({'Kilómetros recorridos': ['sum', 'count', 'mean', 'min', 'max', 'std', 'var']})

datosDistancia.columns = ['Total', 'Meses', 'Promedio', 'Minima Distancia', 'Maxima Distancia', 'Estandar', 'Varianza']

datosUnidades = datos.groupby(['ANIO', 'TRANSPORTE']).agg({'UNIDADES_OPERANDO': ['sum', 'count', 'mean', 'min', 'max', 'std', 'var']})

datosUnidades.columns = ['Total', 'Meses', 'Promedio', 'Minimo Unidades', 'Maxima Unidades', 'Estandar', 'Varianza']

# print(datosPasajeros)
datosPasajeros.to_csv('TransporteNL_Estadistica_Pasajeros.csv', index=False)
# print(datosDistancia)
datosDistancia.to_csv('TransporteNL_Estadistica_Distancias.csv', index=False)
# print(datosUnidades)
datosUnidades.to_csv('TransporteNL_Estadistica_Unidades.csv', index=False)