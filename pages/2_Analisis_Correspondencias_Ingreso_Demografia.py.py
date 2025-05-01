# pages/2_Analisis_Correspondencias_Ingreso_Demografia.py
import streamlit as st
import pandas as pd
import numpy as np
import random
import os

st.set_page_config(page_title="CA - Ingreso y Demografía")

# Mostrar logo en todo el examen
top_logo = "logo_usta.jpg"
if os.path.exists(top_logo):
    st.image(top_logo, width=320)

st.title("Relación entre Ingresos y Variables Demográficas (Análisis de Correspondencias)")

if "student_id" not in st.session_state:
    st.error("Por favor, regrese a la página principal e ingrese su ID.")
    st.stop()

student_id = st.session_state.student_id
random.seed(student_id)

# Variables posibles
variables_posibles = ["gender", "workclass", "marital-status", "race"]
var_seleccionada = random.choice(variables_posibles)

# Cargar y muestrear el dataset
full_df = pd.read_csv("datasets/adult.csv")
columns_needed = [var_seleccionada, "income"]
df = full_df[columns_needed].dropna()
sample_size = round(df.shape[0]*0.6)
np.random.seed(sum([ord(c) for c in student_id]))
df_sample = df.sample(n=sample_size, random_state=np.random.randint(0, 1e6)).reset_index(drop=True)

# Descargar dataset personalizado
st.download_button("Descargar dataset en CSV", df_sample.to_csv(index=False), file_name="ingresos_demografia_estudiante.csv")

st.subheader("Contexto del problema")
st.markdown(f"""
Se desea estudiar la relación entre la variable de ingresos (`income`) y una característica demográfica aleatoria.

En tu caso, se ha seleccionado la variable **`{var_seleccionada}`** para compararla con `income` mediante análisis de correspondencias.
""")

st.subheader("Instrucciones")
st.markdown(f"""
1. Construya una **tabla de contingencia** entre `{var_seleccionada}` e `income`.
2. Realice una **prueba Chi-cuadrado de independencia**.
3. Aplique el **análisis de correspondencias** y genere el gráfico del plano factorial.
4. Interprete la proximidad entre categorías.
5. Prepare su respuesta en un único archivo `.pdf` o `.md` y súbalo a continuación.
""")

archivo = st.file_uploader("Suba aquí su archivo de respuestas (PDF o Markdown):", type=["pdf", "md"])
if archivo is not None:
    path = f"respuestas/respuestas_{student_id}_ca.{archivo.name.split('.')[-1]}"
    with open(path, "wb") as f:
        f.write(archivo.getbuffer())
    st.success("Archivo cargado correctamente. Puede continuar con los demás ejercicios.")