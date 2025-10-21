"""
Clase Presupuesto: genera el presupuesto de un pedido o conjunto de pedidos.
Aplica funciones matemáticas y reglas de negocio (descuentos, promociones).
"""

class Presupuesto:
    def __init__(self, pedidos, descuento=0):
        self.pedidos = pedidos  # lista de objetos Pedido
        self.descuento = descuento  # porcentaje

    def calcular_total(self):
        total = sum(p.calcular_total() for p in self.pedidos)
        total_con_descuento = total * (1 - self.descuento/100)
        return total_con_descuento

    def __str__(self):
        return f"Presupuesto: Total con descuento ({self.descuento}%): ${self.calcular_total():.2f}"
