import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.header('Construir Histograma')

if hist_button:
    st.write('Crea un histograma para el conjunto de datos de la venta de automoviles')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

disp_buttom = st.header('Construir un gráfico de dispersión')

if disp_buttom:
    st.write('creación de un gráfico de dispresión para la venta de automoviles')
    disper = px.scatter(car_data, x='odometer')
    st.plotly_chart(disper, use_container_width=True)