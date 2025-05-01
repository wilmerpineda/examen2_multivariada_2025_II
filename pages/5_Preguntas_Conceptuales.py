# pages/5_Preguntas_Conceptuales.py
import streamlit as st
import json
import os

st.set_page_config(page_title="Preguntas Conceptuales")

# Mostrar logo en todo el examen
top_logo = "logo_usta.jpg"
if os.path.exists(top_logo):
    st.image(top_logo, width=320)

st.title("Preguntas Conceptuales de Estadística Multivariada")

if "student_id" not in st.session_state:
    st.error("Por favor, regrese a la página principal e ingrese su ID.")
    st.stop()

student_id = st.session_state.student_id

st.subheader("1. ¿Cuál de las siguientes afirmaciones sobre el ACP es correcta?")
res1 = st.radio("Seleccione una opción:", [
    "A) El ACP solo puede aplicarse a variables categóricas.",
    "B) Las componentes principales siempre son independientes entre sí.",
    "C) El ACP se basa en maximizar la varianza explicada por cada componente.",
    "D) El ACP requiere una variable dependiente."
], key="preg1")

st.subheader("2. ¿Qué representa una categoría alejada del origen en el plano factorial de CA?")
res2 = st.radio("Seleccione una opción:", [
    "A) Alta contribución a la inercia total.",
    "B) Asociación con muchas categorías.",
    "C) Baja importancia estadística.",
    "D) Alta correlación con todas las variables."
], key="preg2")

st.subheader("3. ¿Qué caracteriza al Kernel PCA respecto al PCA clásico?")
res3 = st.radio("Seleccione una opción:", [
    "A) Utiliza funciones kernel para modelar relaciones no lineales.",
    "B) Usa solo la matriz de covarianza.",
    "C) Solo se aplica a datos categóricos.",
    "D) No permite visualización en 2D."
], key="preg3")

st.subheader("4. ¿Cuál es una limitación típica del Análisis de Correspondencias Múltiples?")
res4 = st.radio("Seleccione una opción:", [
    "A) No puede trabajar con variables categóricas.",
    "B) Pierde validez cuando hay muchas categorías poco frecuentes.",
    "C) No puede representarse gráficamente.",
    "D) Siempre produce resultados lineales."
], key="preg4")

st.subheader("5. ¿Qué indica la proximidad entre dos modalidades en un plano factorial?")
res5 = st.radio("Seleccione una opción:", [
    "A) Que tienen alta varianza.",
    "B) Que tienen alta frecuencia conjunta.",
    "C) Que son independientes.",
    "D) Que están en cuadrantes opuestos."
], key="preg5")

st.subheader("6. El ACP puede ser utilizado para reducir dimensionalidad en datos con muchas variables correlacionadas.")
res6 = st.radio("Seleccione una opción:", ["Verdadero", "Falso"], key="preg6")

st.subheader("7. En CA, las distancias entre puntos reflejan similitud entre categorías.")
res7 = st.radio("Seleccione una opción:", ["Verdadero", "Falso"], key="preg7")

st.subheader("8. El Kernel PCA es siempre mejor que el PCA clásico en todos los casos.")
res8 = st.radio("Seleccione una opción:", ["Verdadero", "Falso"], key="preg8")

st.subheader("9. Explique con sus palabras qué significa que dos categorías estén próximas en un plano factorial de CA o ACM.")
res9 = st.text_area("Respuesta abierta:", key="preg9")

st.subheader("10. ¿En qué situaciones sería preferible usar un análisis de correspondencias múltiples sobre un ACP?")
res10 = st.text_area("Respuesta abierta:", key="preg10")

if st.button("Guardar respuestas conceptuales"):
    respuestas = {
        "id": student_id,
        "ejercicio": "Preguntas Conceptuales",
        "seleccion_multiple": [res1, res2, res3, res4, res5],
        "falso_verdadero": [res6, res7, res8],
        "abiertas": [res9, res10]
    }
    path = f"respuestas/respuestas_{student_id}_conceptual.json"
    with open(path, "w") as f:
        json.dump(respuestas, f, indent=4)
    st.success("Respuestas guardadas correctamente.")