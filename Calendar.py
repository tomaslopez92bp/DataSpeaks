####################################################################################
from google.oauth2 import service_account
from google.cloud import bigquery
import streamlit as st
from datetime import datetime

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

####################################################################################

# Define la referencia a tu tabla de BigQuery
dataset_id = "ageless-math-320621.Calendar_prueba"
table_id = "calendar_streamlit"
table_ref = f"{dataset_id}.{table_id}"

def insert_data_to_bigquery(start_date, end_date, event):
    
    
    # Crea el diccionario de datos a insertar
    data = [
        {
            "start_date": start_date,
            "end_date": end_date,
            "event": event
        }
    ]

    # Inserta los datos en la tabla de BigQuery
    errors = client.insert_rows(table_ref, data)

    if errors == []:
        st.success("Los datos se insertaron correctamente en BigQuery.")
    else:
        st.error("Ocurrieron errores al insertar los datos en BigQuery.")

####################################################################################
def process_data(start_date, end_date, event):

    # Llama a la función para insertar los datos en BigQuery
    insert_data_to_bigquery(start_date, end_date, event)
####################################################################################
#STREAMLIT

# Título de la aplicación
st.title("Events Calendar - Data Speaks")

# Subtítulo de la aplicación
st.subheader("Please enter the requested data and then press the save button")

# Formulario para ingresar la información del evento
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
event = st.text_input("Event")

# Validación de los valores ingresados por el usuario
if start_date > end_date:
    st.error("Error: Start date cannot be later than end date!")
elif not event:
    st.error("Error: Please enter a valid event! - Event field is empty")
else:
    # Botón para guardar la información del evento
    if st.button("Save Event"):
        # Guardar la información del evento en la base de datos o en un archivo
        process_data(start_date, end_date, event)
        st.success('Los datos se han guardado correctamente en BigQuery.')
