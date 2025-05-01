# pages/1_Estudio_Esperanza_de_Vida_ACP.py
import streamlit as st
import pandas as pd
import numpy as np
import random
import os
import json

st.set_page_config(page_title="ACP - Esperanza de Vida")

# Mostrar logo en todo el examen
top_logo = "logo_usta.jpg"
if os.path.exists(top_logo):
    st.image(top_logo, width=320)

st.title("Análisis de Esperanza de Vida y Factores de Salud (ACP)")

if "student_id" not in st.session_state:
    st.error("Por favor, regrese a la página principal e ingrese su ID.")
    st.stop()

student_id = st.session_state.student_id
random.seed(student_id)

# Cargar el dataset
df_full = pd.read_csv("datasets/esperanza_vida.csv")

# Muestreo reproducible para cada estudiante
sample_size = round(df_full.shape[0]*0.2)
np.random.seed(sum([ord(c) for c in student_id]))
df_student = df_full.sample(n=sample_size, random_state=np.random.randint(0, 1e6)).reset_index(drop=True)

# Permitir descarga
st.download_button("Descargar dataset en CSV", df_student.to_csv(index=False), file_name="esperanza_vida_estudiante.csv")

st.subheader("Contexto del problema")
st.markdown("""
La Organización Mundial de la Salud ha recolectado indicadores de salud pública y económica en distintos países, tales como tasas de mortalidad, gasto público en salud, inmunización infantil, y otros factores que afectan la esperanza de vida.

El objetivo es identificar patrones entre estos indicadores que expliquen la variabilidad en la esperanza de vida.
""")

st.subheader("Instrucciones")
st.markdown("""
1. Realice un análisis exploratorio de los indicadores.
2. Aplique el Análisis de Componentes Principales (ACP) sobre las variables numéricas activas.
3. Puede considerar variables suplementarias como el país o región si están disponibles.
4. Interprete las dos primeras componentes principales.
5. Genere y adjunte el plano factorial de individuos y variables.
6. Concluya sobre los factores que más inciden en la esperanza de vida.
7. **Suba un único archivo con sus respuestas en formato PDF o Markdown (.md).**
""")

archivo = st.file_uploader("Suba aquí su archivo de respuestas (PDF o Markdown):", type=["pdf", "md"])

if archivo is not None:
    carpeta_respuestas = "respuestas"
    os.makedirs(carpeta_respuestas, exist_ok=True)
    nombre_archivo = f"respuestas/respuestas_{student_id}_acp.{archivo.name.split('.')[-1]}"
    with open(nombre_archivo, "wb") as f:
        f.write(archivo.getbuffer())
    st.success("Archivo cargado correctamente. Puede continuar con los demás ejercicios.")
