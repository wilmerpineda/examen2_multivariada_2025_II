# pages/4_Preferencias_Terapias_ACM.py
import streamlit as st
import pandas as pd
import numpy as np
import random
import os

st.set_page_config(page_title="ACM - Preferencias Categóricas")

# Mostrar logo en todo el examen
top_logo = "logo_usta.jpg"
if os.path.exists(top_logo):
    st.image(top_logo, width=320)

st.title("Relaciones entre Variables Categóricas (Análisis de Correspondencias Múltiples)")

if "student_id" not in st.session_state:
    st.error("Por favor, regrese a la página principal e ingrese su ID.")
    st.stop()

student_id = st.session_state.student_id
random.seed(student_id)

# Cargar el dataset
column_names = ["color", "size", "act", "age", "inflated"]
df_full = pd.read_csv("datasets/adult+stretch.data", header=None, names=column_names)

# Muestreo reproducible CON reemplazo
sample_size = 100
np.random.seed(sum([ord(c) for c in student_id]))
df_student = df_full.sample(n=sample_size, replace=True, random_state=np.random.randint(0, 1e6)).reset_index(drop=True)

# Descargar CSV personalizado
st.download_button("Descargar dataset en CSV", df_student.to_csv(index=False), file_name="acm_balloons_estudiante.csv")

st.subheader("Contexto del problema")
st.markdown("""
Este conjunto de datos describe condiciones categóricas bajo las cuales se infla un globo. Las variables incluyen color, tamaño, acción realizada y edad del sujeto. El objetivo es analizar las asociaciones entre estas variables utilizando ACM.
""")

st.subheader("Instrucciones")
st.markdown("""
1. Realice un análisis exploratorio básico (tablas de frecuencia).
2. Aplique el Análisis de Correspondencias Múltiples (ACM).
3. Genere el plano factorial con individuos y categorías.
4. Interprete agrupamientos y relaciones entre categorías.
5. Suba un archivo `.pdf` o `.md` con su interpretación y gráficos.
""")

archivo = st.file_uploader("Suba aquí su archivo de respuestas (PDF o Markdown):", type=["pdf", "md"])
if archivo is not None:
    extension = archivo.name.split(".")[-1]
    path = f"respuestas/respuestas_{student_id}_acm.{extension}"
    with open(path, "wb") as f:
        f.write(archivo.getbuffer())
    st.success("Archivo cargado correctamente.")