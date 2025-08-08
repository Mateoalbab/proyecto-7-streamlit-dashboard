# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuración Inicial y Carga de Datos ---

# Título de la aplicación web
st.header('Análisis Exploratorio de Datos de Anuncios de Venta de Coches')

# Cargar el dataset
try:
    car_data = pd.read_csv('vehicles_us.csv')
    st.write("Dataset cargado correctamente.")
except FileNotFoundError:
    st.error("Error: No se pudo encontrar el archivo 'vehicles_us.csv'. Asegúrate de que esté en el directorio correcto.")

# --- Aquí añadiremos los componentes interactivos ---

# --- Creación de Gráficos con Botones ---

# Botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Si el botón es presionado
    # Escribir un mensaje de confirmación
    st.write('Creación de un histograma para la columna odómetro')

    # Crear el histograma con Plotly Express
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Si el botón es presionado
    # Escribir un mensaje de confirmación
    st.write('Creación de un gráfico de dispersión para odómetro vs. precio')

    # Crear el gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
