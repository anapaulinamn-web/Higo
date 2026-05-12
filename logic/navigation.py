"""
Lógica pura para validación y cálculo de rutas sensoriales.
"""
from config import UMBRAL_RUIDO_ALTO, MAX_DENSIDAD_PERSONAS

def evaluar_seguridad_tramo(decibelios: int, ocupacion: float) -> bool:
    """
    Valida inputs y decide si el entorno es apto.
    """
    # Validación de frontera
    if not (30 <= decibelios <= 120):
        return False
    if not (0.0 <= ocupacion <= 1.0):
        return False
        
    if decibelios > UMBRAL_RUIDO_ALTO or ocupacion > MAX_DENSIDAD_PERSONAS:
        return False
    return True

def obtener_instruccion_literal(es_seguro: bool, tramo: str) -> str:
    """
    Genera microcopy directo basado en el estado.
    """
    if es_seguro:
        return f"El tramo {tramo} es predecible. Puedes avanzar."
    return f"Imprevisto en {tramo}. Detente y sigue la ruta espejo."
