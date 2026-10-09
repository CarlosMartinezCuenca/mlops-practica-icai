import numpy as np

import os 
import json
import requests

import streamlit as st

# Título de la aplicación
st.title("API de Predicción del Modelo Iris")

# Descripción de la aplicación
st.write("Ingresa las características de la flor Iris para obtener una predicción de su especie.")

# Campos de entrada para las características del iris
sepal_length = st.slider('Longitud del sépalo (cm)', 0.0, 10.0, 5.0)
sepal_width = st.slider('Anchura del sépalo (cm)', 0.0, 10.0, 3.0)
petal_length = st.slider('Longitud del pétalo (cm)', 0.0, 10.0, 4.0)
petal_width = st.slider('Anchura del pétalo (cm)', 0.0, 10.0, 1.0)

# Botón para hacer predicción
if st.button('Obtener Predicción'):
    # Crear datos en formato JSON
    features = [sepal_length, sepal_width, petal_length, petal_width]
    payload = {'features': features}

    # URL de la API
    api_url = os.environ.get('API_URL')

    try:
        # Hacer la solicitud POST a la API
        response = requests.post(api_url, json=payload, headers={'Content-Type': 'application/json'})


        # Verificar la respuesta de la API
        if response.status_code == 200:
            prediction_result = response.json().get('prediction')

            # Mapear el resultado numérico a la especie correspondiente
            species_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
            prediction_species = species_map.get(prediction_result, 'Especie desconocida')
            
            st.success(f'La predicción de la especie es: {prediction_species}')
        else:
            st.error(f"Error en la petición: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"No se pudo conectar con la API. Asegúrate de que está en ejecución. Error: {e}")