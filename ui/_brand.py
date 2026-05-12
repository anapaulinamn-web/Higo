import streamlit as st

def inject_brand():
    """
    Inyecta la identidad visual de HIGO mediante CSS custom.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Outfit:wght@700&family=JetBrains+Mono&display=swap');

        :root {
            --primary: #4A90E2;
            --bg: #FFFFFF;
            --surface: #F4F7F9;
            --text: #1A2B3C;
            --radius-lg: 24px;
            --radius-md: 12px;
        }

        /* Títulos */
        h1, h2, h3 {
            font-family: 'Outfit', sans-serif !important;
            color: var(--text) !important;
            letter-spacing: -0.02em;
        }

        /* Botones amigables */
        .stButton>button {
            border-radius: var(--radius-md) !important;
            border: 1px solid #E0E0E0 !important;
            background-color: var(--bg) !important;
            color: var(--text) !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 500 !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:hover {
            border-color: var(--primary) !important;
            color: var(--primary) !important;
            background-color: var(--surface) !important;
        }

        /* Inputs y Cards */
        .stTextInput>div>div>input, .stSelectbox>div>div>div {
            border-radius: var(--radius-md) !important;
            border: 1px solid #E0E0E0 !important;
        }

        [data-testid="stExpander"], .stAlert {
            border-radius: var(--radius-md) !important;
            border: none !important;
            background-color: var(--surface) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        }

        /* Sidebar Limpio */
        [data-testid="stSidebar"] {
            background-color: var(--surface) !important;
            border-right: 1px solid #E0E0E0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
