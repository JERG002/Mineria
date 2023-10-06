import pandas as pd
from scipy.stats import f_oneway

def resultado(resultadoAnova):
    if resultadoAnova.pvalue < 0.05:
        print("Hay diferencias significativas entre al menos dos grupos.")
    else:
        print("No hay diferencias significativas entre los grupos.")

datos = pd.read_csv('TransporteNL_Limpio.csv')


datosNL = datos.where(datos['ID_ENTIDAD'] == 19)
datost1 = datosNL.where(datosNL['TRANSPORTE'] == 'Metrorrey')
datost1 = datost1.dropna(subset='ID_ENTIDAD')
datost1['Metro'] = datost1['Pasajeros transportados']
datpst2 = datosNL.where(datosNL['TRANSPORTE'] == 'Transmetro')
datpst2 = datpst2.dropna(subset='TRANSPORTE')
datpst2['Transmetro'] = datpst2['Pasajeros transportados']
datosjoinNL = pd.concat([datost1, datpst2], axis=0, ignore_index=True)

resultado_anova01 = f_oneway(datost1['Metro'], datpst2['Transmetro'])


datosCMX = datos.where(datos['ID_ENTIDAD'] == 9)
datost1 = datosCMX.where(datosCMX['TRANSPORTE'] == 'Sistema de Transporte Colectivo Metro')
datost1 = datost1.dropna(subset='ID_ENTIDAD')
datost1['Metro'] = datost1['Pasajeros transportados']
datpst2 = datosCMX.where(datosCMX['TRANSPORTE'] == 'Metrobús')
datpst2 = datpst2.dropna(subset='TRANSPORTE')
datpst2['Metrobus'] = datpst2['Pasajeros transportados']
datosjoinCDMX = pd.concat([datost1, datpst2], axis=0, ignore_index=True)



resultado_anova1 = f_oneway(datosjoinNL['Pasajeros transportados'], datosjoinNL['UNIDADES_OPERANDO'])
resultado_anova2 = f_oneway(datosjoinNL['Kilómetros recorridos'], datosjoinNL['UNIDADES_OPERANDO'])
resultado_anova3 = f_oneway(datost1['Metro'], datpst2['Metrobus'])
resultado_anova4 = f_oneway(datosjoinCDMX['Pasajeros transportados'], datosjoinCDMX['UNIDADES_OPERANDO'])


print("ANOVA NUEVO LEON Metro - Transmetro: ",resultado_anova01)
resultado(resultado_anova01)
print("ANOVA NUEVO LEON Metro y Transmetro - Unidades Operando: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA NUEVO LEON Kilometros recorridos - Unidades Operando: ",resultado_anova2)
resultado(resultado_anova2)
print("ANOVA CDMX Metro - Metrobus: ",resultado_anova3)
resultado(resultado_anova3)
print("ANOVA CDMX Metro y Metrobus - Unidades Operando: ",resultado_anova4)
resultado(resultado_anova4)

datosCMX = datos.where(datos['ID_ENTIDAD'] == 9)
datost1 = datosCMX.where(datosCMX['TRANSPORTE'] == 'Tren Ligero')
datost1 = datost1.dropna(subset='ID_ENTIDAD')
datost1['TrenLigero'] = datost1['Pasajeros transportados']
datpst2 = datosCMX.where(datosCMX['TRANSPORTE'] == 'Trolebús')
datpst2 = datpst2.dropna(subset='TRANSPORTE')
datpst2['Trole'] = datpst2['Pasajeros transportados']
datosjoinCDMX = pd.concat([datost1, datpst2], axis=0, ignore_index=True)
resultado_anova04 = f_oneway(datost1['TrenLigero'], datpst2['Trole'])
resultado_anova4 = f_oneway(datosjoinCDMX['Pasajeros transportados'], datosjoinCDMX['UNIDADES_OPERANDO'])

print("ANOVA CDMX Tren ligero - Trolebus: ",resultado_anova4)
resultado(resultado_anova4)
print("ANOVA CDMX Tren ligero y Trolebus - Unidades Operando: ",resultado_anova4)
resultado(resultado_anova4)

datosCMX = datos.where(datos['ID_ENTIDAD'] == 9)
datost1 = datosCMX.where(datosCMX['TRANSPORTE'] == 'Red de Transporte de Pasajeros')
datost1 = datost1.dropna(subset='ID_ENTIDAD')
datost1['Bus'] = datost1['Pasajeros transportados']
datpst2 = datosCMX.where(datosCMX['TRANSPORTE'] == 'Sistema de Transporte Colectivo Metro')
datpst2 = datpst2.dropna(subset='TRANSPORTE')
datpst2['Metro'] = datpst2['Pasajeros transportados']
datosjoinCDMX = pd.concat([datost1, datpst2], axis=0, ignore_index=True)

resultado_anova04 = f_oneway(datost1['Bus'], datpst2['Metro'])
resultado_anova4 = f_oneway(datosjoinCDMX['Pasajeros transportados'], datosjoinCDMX['UNIDADES_OPERANDO'])

print("ANOVA CDMX Autobus - Metro: ",resultado_anova04)
resultado(resultado_anova04)
print("ANOVA CDMX Autobus y Metro - Unidades Operando: ",resultado_anova4)
resultado(resultado_anova4)