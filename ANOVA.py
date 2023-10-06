import pandas as pd
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.multivariate.manova import MANOVA

datos = pd.read_csv('TransporteNL_Limpio.csv')
datos['FECHA'] = pd.to_datetime(datos.FECHA, format='%Y-%m-%d %H:%M:%S')
datos['ANIO'] = datos['FECHA'].dt.year


grupo_pasajeros_transportados = [grupo['Pasajeros transportados'].tolist() for _, grupo in datos.groupby('TRANSPORTE')]
resultado_anova_pasajeros = f_oneway(*grupo_pasajeros_transportados)
print("Resultados ANOVA para Pasajeros Transportados:")
print(resultado_anova_pasajeros)


grupo_unidades_operando = [grupo['UNIDADES_OPERANDO'].tolist() for _, grupo in datos.groupby('ID_ENTIDAD')]
resultado_anova_unidades = f_oneway(*grupo_unidades_operando)
print("Resultados ANOVA para Unidades Operando:")
print(resultado_anova_unidades)



grupo_kilometros_recorridos = [grupo['Kilómetros recorridos'].tolist() for _, grupo in datos.groupby('ANIO')]
resultado_anova_kilometros = f_oneway(*grupo_kilometros_recorridos)
print("Resultados ANOVA para Kilómetros Recorridos:")
print(resultado_anova_kilometros)

datos['Pasajeros'] = datos['Pasajeros transportados']
datos['Kilometros'] = datos['Kilómetros recorridos']


variables = ['Pasajeros', 'Kilometros', 'UNIDADES_OPERANDO']
datos['grupo'] = datos['TRANSPORTE']

manova = MANOVA.from_formula(formula='Pasajeros + Kilometros + UNIDADES_OPERANDO ~ grupo', data=datos)
resultados_manova = manova.mv_test()

# Muestra los resultados
print(resultados_manova)

#El resultado del Pvalor en las pruebas ANOVA es muy cercano al 0, por lo tanto las diferencias entre algunas de las medias son estadísticamente significativas

print("Las diferencias entre las medias SON ESTADISTICAMENTE SIGNIFICATIVAS")