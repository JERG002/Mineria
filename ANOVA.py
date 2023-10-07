import pandas as pd
from scipy.stats import f_oneway

def resultado(resultadoAnova):
    if resultadoAnova.pvalue < 0.05:
        print("Hay diferencias significativas entre al menos dos grupos.\n")
    else:
        print("No hay diferencias significativas entre los grupos.\n")

datos = pd.read_csv('TransporteNL_Limpio.csv')

datos = datos.drop(datos[(datos['Pasajeros transportados'] == 0) | (datos['UNIDADES_OPERANDO'] == 0) | (datos['Kilómetros recorridos'] == 0)].index)

datosMetrorrey = datos.where(datos['TRANSPORTE'] == 'Metrorrey')
datosMetrorrey = datosMetrorrey.dropna()

datosTrenLigero = datos.where(datos['TRANSPORTE'] == 'Tren Ligero')
datosTrenLigero = datosTrenLigero.dropna()

datosMetroCDMX = datos.where(datos['TRANSPORTE'] == 'Sistema de Transporte Colectivo Metro')
datosMetroCDMX = datosMetroCDMX.dropna()

datosTrolebus = datos.where(datos['TRANSPORTE'] == 'Trolebús')
datosTrolebus = datosTrolebus.dropna()

datosTransmetroNL = datos.where(datos['TRANSPORTE'] == 'Transmetro')
datosTransmetroNL = datosTransmetroNL.dropna()

datosMetrobus = datos.where(datos['TRANSPORTE'] == 'Metrobús')
datosMetrobus = datosMetrobus.dropna()

datosBusCDMX = datos.where(datos['TRANSPORTE'] == 'Red de transporte de pasajeros')
datosBusCDMX = datosBusCDMX.dropna()

datosCablebus = datos.where(datos['TRANSPORTE'] == 'Cablebús')
datosCablebus = datosCablebus.dropna()

datosTrenSub = datos.where(datos['TRANSPORTE'] == 'Tren Suburbano')
datosTrenSub = datosTrenSub.dropna()

datosTrenEle = datos.where(datos['TRANSPORTE'] == 'Tren Eléctrico')
datosTrenEle = datosTrenEle.dropna()

datosEcovia = datos.where(datos['TRANSPORTE'] == 'Ecovía')
datosEcovia = datosEcovia.dropna()

datosViveBus = datos.where(datos['TRANSPORTE'] == 'Vivebús')
datosViveBus = datosViveBus.dropna()

datosMexiBus = datos.where(datos['TRANSPORTE'] == 'Mexibús')
datosMexiBus = datosMexiBus.dropna()

datosMexicable = datos.where(datos['TRANSPORTE'] == 'Mexicable')
datosMexicable = datosMexicable.dropna()

datosQbus = datos.where(datos['TRANSPORTE'] == 'Qrobús')
datosQbus = datosQbus.dropna()

datosOptibus = datos.where(datos['TRANSPORTE'] == 'Optibús')
datosOptibus = datosOptibus.dropna()



resultado_anova1 = f_oneway(datosMetroCDMX['Pasajeros transportados'], datosMetrorrey['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosMetroCDMX['UNIDADES_OPERANDO'], datosMetrorrey['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosTransmetroNL['Pasajeros transportados'], datosMetrobus['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosTransmetroNL['UNIDADES_OPERANDO'], datosMetrobus['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosEcovia['Pasajeros transportados'], datosMetrobus['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosEcovia['UNIDADES_OPERANDO'], datosMetrobus['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosEcovia['Pasajeros transportados'], datosTransmetroNL['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosEcovia['UNIDADES_OPERANDO'],datosTransmetroNL['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosMexiBus['Pasajeros transportados'], datosOptibus['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosMexiBus['UNIDADES_OPERANDO'],datosOptibus['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosCablebus['Pasajeros transportados'], datosOptibus['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosCablebus['UNIDADES_OPERANDO'],datosOptibus['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosCablebus['Pasajeros transportados'], datosMexiBus['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosCablebus['UNIDADES_OPERANDO'],datosMexiBus['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosCablebus['Pasajeros transportados'], datosMexicable['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosCablebus['UNIDADES_OPERANDO'], datosMexicable['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosMexiBus['Pasajeros transportados'], datosMexicable['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosMexiBus['UNIDADES_OPERANDO'], datosMexicable['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosTrenLigero['Pasajeros transportados'], datosTrenEle['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosTrenLigero['UNIDADES_OPERANDO'], datosTrenEle['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosTrenSub['Pasajeros transportados'], datosTrenEle['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosTrenSub['UNIDADES_OPERANDO'], datosTrenEle['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosTrenSub['Pasajeros transportados'], datosTrenLigero['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosTrenSub['UNIDADES_OPERANDO'], datosTrenLigero['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)

resultado_anova1 = f_oneway(datosTrenSub['Pasajeros transportados'], datosMetrorrey['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosTrenSub['UNIDADES_OPERANDO'], datosMetrorrey['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)


resultado_anova1 = f_oneway(datosTrenSub['Pasajeros transportados'], datosMetroCDMX['Pasajeros transportados'])
resultado_anova2 = f_oneway(datosTrenSub['UNIDADES_OPERANDO'], datosMetroCDMX['UNIDADES_OPERANDO'])
print("ANOVA Pasajeros Metrorrey - Metro CDMX: ",resultado_anova1)
resultado(resultado_anova1)
print("ANOVA Unidades Metrorrey - Metro CDMX: ",resultado_anova2)
resultado(resultado_anova2)