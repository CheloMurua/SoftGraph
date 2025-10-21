"""
Clase Pedido: representa un pedido de un cliente.
Incluye cálculo de total y fecha.
Aplica funciones matemáticas: total = cantidad * precio_unitario
"""

from datetime import date

class Pedido:
    def __init__(self, cliente_id, descripcion, cantidad, precio_unitario, fecha=None, id=None):
        self.id = id
        self.cliente_id = cliente_id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha or date.today()

    def calcular_total(self):
        """Calcula el total del pedido"""
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Pedido {self.id} de cliente {self.cliente_id}: {self.descripcion}, Cantidad: {self.cantidad}, Total: ${self.calcular_total():.2f}"
