import streamlit as st
import pandas as pd
import numpy as np



st.title(" Concesionario JACD")

marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Camry', 'Civic', 'F-150', 'Silverado', 'Altima', 'X5', 'C-Class', 'A4', 'Jetta', 'Elantra']
anios = [2018, 2020, 2019, 2017, 2016, 2021, 2018, 2020, 2019, 2017]
precios = np.random.randint(10000, 120000, 10)

df_autos = pd.DataFrame({'Marca': marcas, 'Modelo': modelos, 'Año': anios, 'Precio': precios})
df_autos

# Creamos un DataFrame de ejemplo con información de vehículos

vehiculos_df = pd.DataFrame(df_autos)

# Establecemos la columna 'Modelo' como índice del DataFrame
vehiculos_df.set_index('Marca', inplace=True)

# # Creamos un gráfico de línea con las ventas de los vehículos por año
st.line_chart(vehiculos_df[['Precio']])

st.title("LOG Pandas")
#Seleccionar todas las filas de la columna "marca"
st.subheader(" Listado de las Marcas")
marcas = df_autos.loc[:, 'Marca']
cantidad = marcas.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(marcas)

#Seleccionar las filas de los autos cuyo precio es mayor a $40,000
st.subheader(" Autos con precio mayor a $ 40.000")
precios = df_autos.loc[df_autos['Precio'] > 40000, :]
cantidad = precios.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(precios)


#Seleccionar las filas de los autos que son de la marca "BMW".
st.subheader(" Autos de la marca BMW")
bmw = df_autos.loc[df_autos['Marca'] == 'BMW', :]
cantidad = bmw.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(bmw)

#Seleccionar las filas de los autos que son de la marca "Toyota" y tienen un precio menor a $20,000
st.subheader(" Autos de la marca BMW Toyota con precio menor a $20,000")
toyota = df_autos.loc[(df_autos['Marca'] == 'Toyota') & (df_autos['Precio'] < 20000), :]
cantidad = toyota.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(toyota)

#Seleccionar las filas de los autos que son del año 2019
st.subheader(" Autos del año 2019")
modelo = df_autos.loc[df_autos['Año'] == 2019, :]
cantidad = modelo.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(modelo)

#Seleccionar las filas de los autos que son del año 2016 o anteriores.
st.subheader(" Autos del año 2016 o anteriores")
modelo = df_autos.loc[df_autos['Año'] <= 2016, :]
cantidad = modelo.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(modelo)

#Seleccionar las filas de los autos que son de la marca "Honda" y el modelo es "Civic".
st.subheader(" Autos Honda Civic")
hondaCivic = df_autos.loc[(df_autos['Marca'] == 'Honda') & (df_autos['Modelo'] == 'Civic'), :]
cantidad = hondaCivic.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(hondaCivic)

#Seleccionar las filas de los autos que tienen un precio entre $25,000 y $30,000.
st.subheader(" Autos con precios entre $25.000 y $30.000")
precios = df_autos.loc[(df_autos['Precio'] > 25000) & (df_autos['Precio'] <= 30000) , :]
cantidad = precios.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(precios)

#Seleccionar las filas de los autos que tienen un precio mayor a $30,000 y el modelo es "C-Class"
st.subheader(" Autos con precios mayor a $30.000 y modelo es C-Class")
preciosmodelo = df_autos.loc[(df_autos['Precio'] > 30000) & (df_autos['Modelo'] == 'C-Class') , :]
cantidad = preciosmodelo.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(preciosmodelo)

#Seleccionar las filas de los autos que son de la marca "Volkswagen" y el modelo no es "Jetta".
st.subheader(" Autos Volkswagen Jetta")
volkwagenjetta = df_autos.loc[(df_autos['Marca'] == 'Volkswagen') & (df_autos['Modelo'] == 'Jetta'), :]
cantidad = volkwagenjetta.shape[0]
st.write("El total de Autos es: ", cantidad)
st.dataframe(volkwagenjetta)