"""
Clase Presupuesto: genera el presupuesto de un pedido o conjunto de pedidos.
Aplica funciones matemáticas y reglas de negocio (descuentos, promociones).
"""

class Presupuesto:
    def __init__(self, id=None, cliente_id=None, total=0, descuento=0, total_final=0, fecha=None):
        self.id = id
        self.cliente_id = cliente_id
        self.total = total
        self.descuento = descuento
        self.total_final = total_final
        self.fecha = fecha
        
    def calcular_total(self):
        total = sum(p.calcular_total() for p in self.pedidos)
        total_con_descuento = total * (1 - self.descuento/100)
        return total_con_descuento
    
    def __str__(self):
        return (
            f"Presupuesto(ID: {self.id}, ClienteID: {self.cliente_id}, "
            f"Total: ${self.total:.2f}, Descuento: {self.descuento}%, "
            f"Total Final: ${self.total_final:.2f}, Fecha: {self.fecha})"
        )
