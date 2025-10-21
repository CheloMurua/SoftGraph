"""
DAO: maneja CRUD de clientes, pedidos y presupuestos.
Aplica técnicas de conteo, lógica y relaciones entre entidades.
"""

from models.cliente import Cliente
from models.pedido import Pedido
from models.presupuesto import Presupuesto
from datetime import datetime

class ClienteDAO:
    def __init__(self, db):
        self.db = db

    def agregar_cliente(self, cliente: Cliente):
        query = "INSERT INTO clientes (nombre, dni, email) VALUES (%s, %s, %s)"
        return self.db.ejecutar_query(query, (cliente.nombre, cliente.dni, cliente.email))

    def listar_clientes(self):
        resultados = self.db.ejecutar_query("SELECT * FROM clientes")
        return [Cliente(r['nombre'], r['dni'], r['email'], r['id']) for r in resultados]

    def buscar_cliente_por_dni(self, dni):
        resultados = self.db.ejecutar_query("SELECT * FROM clientes WHERE dni=%s", (dni,))
        if resultados:
            r = resultados[0]
            return Cliente(r['nombre'], r['dni'], r['email'], r['id'])
        return None
    # dao.py, dentro de ClienteDAO
    def eliminar_cliente(self, cliente_id):
        """
        Elimina un cliente por su ID.
        """
        query = "DELETE FROM clientes WHERE id=%s"
        return self.db.ejecutar_query(query, (cliente_id,))


class PedidoDAO:
    def __init__(self, db):
        self.db = db

    def agregar_pedido(self, pedido: Pedido):
        query = "INSERT INTO pedidos (cliente_id, descripcion, cantidad, precio_unitario, fecha) VALUES (%s, %s, %s, %s, %s)"
        return self.db.ejecutar_query(query, (pedido.cliente_id, pedido.descripcion, pedido.cantidad, pedido.precio_unitario, pedido.fecha))

    def listar_pedidos(self):
        resultados = self.db.ejecutar_query("SELECT * FROM pedidos")
        return [Pedido(r['cliente_id'], r['descripcion'], r['cantidad'], r['precio_unitario'], r['fecha'], r['id']) for r in resultados]
    # dao.py, dentro de PedidoDAO
    def eliminar_pedido(self, pedido_id):
        """
        Elimina un pedido por su ID.
        """
        query = "DELETE FROM pedidos WHERE id=%s"
        return self.db.ejecutar_query(query, (pedido_id,))

class PresupuestoDAO:
    def __init__(self, db):
        self.db = db

    def agregar_presupuesto(self, cliente_id, total, descuento=0):
        """
        Inserta un nuevo presupuesto en la base de datos.
        """
        query = """
        INSERT INTO presupuestos (cliente_id, total, descuento, fecha)
        VALUES (%s, %s, %s, %s)
        """
        fecha = datetime.now()
        return self.db.ejecutar_query(query, (cliente_id, total, descuento, fecha))

    def listar_presupuestos(self):
        """
        Retorna una lista de objetos Presupuesto desde la base de datos.
        """
        query = "SELECT * FROM presupuestos"
        resultados = self.db.ejecutar_query(query)
        if resultados:
            return [
                Presupuesto(
                    cliente_id=r['cliente_id'],
                    total=r['total'],
                    descuento=r['descuento'],
                    fecha=r['fecha'],
                    id=r['id']
                )
                for r in resultados
            ]
        return []

    def buscar_presupuesto_por_id(self, presupuesto_id):
        """
        Retorna un presupuesto específico por su ID.
        """
        query = "SELECT * FROM presupuestos WHERE id=%s"
        resultados = self.db.ejecutar_query(query, (presupuesto_id,))
        if resultados:
            r = resultados[0]
            return Presupuesto(
                cliente_id=r['cliente_id'],
                total=r['total'],
                descuento=r['descuento'],
                fecha=r['fecha'],
                id=r['id']
            )
        return None