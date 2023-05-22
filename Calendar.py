import streamlit as st
import pandas as pd
import datetime
from google.oauth2 import service_account
from google.cloud import bigquery

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/Zeke/GitHub/DataSpeaks/GoogleCloudAccess.json"
client = bigquery.Client()

# Título de la aplicación
st.title("Events Calendar - Data Speaks")

# Subtítulo de la aplicación
st.subheader("Please enter the requested data and then press the save button")

# Formulario para ingresar la información del evento
start_date = st.date_input("Start Date", value=pd.to_datetime('today').date())
end_date = st.date_input("End Date", value=pd.to_datetime('today').date())
event = st.text_input("Event", value='')

# Validación de los valores ingresados por el usuario
if start_date > end_date:
    st.error("Error: Start date cannot be later than end date!")
elif not event:
    st.error("Error: Please enter a valid event! - Event field is empty")
else:
    # Botón para guardar la información del evento
    if st.button("Save Event"):
        # Guardar la información del evento en la base de datos o en un archivo
        st.success("Event saved successfully!")
