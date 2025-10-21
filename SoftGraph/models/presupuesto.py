"""
Clase Presupuesto: genera el presupuesto de un pedido o conjunto de pedidos.
Aplica funciones matemáticas y reglas de negocio (descuentos, promociones).
"""

"""
Clase Presupuesto: genera el presupuesto de un pedido o conjunto de pedidos.
Aplica funciones matemáticas y reglas de negocio (descuentos, promociones).
"""

from decimal import Decimal

class Presupuesto:
    def __init__(self, pedidos, descuento=0):
        self.pedidos = pedidos  # lista de objetos Pedido
        self.descuento = Decimal(descuento)  # convertir a Decimal para operaciones seguras

    def calcular_total(self):
        # Convertir cada total de pedido a Decimal
        total = sum(Decimal(p.calcular_total()) for p in self.pedidos)
        # Aplicar descuento
        total_con_descuento = total * (Decimal('1') - self.descuento / Decimal('100'))
        return total_con_descuento

    def __str__(self):
        return f"Presupuesto: Total con descuento ({self.descuento}%): ${self.calcular_total():.2f}"

