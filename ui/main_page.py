import streamlit as st
import time
from ui.styles import apply_custom_styles
from logic.navigation import evaluar_seguridad_tramo, obtener_instruccion_literal
from data.database import registrar_evento
from config import LBL_CARGANDO, LBL_EXITO_RUTA, LBL_ALERTA_INCIDENCIA, LBL_ACCION_LITERAL

def render_interface():
    apply_custom_styles()
    
    st.title("📍 HIGO")
    st.write("Hola Marc. Tu seguridad es nuestra prioridad hoy.")

    # 1. ESTADO: CONFIGURACIÓN
    with st.expander("⚙️ Ajustes de mi zona de confort", expanded=False):
        st.info("Personaliza tus límites sensoriales para este viaje.")
        sensibilidad = st.select_slider("Sensibilidad al ruido", options=["Baja", "Media", "Alta"])
        
    # 2. MONITOR: EN TIEMPO REAL
    st.divider()
    
    # Simulación de carga para el demo
    with st.status(LBL_CARGANDO, expanded=True) as status:
        st.write("Conectando con sensores de la estación...")
        time.sleep(1)
        st.write("Analizando flujo de pasajeros...")
        time.sleep(0.5)
        status.update(label="Análisis completado", state="complete", expanded=False)

    # Inputs para el demo
    col_a, col_b = st.columns(2)
    with col_a:
        ruido = st.number_input("Ruido actual (dB)", 30, 110, 65, help="Datos en tiempo real del sensor de andén.")
    with col_b:
        gente = st.slider("Flujo de gente", 0.0, 1.0, 0.4, help="Porcentaje de ocupación del vagón.")

    # 3. LÓGICA Y FEEDBACK
    es_seguro = evaluar_seguridad_tramo(ruido, gente)
    
    if es_seguro:
        st.success(f"**{LBL_EXITO_RUTA}**")
        st.balloons() if st.toggle("Modo celebración al llegar") else None
    else:
        st.error(f"**{LBL_ALERTA_INCIDENCIA}**")
        st.warning(f"**INSTRUCCIÓN:** {LBL_ACCION_LITERAL}")
        
        # 4. ACCIÓN DE CRISIS
        if st.button("🚨 ACTIVAR PROTOCOLO DE AYUDA"):
            with st.spinner("Notificando a personal de estación y contactos..."):
                try:
                    registrar_evento("Activación de Protocolo de Ayuda", 5)
                    time.sleep(1.5)
                    st.toast("Ayuda solicitada con éxito.", icon="✅")
                    st.success("Mantén la calma. Alguien viene a tu encuentro en la Salida B.")
                except Exception as e:
                    st.error(f"Error de conexión: {e}. Llama al 112 directamente.")

    # 5. FOOTER DE CIERRE
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1041/1041916.png", width=100)
    st.sidebar.title("Menú Seguro")
    if st.sidebar.button("🏠 Mi Ruta de Regreso"):
        st.toast("Cargando ruta más tranquila a casa...")
