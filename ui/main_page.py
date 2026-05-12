"""
Componentes de la interfaz de usuario principal para HIGO.
"""
import streamlit as st
from logic.navigation import evaluar_seguridad_tramo, obtener_instruccion_literal
from data.database import registrar_evento

def render_interface():
    st.title("📍 HIGO")
    st.subheader("Guía de Movilidad para Marc")

    # Simulación de sensor (Input de usuario para el MVP)
    col1, col2 = st.columns(2)
    with col1:
        ruido = st.slider("Nivel de ruido detectado (dB)", 30, 100, 60)
    with col2:
        gente = st.slider("Ocupación estimada", 0.0, 1.0, 0.3)

    es_seguro = evaluar_seguridad_tramo(ruido, gente)
    instruccion = obtener_instruccion_literal(es_seguro, "Línea 1 - Metro")

    if not es_seguro:
        st.error(f"**ACCIÓN REQUERIDA:** {instruccion}")
        if st.button("Reportar Bloqueo y Pedir Ayuda"):
            registrar_evento("Bloqueo Sensorial en Metro", 5)
            st.warning("Ayuda solicitada. Quédate donde estás, un asistente sabe tu posición.")
    else:
        st.success(f"**ESTADO:** {instruccion}")
