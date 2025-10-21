"""
Service de Pedido: maneja la lógica de negocio sobre pedidos.
Aplica cálculo de totales y posibles descuentos antes de guardar.
"""

from dao.dao import PedidoDAO
from models.pedido import Pedido

class PedidoService:
    def __init__(self, db):
        self.pedido_dao = PedidoDAO(db)

    def agregar_pedido(self, cliente_id, descripcion, cantidad, precio_unitario):
        pedido = Pedido(cliente_id, descripcion, cantidad, precio_unitario)
        total = pedido.calcular_total()
        print(f"Total calculado para el pedido: ${total:.2f}")
        return self.pedido_dao.agregar_pedido(pedido)

    def listar_pedidos(self):
        return self.pedido_dao.listar_pedidos()
