import pandas as pd
import openpyxl 

#Crear una variable con la base de datos de Excel:
BD = pd.read_excel(r"C:\Andres\Estudio\GIScience\Python para SIG\Programas\Base_Datos_Geoespacial_Pandas.xlsx", sheet_name=1)

print("1) Descripción del dataframe:")
print(BD.head()) #Visualización de las primeras cinco filas del DataFrame
print(BD.tail()) #Visualización de las últimas cinco filas del DataFrame

print(BD.shape) #Muestra el número de filas y columnas del DataFrame
print(BD.shape[0]) #Muestra el número de filas del DataFrame
print(BD.shape[1]) #Muestra el número de columnas del DataFrame

print(BD.columns) #Muestra los nombres de las columnas de un DataFrame en la forma de un objeto indexado

print("2) Información sobre los datos:")
print(BD.info()) #Muestra información sobre los tipos de datos, los valores faltantes y el tamaño de los datos del DataFrame 

print("3) Estadísticas:")

print(BD.describe()) #Visualización de estadísticas de las columnas (atributos) numéricas
print(BD.describe(percentiles=[0.3, 0.5, 0.7])) #Modificar los cuartiles con el argumento percentiles: especificar percentiles 30%, 50% y 70%
print(BD.describe().T) #Lo mismo que BD.describe(), pero con las estadísticas traspuestas



