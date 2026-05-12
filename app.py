import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import datetime

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO (Literal y Minimalista)
st.set_page_config(page_title="HIGO - Movilidad Autónoma", page_icon="📍", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #F8F9FA; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; font-weight: bold; }
    .stAlert { border: 1px solid #000; }
    h1, h2, h3 { color: #1A1A1A; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. PERSISTENCIA DE ESTADO (Marc Session State)
if 'step' not in st.session_state:
    st.session_state.step = "setup"
if 'incidencia_activa' not in st.session_state:
    st.session_state.incidencia_activa = False

# 3. MOCK DATA: RUTAS SENSORIALES
def get_route_data():
    return {
        "Ruta Habitual": {"ruido": "Bajo", "luz": "Natural", "puntos_descanso": 2, "instrucciones": ["Salida A", "Pasillo Izquierdo", "Vagón Final"]},
        "Ruta Espejo (Contingencia)": {"ruido": "Medio-Bajo", "luz": "LED Suave", "puntos_descanso": 3, "instrucciones": ["Bus 24 (Vacio)", "Parada Parques", "Caminar 5 min"]}
    }

# 4. LÓGICA DE INTERFAZ
st.title("HIGO")
st.caption("Asistente de movilidad predictiva | Usuario: Marc")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Estado del Trayecto")
    
    if not st.session_state.incidencia_activa:
        st.success("✅ Todo despejado. Tu ruta habitual es segura.")
        if st.button("Simular Incidencia en Metro"):
            st.session_state.incidencia_activa = True
            st.rerun()
    else:
        st.error("⚠️ INCIDENCIA DETECTADA: Retraso en Línea 1")
        st.warning("**Instrucción Literal:** No entres al andén. El ruido subirá por aglomeración. Cambia a 'Ruta Espejo'.")
        if st.button("Aceptar Ruta Segura"):
            st.info("🔄 Re-calculando paso a paso...")

with col2:
    # Render de Mapa
    m = folium.Map(location=[40.4167, -3.7037], zoom_start=14, tiles="cartodbpositron")
    # Simulación de zona de alta carga sensorial
    folium.Circle(location=[40.418, -3.705], radius=200, color="red", fill=True, popup="Zona Ruidosa").add_to(m)
    st_folium(m, width=700, height=450)

# 5. PASO A PASO (Estructuración Cognitiva)
st.divider()
st.subheader("Instrucciones Paso a Paso")
route = get_route_data()["Ruta Espejo (Contingencia)" if st.session_state.incidencia_activa else "Ruta Habitual"]

for i, inst in enumerate(route["instrucciones"]):
    st.info(f"**Paso {i+1}:** {inst}")

# Footer de Seguridad
st.sidebar.markdown("### Soporte Crítico")
st.sidebar.button("🆘 Necesito Ayuda")
st.sidebar.button("🏠 Volver a Casa (Ruta Segura)")
