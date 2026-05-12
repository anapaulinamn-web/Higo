"""
Inyección de estilos CSS para reducir la carga cognitiva.
"""
import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Tipografía clara y espaciado generoso */
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
            font-size: 18px;
        }
        /* Botones grandes y predecibles */
        .stButton>button {
            height: 4em;
            border: 2px solid #000;
            font-weight: 700;
        }
        /* Alertas sin animaciones distractoras */
        .stAlert {
            border-left: 10px solid;
        }
        </style>
    """, unsafe_allow_html=True)
