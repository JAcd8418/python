import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de insectos
mosca = 100
hormiga = 50 
mariposa = 20
escarabajo = 30

# Categorías de insectos
insectos = ['Moscas', 'Hormigas', 'Mariposas', 'Escarabajos']

# Frecuencia de insectos
frecuencias = [mosca, hormiga, mariposa, escarabajo]

# Crear el gráfico 
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)  
ax.bar(insectos, frecuencias)

# Mostrar el gráfico  
st.pyplot(fig)


import streamlit as st
import pandas as pd 
import requests

# API URL
url = "https://api-colombia.com/api/v1/President"
st.subheader("Presidentes de Colombia 1886-2023")
# Get response
response = requests.get(url)

# Check status code
if response.status_code == 200:

    # Get data
    data = response.json()
    
    # Create list of dicts from data 
    presidents = [{
        "Nombre": d["name"],
        "Apellido": d["lastName"],
        "Periodo Inicial": d["startPeriodDate"],
        "Periodo Final": d["endPeriodDate"],  
    } for d in data]
    
    # Create DataFrame 
    df = pd.DataFrame(presidents)
    df    
    
else:
    st.error("Ocurrió un error")
