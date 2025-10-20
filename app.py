import streamlit as st
import tensorflow as tf
import numpy as np

st.set_page_config(page_title="Predicción Académica", page_icon="🎓", layout="centered")

st.title("🎓 Predicción del Rendimiento Académico")
st.write("Introduce los datos del estudiante para estimar su posible rendimiento académico.")

# --- Cargar modelo ---
@st.cache_resource
def cargar_modelo():
    modelo = tf.keras.models.load_model("modelo_rendimiento.h5")
    return modelo

modelo = cargar_modelo()

# --- Entradas del usuario ---
nivel = st.selectbox("Nivel educativo", ["Primaria", "Secundaria"])
situacion = st.selectbox("Situación socioeconómica", ["Baja", "Media baja", "Media", "Media alta", "Alta"])
motivacion = st.selectbox("Nivel de motivación", ["Muy baja", "Baja", "Media", "Alta", "Muy alta"])
responsabilidad = st.selectbox("Responsabilidad", ["Baja", "Media", "Alta", "Muy alta"])

# Mapeos
nivel_map = {"primaria": 0, "secundaria": 1}
situ_map = {"baja": 1, "media baja": 2, "media": 3, "media alta": 4, "alta": 5}
motiv_map = {"muy baja": 1, "baja": 2, "media": 3, "alta": 4, "muy alta": 5}
resp_map = {"baja": 1, "media": 2, "alta": 3, "muy alta": 4}

# Preparar datos
x_input = np.array([[ 
    nivel_map[nivel.lower()],
    situ_map[situacion.lower()],
    motiv_map[motivacion.lower()],
    resp_map[responsabilidad.lower()]
]])

# Botón
if st.button("🔍 Predecir rendimiento"):
    pred = modelo.predict(x_input)
    pred_value = float(pred[0][0])

    st.success(f"El rendimiento estimado es: **{pred_value:.2f}**")

    if pred_value < 0.4:
        st.error("⚠️ Bajo rendimiento académico.")
    elif pred_value < 0.7:
        st.warning("🟡 Rendimiento medio.")
    else:
        st.balloons()
        st.info("✅ Buen rendimiento académico.")
