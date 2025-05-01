# app.py
import streamlit as st
from datetime import datetime, timezone, timedelta
import os
import json

st.set_page_config(page_title="Examen de Estadística Multivariada")

# Mostrar logo en todo el examen
top_logo = "logo_usta.jpg"
if os.path.exists(top_logo):
    st.image(top_logo, width=320)

st.title("Examen Interactivo de Estadística Multivariada")

# Ruta donde se guardarán los metadatos de los estudiantes
data_dir = "respuestas"
os.makedirs(data_dir, exist_ok=True)

# Fecha y hora límite absoluta (UTC-5)
limite_absoluto = datetime(2025, 5, 5, 4, 59, 59, tzinfo=timezone.utc)
ahora = datetime.now(timezone.utc)
if ahora > limite_absoluto:
    st.error("El examen ha cerrado: no se permiten entregas después del 4 de mayo de 2025, 11:59 pm (UTC-5).")
    st.stop()

# Registro del estudiante y manejo del tiempo de acceso
st.header("Registro del Estudiante")
student_id = st.text_input("Por favor, ingrese su código o identificación para comenzar el examen:")

if student_id:
    meta_path = os.path.join(data_dir, f"meta_{student_id}.json")

    if os.path.exists(meta_path):
        with open(meta_path) as f:
            meta = json.load(f)
        start_time = datetime.fromisoformat(meta["start_time"])
    else:
        start_time = datetime.now()
        meta = {"start_time": start_time.isoformat()}
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=4)

    elapsed = datetime.now() - start_time
    remaining = timedelta(days=3) - elapsed

    if remaining.total_seconds() <= 0:
        st.error("El tiempo límite de 3 días ha expirado para este ID. Contacte al profesor si necesita soporte.")
        st.stop()

    # Guardar ID en sesión para las otras páginas
    st.session_state.student_id = student_id

    st.success(f"Bienvenido/a, ID registrado: {student_id}")

    # Mostrar tiempo restante
    dias = remaining.days
    horas, rem = divmod(remaining.seconds, 3600)
    minutos, _ = divmod(rem, 60)
    st.warning(f"Tiempo restante: {dias} días, {horas} h, {minutos} min")

    st.markdown("""
    ---
    # Instrucciones Generales
    - Este examen consta de **5 partes**: 4 ejercicios prácticos y 1 conjunto de preguntas conceptuales.
    - Tienes **3 días** desde tu primer acceso para completarlo, y no más allá del **4 de mayo de 2025 a las 11:59pm (UTC-5)**.
    - Cada ejercicio tiene una **página propia**, accesible desde el menú lateral.
    - En cada ejercicio:
        - Descarga tu dataset personalizado.
        - Realiza el análisis según las instrucciones.
        - Guarda tus respuestas directamente desde la interfaz.
    - Recuerda interpretar los resultados y adjuntar gráficos cuando se solicite.
    ---
    """)

else:
    st.info("Ingresa tu identificación para comenzar. El temporizador de 3 días iniciará en cuanto ingreses.")