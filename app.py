"""
Entry point de HIGO. Router y orquestador.
"""
import streamlit as st
from ui.styles import apply_custom_styles
from ui.main_page import render_interface
from data.database import init_db

def main():
    # 1. Inicializar persistencia
    init_db()

    # 2. Aplicar capa visual
    apply_custom_styles()

    # 3. Router
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = True # Autologin para el MVP de Marc

    render_interface()

if __name__ == "__main__":
    main()
