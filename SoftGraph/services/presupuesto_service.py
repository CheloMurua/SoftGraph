from models.presupuesto import Presupuesto

class PresupuestoService:
    def __init__(self):
        pass  # No necesita DAO, trabaja con objetos Pedido en memoria

    def generar_presupuesto(self, pedidos, descuento=0):
        presupuesto = Presupuesto(pedidos, descuento)
        print(presupuesto)
        return presupuesto
