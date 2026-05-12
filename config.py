"""
Configuraciones globales y constantes del sistema HIGO.
"""
import os

# Rutas de archivos (Streamlit Cloud requiere /tmp para escritura)
DB_PATH = "/tmp/higo_persistence.db"

# Umbrales Sensoriales
UMBRAL_RUIDO_ALTO = 75  # Decibelios estimados
MAX_DENSIDAD_PERSONAS = 0.8  # 80% de capacidad

# Mensajes Literales (Evita ambigüedad)
MSG_INCIDENCIA_GENERICA = "Retraso en la línea por causas técnicas."
MSG_INSTRUCCION_HIGO = "No entres al andén. El ruido subirá. Camina hacia la salida B."

# Colores de Interfaz (Accesibilidad)
COLOR_SAFE = "#28A745"
COLOR_WARNING = "#FFC107"
COLOR_DANGER = "#DC3545"
