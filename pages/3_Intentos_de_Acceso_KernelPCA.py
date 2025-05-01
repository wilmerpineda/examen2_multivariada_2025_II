# pages/3_Intentos_de_Acceso_KernelPCA.py
import streamlit as st
import pandas as pd
import numpy as np
import random
import os

st.set_page_config(page_title="Kernel PCA - Ionosfera")

# Mostrar logo en todo el examen
top_logo = "logo_usta.jpg"
if os.path.exists(top_logo):
    st.image(top_logo, width=320)

st.title("Segmentación de Señales de Radar mediante Kernel PCA")

if "student_id" not in st.session_state:
    st.error("Por favor, regrese a la página principal e ingrese su ID.")
    st.stop()

student_id = st.session_state.student_id
random.seed(student_id)

# Leer los datos
columnas = [f"V{i+1}" for i in range(34)] + ["target"]
data_path = "datasets/ionosphere.data"
df_full = pd.read_csv(data_path, header=None, names=columnas)

# Convertir clase 'g' (good) -> 1 y 'b' (bad) -> 0
df_full["target"] = df_full["target"].map({"g": 1, "b": 0})
df_full = df_full.dropna()

# Muestreo reproducible para el estudiante
sample_size = 200
np.random.seed(sum([ord(c) for c in student_id]))
df_student = df_full.sample(n=sample_size, random_state=np.random.randint(0, 1e6)).reset_index(drop=True)

# Permitir descarga del dataset personalizado
st.download_button("Descargar dataset en CSV", df_student.to_csv(index=False), file_name="ionosfera_estudiante.csv")

st.subheader("Contexto del problema")
st.markdown("""
Una empresa aeroespacial recolectó datos de radar reflejados por la ionosfera. Cada observación representa una serie de señales captadas por 34 sensores. El objetivo es identificar si la señal es 'buena' (estructura detectable) o 'mala' (ruido).

El problema es no lineal, por lo que se desea aplicar Kernel PCA para mejorar la visualización y segmentación de los casos.
""")

st.subheader("Instrucciones")
st.markdown("""
1. Realice un análisis exploratorio básico de las variables numéricas.
2. Aplique Kernel PCA usando al menos tres funciones kernel distintas (`linear`, `poly`, `rbf`).
3. Reduzca la dimensionalidad a 2 y grafique los datos coloreando por la variable `target`.
4. Compare la segmentación lograda con cada kernel.
5. Prepare su interpretación y análisis en un único archivo `.pdf` o `.md` y súbalo a continuación.
""")

archivo = st.file_uploader("Suba aquí su archivo de respuestas (PDF o Markdown):", type=["pdf", "md"])
if archivo is not None:
    extension = archivo.name.split(".")[-1]
    filename = f"respuestas/respuestas_{student_id}_kpca.{extension}"
    with open(filename, "wb") as f:
        f.write(archivo.getbuffer())
    st.success("Archivo cargado correctamente.")
