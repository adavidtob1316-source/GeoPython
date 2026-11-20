import geopandas as gpd
import matplotlib.pyplot as plt

#Abrir archivo shapefile y guardarlo en una variable:
shapefile = gpd.read_file(r"ruta de archivo")

#Desplegar la variable:
print(shapefile)

#Averiguar el tipo de variable:
print(type(shapefile))

print(shapefile.crs) #Despliega el CRS

print(shapefile.plot(color="red", edgecolor="black"))

plt.show()
