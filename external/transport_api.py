import requests
import streamlit as st

def fetch_metro_alerts():
    url = "https://api.tu-ciudad.es/v1/alerts"
    headers = {"Authorization": f"Bearer {st.secrets['TRANSPORT_API_KEY']}"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        return response.json() # Devuelve los retrasos reales
    except Exception:
        return None # Resiliencia: si falla, HIGO usa modo seguro
