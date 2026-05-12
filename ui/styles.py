import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
            color: #1A1A1A;
        }
        
        .stAlert {
            border: 2px solid #000;
            border-radius: 8px;
        }
        
        .stButton>button {
            border: 2px solid #1A1A1A;
            border-radius: 12px;
            font-size: 20px !important;
            transition: 0.2s;
        }
        
        .stButton>button:hover {
            background-color: #F0F0F0;
            transform: translateY(-2px);
        }
        
        /* Ocultar elementos innecesarios para reducir distracción */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
