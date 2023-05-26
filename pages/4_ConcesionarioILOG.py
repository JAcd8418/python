import streamlit as st
import pandas as pd
import numpy as np

st.title(" Concesionario JACD")

data = marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Camry', 'Civic', 'F-150', 'Silverado', 'Altima', 'X5', 'C-Class', 'A4', 'Jetta', 'Elantra']
anios = [2018, 2020, 2019, 2017, 2016, 2021, 2018, 2020, 2019, 2017]
precios = np.random.randint(15000, 50000, 10)

df_autos = pd.DataFrame({'Marca': marcas, 'Modelo': modelos, 'Año': anios, 'Precio': precios})

# Mostrar el DataFrame

st.dataframe(df_autos)

st.title("I-LOG Pandas")

#Seleccionar las filas de los autos de los primeros 5 fabricantes en el DataFrame.
st.subheader(" Autos de los 5 primeros fabricantes")
dato = df_autos.iloc[0:5, :]
st.dataframe(dato)

#Seleccionar las filas de los autos de los últimos 5 fabricantes en el DataFrame
st.subheader(" Autos de los 5 ultimos fabricantes")
dato = df_autos.iloc[5:10, :]
st.dataframe(dato)

#Seleccionar la primera columna de todas las filas del DataFrame
st.subheader("Listado de las Marcas ")
dato = df_autos.iloc[:, 0 ]
st.dataframe(dato)

#Seleccionar las filas pares del DataFrame
st.subheader("las filas pares ")
pares = df_autos.iloc[::2, :]
st.dataframe(pares)

#Seleccionar las filas impares del DataFrame que tienen un precio mayor a $25,000
st.subheader("las filas impares con precio mayos a $25.000 ")
impares = df_autos.iloc[1::2, :][df_autos['Precio'] > 25000]
st.dataframe(impares)

#Seleccionar las filas de los autos que son de la marca "Ford" y el modelo es "F-150"
st.subheader("Autos Ford F-150")
dato = df_autos.iloc[2::1][df_autos['Modelo']=='F-150']
st.dataframe(dato)