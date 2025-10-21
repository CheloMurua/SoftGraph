"""
Funciones matemáticas auxiliares.
Ejemplos: aplicar descuentos, calcular combinaciones de servicios, etc.
"""

def aplicar_descuento(total, porcentaje):
    return total * (1 - porcentaje/100)

def calcular_combinaciones_servicios(servicios):
    """Retorna la cantidad de combinaciones posibles"""
    from itertools import combinations
    total = 0
    for r in range(1, len(servicios)+1):
        total += len(list(combinations(servicios, r)))
    return total
