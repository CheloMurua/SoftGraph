from decimal import Decimal
from models.presupuesto import Presupuesto
from datetime import datetime

class PresupuestoService:
    def __init__(self, db, presupuesto_dao):
        self.db = db
        self.presupuesto_dao = presupuesto_dao

    def generar_presupuesto(self, pedidos, descuento):
        if not pedidos:
            print("⚠️ No hay pedidos disponibles para generar un presupuesto.")
            return None

        # Calcular el total general
        total = Decimal(sum(float(p.precio_unitario) * int(p.cantidad) for p in pedidos))

        descuento_decimal = Decimal(descuento) / Decimal(100)
        total_con_descuento = total * (Decimal(1) - descuento_decimal)

        print("\n=== 💼 PRESUPUESTO GENERADO ===")
        print(f"Total sin descuento: ${total:.2f}")
        print(f"Descuento aplicado: {descuento}%")
        print(f"Total con descuento: ${total_con_descuento:.2f}")
        print("===============================")

        # Tomar cliente_id desde el primer pedido (asumiendo todos del mismo cliente)
        cliente_id = pedidos[0].cliente_id if pedidos else None

        # Crear el objeto Presupuesto
        presupuesto = Presupuesto(
            cliente_id=cliente_id,
            total=total_con_descuento,
            descuento=Decimal(descuento),
            fecha=datetime.now()
        )

        # Guardar en base de datos
        try:
            self.presupuesto_dao.agregar_presupuesto(cliente_id, total_con_descuento, descuento)
            print("✅ Presupuesto guardado correctamente en la base de datos.")
        except Exception as e:
            print(f"❌ Error al guardar presupuesto: {e}")

        return presupuesto
