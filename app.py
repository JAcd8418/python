import streamlit as st

st.title("Data set´s ")




from PIL import Image

image = Image.open('movilidad.jpg')

st.image(image, caption='Movilidad en Medellín')

from PIL import Image

image = Image.open('fifa-logo0.gif')

st.image(image, caption='Jugadores FIFA 2023')


