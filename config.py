"""
Configuraciones globales y constantes de diseño para HIGO.
"""
import os

# Persistencia
DB_PATH = "/tmp/higo_persistence.db"

# Umbrales Sensoriales de Marc (Default)
UMBRAL_RUIDO_ALTO = 75 
MAX_DENSIDAD_PERSONAS = 0.7 

# Microcopy de Producto (Evitar lenguaje genérico)
LBL_CARGANDO = "Analizando entorno sensorial..."
LBL_EXITO_RUTA = "Ruta despejada. Tienes el control."
LBL_ALERTA_INCIDENCIA = "¡Atención! Cambio en el entorno detectado."
LBL_ACCION_LITERAL = "Tu instrucción: Sal del metro ahora y usa la Ruta Espejo."

# Colores de Semáforo Sensorial
COLOR_SAFE = "#D4EDDA"
COLOR_WARNING = "#FFF3CD"
COLOR_DANGER = "#F8D7DA"
