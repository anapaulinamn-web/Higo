"""
Capa de datos para persistencia de estados de crisis y preferencias de Marc.
"""
import sqlite3
from config import DB_PATH

def init_db():
    """Inicializa la base de datos y crea tablas si no existen."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS logs_crisis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    evento TEXT NOT NULL,
                    nivel_estres INTEGER
                )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error inicializando DB: {e}")

def registrar_evento(evento: str, nivel: int):
    """Guarda un evento de movilidad en la base de datos."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO logs_crisis (evento, nivel_estres) VALUES (?, ?)", (evento, nivel))
    except sqlite3.Error as e:
        raise Exception(f"Fallo al persistir evento: {e}")
