"""
Programa principal: instancia DB, Services y ejecuta operaciones.
Simula un flujo real de la imprenta.
"""

from database.database import Database
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.presupuesto_service import PresupuestoService

if __name__ == "__main__":
    db = Database(user='root', password='1234')  # Cambiar según tu configuración
    db.conectar()

    # Servicios
    cliente_service = ClienteService(db)
    pedido_service = PedidoService(db)
    presupuesto_service = PresupuestoService()

    # Agregar cliente
    cliente_service.agregar_cliente("Maria Jose Castro", "25920011", "maria@email.com")

    # Listar clientes
    print("\n=== Clientes ===")
    for c in cliente_service.listar_clientes():
        print(c)

    # Crear pedido
    cliente = cliente_service.cliente_dao.buscar_cliente_por_dni("25920011")
    pedido_service.agregar_pedido(cliente.id, "Impresión Flyers", 500, 2.5)

    # Listar pedidos
    print("\n=== Pedidos ===")
    pedidos = pedido_service.listar_pedidos()
    for p in pedidos:
        print(p)

    # Generar presupuesto
    presupuesto_service.generar_presupuesto(pedidos, descuento=10)

    db.desconectar()
