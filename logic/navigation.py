"""
Lógica pura para la toma de decisiones de ruta basada en datos sensoriales.
"""
from config import UMBRAL_RUIDO_ALTO, MAX_DENSIDAD_PERSONAS

def evaluar_seguridad_tramo(decibelios: int, ocupacion: float) -> bool:
    """
    Determina si un tramo es seguro sensorialmente.
    Inputs: decibelios (int), ocupacion (float 0-1)
    Outputs: bool (True si es seguro)
    """
    if decibelios > UMBRAL_RUIDO_ALTO or ocupacion > MAX_DENSIDAD_PERSONAS:
        return False
    return True

def obtener_instruccion_literal(es_seguro: bool, tramo_nombre: str) -> str:
    """Retorna la acción exacta a realizar."""
    if not es_seguro:
        return f"Tramo {tramo_nombre} saturado. Usa la ruta alternativa por el exterior."
    return f"Tramo {tramo_nombre} despejado. Continúa con calma."
